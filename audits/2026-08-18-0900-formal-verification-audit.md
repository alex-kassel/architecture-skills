# Formal Verification & Mutation Safety Audit

- Target Skill: `skills/guide-architecture-design`
- Target Commit SHA: `886738f80456c21e64177c865181b539c36be8bf`
- Audit Date & Time: `2026-08-18 09:00`
- Auditor Role: Senior Formal Verification & Workflow Security Engineer

---

## Блок 1: Промпт Аудитора (Auditor Prompt)

> [!NOTE]
> Исходный промпт, переданный независимому агенту-аудитору:

```markdown
Ты — строгий инженер по формальной верификации LLM-агентов и системной безопасности workflows. Твоя задача — провести жесткий аудит логики, полноты и операционной надежности скилла дизайна архитектуры: `skills/guide-architecture-design/SKILL.md` и всех его референсов в `skills/guide-architecture-design/references/`.

Твой аудит должен фокусироваться НЕ на красоте текста, а на ЛОГИЧЕСКОЙ НЕПРОТИВОРЕЧИВОСТИ, СТРЕСС-УСТОЙЧИВОСТИ и БЕЗОПАСНОСТИ МУТАЦИЙ.

Проведи глубокий анализ по следующим направлениям:
1. Противоречия и десинхронизация:
   - Найди прямые или косвенные противоречия между правилами в SKILL.md и уточнениями в references/*.md (operating-contract.md, workflow-modes.md, gates-recovery-and-git.md, decision-capture-and-sync.md).
   - Есть ли условия, при которых два правила требуют взаимоисключающих действий от модели?

2. Маршрутизация и граничные условия (Routing & Boundaries):
   - Насколько чётко проведены границы V1? Существуют ли «серые зоны» в запросах пользователя, когда модель может перепутать мутирующий гид `guide-architecture-design` с немутирующим аудитом `audit-architecture-handoff`?
   - Есть ли зацикливания (infinite loops) или тупиковые состояния (deadlocks) в схеме переходов между режимами работы (workflow modes)?

3. Обработка крайних случаев и ошибок (Edge Cases & Fault Tolerance):
   - Как скилл ведет себя при нештатных ситуациях: грязный worktree, interrupted session, незакоммиченные файлы других инструментов, конфликты веток, некорректный или отсутствующий operating contract?
   - Достаточно ли алгоритмизированы шаги восстановления, или агенту приходится «додумывать» действия?

4. Риски несанкционированных мутаций (Data Integrity & Authority):
   - Есть ли лазейки, позволяющие агенту самостоятельно принять архитектурное решение без явного подтверждения владельца (Owner)?
   - Гарантирует ли скилл, что ни один файл проекта или скилла не будет изменен до прохождения всех предварительных гейтов и получения явного consent?

Сформируй структурированный отчет с конкретными ссылками на файлы и строки, категоризируй найденные проблемы по уровню критичности (Critical, Major, Minor) и предложи исправления для каждой из них.
```

---

## Блок 2: Отчет Аудитора (Audit Report)

# Formal Verification & Mutation Safety Audit Report: `guide-architecture-design`

**Auditor Role:** Senior Formal Verification & Workflow Security Engineer  
**Target:** `skills/guide-architecture-design/SKILL.md` and all references (`references/*.md`)  
**Audit Scope:** Logical Consistency, Routing Determinism, Edge-Case Fault Tolerance, and Mutation Integrity  
**Date:** 2026-08-18  

---

### Executive Summary

Audit of the `guide-architecture-design` skill and its associated reference documentation (`operating-contract.md`, `workflow-modes.md`, `gates-recovery-and-git.md`, `decision-capture-and-sync.md`) revealed critical vulnerabilities in state machine transitions, mutation integrity, and git execution boundaries.

While the skill establishes high safety standards (e.g., zero-write preflights, authority mapping, explicit owner confirmation), several **logical contradictions**, **deadlock states**, and **unconstrained execution fallbacks** compromise its operational safety in automated agent environments.

Total Findings Identified: **11**
- 🔴 **Critical (Критический уровень):** 3 issues
- 🟠 **Major (Высокий/Средний уровень):** 5 issues
- 🟡 **Minor (Низкий уровень):** 3 issues

---

### 1. Противоречия и десинхронизация (Contradictions & Desynchronization)

#### 🔴 [C1] Deadlock & Routing Contradiction in Implementation Readiness Gate Execution
- **Файлы и строки:**
  - `SKILL.md:L3`, `SKILL.md:L15`
  - `workflow-modes.md:L11-L12`, `workflow-modes.md:L60-L63`
  - `gates-recovery-and-git.md:L67-L75`
- **Описание проблемы:**  
  В `SKILL.md:L3` заявлено, что данный скилл используется для применения гейта готовности к реализации ("apply a current independent implementation-readiness gate"). `workflow-modes.md:L12` направляет такие запросы напрямую в режим `READINESS_GATE`.  
  Однако, `gates-recovery-and-git.md:L73` требуют, чтобы для прохождения `READINESS_GATE` в репозитории УЖЕ существовал свежий независимый вердикт `IMPLEMENTATION READY`, сформированный скиллом `audit-architecture-handoff`. В то же время `SKILL.md:L15` и `workflow-modes.md:L11` предписывают перенаправлять оценку готовности в `audit-architecture-handoff` с остановкой гида.  
  **Следствие:** Если пользователь обращается к `guide-architecture-design` с запросом "проверь готовность к реализации", а отчет аудита еще не создан, режим `READINESS_GATE` гарантированно возвращает статус `BLOCKED` и переходит в `COMPLETE`, не вызывая и не делегируя аудит. Образуется дедлок.
- **Предлагаемое исправление:**  
  Четко разграничить в `SKILL.md` и `workflow-modes.md`, что `READINESS_GATE` — это пассивная проверка предсуществующего артефакта аудита. Если вердикт аудита отсутствует или устарел, агент обязан вернуть условие блокировки с явной инструкцией владельцу (или перенаправлением) сначала выполнить `audit-architecture-handoff`.

#### 🔴 [C2] Local Git Fallback in Session-Branch Workflow Violates Mutation Boundaries & Preflight
- **Файлы и строки:**
  - `SKILL.md:L19`, `workflow-modes.md:L58`, `gates-recovery-and-git.md:L63`
- **Описание проблемы:**  
  `workflow-modes.md:L58` и `gates-recovery-and-git.md:L63` допускают локальный фоллбэк (`local git fallback`) при слиянии сессионной ветки Draft PR в `main`.  
  Однако выполнение squash-merge локально требует команд: `git checkout main`, `git merge --squash agent/session-<ID>`, `git commit`, `git branch -D`.  
  **Следствие:**  
  1) Это прямо нарушает `SKILL.md:L19` ("Do not ... perform direct unconfirmed pushes to primary production branches" / ограничение мутаций `main`).  
  2) Переключение веток (`git checkout main`) изменяет `.git/HEAD` и рабочую директорию прямо в процессе закрытия сессии, обходя правила zero-write preflight, так как префлайт проверил состояние сессионной ветки, а не `main`.  
  3) Отсутствует проверка рассинхронизации локального `main` с удаленным `origin/main`.
- **Предлагаемое исправление:**  
  Исключить нерегламентированный "local git fallback" для `main` при закрытии сессионных PR. Если CLI `gh` недоступен, агент должен оставить Draft PR открытым, предоставить локальную команду владельцу и зафиксировать незавершенный гейт слияния, либо описать строго регламентированный префлайтом алгоритм локального слияния с проверкой чистоты и актуальности `main`.

#### 🔴 [C3] Logic Conflict Between Mid-Batch Failure Containment and Autonomous Mechanical Retry
- **Файлы и строки:**
  - `gates-recovery-and-git.md:L49-L56` ("Contain failure")
  - `gates-recovery-and-git.md:L57-L59` ("Permit a deterministic mechanical retry")
- **Описание проблемы:**  
  Раздел "Contain failure" (`gates-recovery-and-git.md:L49-L56`) безапелляционно требует: при ошибке редактирования, валидации или коммита СТОПИТЬ мутации, НЕ очищать и НЕ изменять частичное состояние, и переходить в `RECOVERY`.  
  Раздел "Mechanical retry" (`gates-recovery-and-git.md:L57`) разрешает автономный повтор (mechanical retry) без повторного подтверждения владельца (например, создание отсутствующей директории или исправление опечатки в команде).  
  **Следствие:** Если при выполнении батча часть файлов уже была изменена на диске, а валидация упала из-за ошибки в команде, повторная попытка модифицирует состояние диска во время проваленного батча. Это создает прямое противоречие между требованием немедленной заморозки состояния (Contain failure) и разрешением продолжать мутации (Mechanical retry).
- **Предлагаемое исправление:**  
  Добавить в `gates-recovery-and-git.md:L57` жесткое ограничение: механический ретрай БЕЗ участия владельца разрешен ИСКЛЮЧИТЕЛЬНО на этапе preflight/dry-run до совершения ПЕРВОЙ записи на диск. Если хотя бы один файл был изменен на диске, автоматический ретрай запрещен — переход в `RECOVERY` обязателен.

---

### 2. Маршрутизация и граничные условия (Routing & Boundaries)

#### 🟠 [M1] Unspecified Preflight Snapshot Update Rules During Intra-Batch Multi-File Mutations
- **Файлы и строки:**
  - `gates-recovery-and-git.md:L8-L18`, `decision-capture-and-sync.md:L38-L48`
- **Описание проблемы:**  
  `gates-recovery-and-git.md:L18` требует перепроверять baseline непосредственно перед записью. Однако в батче, состоящем из нескольких файлов (например, синхронизация 4 спецификаций), после записи файла №1 рабочее дерево Git больше не совпадает с исходным snapshot.  
  Правила префлайта не описывают математику обновления baseline-состояния *внутри* одного батча между записиями отдельных файлов.  
  **Следствие:** Агент может либо ложно среагировать на собственные изменения как на стороннюю грязь (внешнее вмешательство) и заблокировать батч, либо пропустить некорректную мутацию из-за неверной квалификации диска.
- **Предлагаемое исправление:**  
  Формализовать шаг инкрементального обновления baseline-следа в `gates-recovery-and-git.md:L18`: при последовательной записи файлов в рамках санкционированного батча ожидаемый хэш/дифф baseline автоматически дополняется дайджестом только что успешно записанного файла батча.

#### 🟠 [M2] Overlap & Ambiguity Between Direct Confirmation (`+`) and Mandatory Pushback on Architectural Risk
- **Файлы и строки:**
  - `decision-capture-and-sync.md:L10-L13`, `decision-capture-and-sync.md:L29`
- **Описание проблемы:**  
  `decision-capture-and-sync.md:L29` утверждает, что короткие фразы типа `+` или `OK` однозначно подтверждают активное предложение.  
  Однако `decision-capture-and-sync.md:L10-L13` обязывают агента оказывать бдительный пушбэк (up to 3 attempts) при наличии архитектурных или технических рисков.  
  **Следствие:** Если владелец отправляет `+` на вариант, содержащий явные архитектурные риски (или предложенный владельцем небезопасный компромисс), в спецификации не задан приоритет между Правилом 1 (`+` как однозначное подтверждение) и Секцией 4 (бдительный пушбэк). Возникает уязвимость, при которой опасные решения фиксируются мгновенно по коротким символам `+`.
- **Предлагаемое исправление:**  
  Явно зафиксировать приоритет в `decision-capture-and-sync.md:L29`: Архитектурная бдительность и пушбэк имеют БОЛЕЕ ВЫСОКИЙ приоритет, чем быстрая квалификация `+`. Если подтверждаемый вариант содержит нерешенные архитектурные риски, символ `+` не считается окончательным подтверждением до проведения до 3 попыток пушбэка со стороны агента.

---

### 3. Обработка крайних случаев и ошибок (Edge Cases & Fault Tolerance)

#### 🟠 [M3] Ambiguity in `DIRECT_SYNC` Qualification of "Durable Authority"
- **Файлы и строки:**
  - `operating-contract.md:L22-L34`, `workflow-modes.md:L49`, `decision-capture-and-sync.md:L78-L79`
- **Описание проблемы:**  
  `workflow-modes.md:L49` разрешает режим `DIRECT_SYNC` без повторного подтверждения владельца, если решение "уже подтверждено в устойчивом авторитете" (durable authority).  
  В `operating-contract.md:L24` приведен список авторитетов, но не определены жесткие метаданные состояния (например, мета-теги `ACCEPTED`/`APPROVED` против `PROPOSED`/`DRAFT`).  
  **Следствие:** Если draft-ADR или черновик дорожной карты содержит неисполненную идею, агент может ошибочно счесть ее за "durable authority" и выполнить `DIRECT_SYNC` с массовым изменением спецификаций без согласия владельца в текущей сессии.
- **Предлагаемое исправление:**  
  В `operating-contract.md:L24` внести строгое правило: Артефакт признается `durable authority` для `DIRECT_SYNC` ТОЛЬКО при наличии явного нормативного статуса `ACCEPTED`, `APPROVED` или `CONFIRMED` в его шапке/метаданных. Любой статус `DRAFT`, `PROPOSED` или отсутствие статуса требует режима `DECISION_CAPTURE` с подтверждением.

#### 🟠 [M4] Predecessor Session Closing Vulnerability Without Owner-Supplied Timestamp
- **Файлы и строки:**
  - `operating-contract.md:L50-L53`, `workflow-modes.md:L15`, `workflow-modes.md:L28`, `gates-recovery-and-git.md:L30-L33`
- **Описание проблемы:**  
  `gates-recovery-and-git.md:L30` запрещает придумывать конечный временной штамп и молча закрывать чужие сессии.  
  Если в проекте осталась незакрытая сессия от *предыдущего разговора* (interrupted session), а пользователь просит "закрой сессию", `workflow-modes.md:L28` требует привязаться к активной сессии. Если агент попытается закрыть её с помощью текущих системных часов (`observed_at`), он фактически выдумает время завершения чужой сессии из предыдущего диалога.
- **Предлагаемое исправление:**  
  Указать в `gates-recovery-and-git.md:L32`, что при закрытии незавершенной предшествующей сессии из ДРУГОГО разговора временная метка завершения ДОЛЖНА быть явно предоставлена или подтверждена владельцем, либо взята из последнего валидированного лога хоста.

#### 🟠 [M5] Under-Specified Recovery Algorithm for Pre-Existing Dirty Targets
- **Файлы и строки:**
  - `operating-contract.md:L18`, `workflow-modes.md:L15-L19`, `gates-recovery-and-git.md:L13-L18`, `gates-recovery-and-git.md:L27`
- **Описание проблемы:**  
  Если в рабочей директории проекта до вызова скилла находились незакоммиченные ручные правки пользователя в файле, который попадает в текущий батч (например, `AGENTS.md`), префлайт блокирует батч. Скилл переходит в `RECOVERY`, однако не дает конкретного дерева решений для интеграции этой грязи.
- **Предлагаемое исправление:**  
  Добавить в `gates-recovery-and-git.md:L27` двухвариантное меню восстановления:  
  Вариант 1 (Владелец коммитит/стэшит свои сторонние правки),  
  Вариант 2 (Владелец явно авторизует включение имеющегося диффа в качестве исходного baseline для текущего батча).

---

### 4. Риски несанкционированных мутаций (Data Integrity & Authority)

#### 🟡 [m1] Exclusion of Feedback Artifact Paths in Zero-Write Batch Preflight Target Enumeration
- **Файлы и строки:**
  - `SKILL.md:L51-L53`, `gates-recovery-and-git.md:L10`
- **Описание проблемы:**  
  `SKILL.md:L51` разрешает запись обратной связи (`observed` record) в сконфигурированное назначение внутри проекта. Однако `gates-recovery-and-git.md:L10` перечисляет список путей для префлайта, но забывает указать пути фидбек-артефактов.
- **Предлагаемое исправление:**  
  Добавить `feedback record path` в перечень проверяемых путей префлайта в `gates-recovery-and-git.md:L10`.

#### 🟡 [m2] Missing GitHub CLI / Draft PR Failure Fallbacks in `SESSION_BINDING`
- **Файлы и строки:**
  - `workflow-modes.md:L30`, `gates-recovery-and-git.md:L45`
- **Описание проблемы:**  
  Режим `SESSION_BINDING` при работе с сессионной веткой обязывает выполнять push и создавать Eager Draft PR через `gh pr create`. Не указаны действия при отсутствии авторизации в GitHub CLI или сбоях сети.
- **Предлагаемое исправление:**  
  Добавить алгоритм фоллбэка: при ошибке `gh pr create` зафиксировать локальную сессионную ветку, уведомить владельца и продолжать работу в локальном режиме без Draft PR.

#### 🟡 [m3] Ambiguity in Timestamp Observation Reuse Across Multi-Turn Sessions
- **Файлы и строки:**
  - `operating-contract.md:L49-L53`
- **Описание проблемы:**  
  `operating-contract.md:L50` предписывает снимать метку времени при первой возможности вызова инструмента, но не уточняет, обновляется ли метка при многоходных инструментах на этапе закрытия.
- **Предлагаемое исправление:**  
  Уточнить: Метка старта сессии фиксируется при связывании (`SESSION_BINDING`), а метка закрытия сессии (`SESSION_CLOSING`) считывается заново в момент выполнения инструмента закрытия.

---

## Блок 3: Отчет о проделанной работе и Триаже (Work Done & Resolution Report)

Все 11 замечаний аудитора были рассмотрены, утверждены владельцем и полностью реализованы в коде скилла:

| ID | Статус Триажа | Решение и Внесенные Правки | Затронутые Файлы | Статус Верификации |
| :--- | :--- | :--- | :--- | :--- |
| **C1** | `accepted` | Уточнено, что `READINESS_GATE` — пассивная проверка. При отсутствии отчета возвращается условие блокировки с вызовом `audit-architecture-handoff`. | [`SKILL.md`](skills/guide-architecture-design/SKILL.md#L15), [`workflow-modes.md`](skills/guide-architecture-design/references/workflow-modes.md#L12) | Verified (`evals/forward-tests.md:L63`) |
| **C2** | `accepted` | Исключен прямой local squash-merge в `main`. Требуется вызов PR CLI (`gh`/`glab`/UI) или явный префлайт на `main`. | [`workflow-modes.md`](skills/guide-architecture-design/references/workflow-modes.md#L58), [`gates-recovery-and-git.md`](skills/guide-architecture-design/references/gates-recovery-and-git.md#L63) | Verified (`evals/forward-tests.md:L63`) |
| **C3** | `accepted` | Автономный mechanical retry ограничен ИСКЛЮЧИТЕЛЬНО фазой dry-run preflight ДО первой записи на диск. После записи — только `RECOVERY`. | [`gates-recovery-and-git.md`](skills/guide-architecture-design/references/gates-recovery-and-git.md#L51) | Verified (`evals/forward-tests.md:L63`) |
| **M1** | `accepted` | Добавлен инкрементальный расчет baseline-дайджестов после каждого записанного файла внутри мульти-файлового батча. | [`gates-recovery-and-git.md`](skills/guide-architecture-design/references/gates-recovery-and-git.md#L18) | Verified (`evals/forward-tests.md:L63`) |
| **M2** | `accepted` *(с уточнением)* | Пушбэк при архитектурном риске ограничен 1 попыткой предупреждения. Символ `+` однозначно подтверждает capture после 1 предупреждения. | [`decision-capture-and-sync.md`](skills/guide-architecture-design/references/decision-capture-and-sync.md#L12) | Verified (`evals/forward-tests.md:L65`) |
| **M3** | `accepted` | Статус `durable authority` квалифицируется только при наличии явных метаданных `ACCEPTED`/`APPROVED`. Документы `DRAFT`/`PROPOSED` требуют согласования. | [`operating-contract.md`](skills/guide-architecture-design/references/operating-contract.md#L34) | Verified (`evals/forward-tests.md:L64`) |
| **M4** | `accepted` | Время закрытия чужой прерванной сессии берется по системным часам хоста с меткой `interrupted_recovered_at`. | [`gates-recovery-and-git.md`](skills/guide-architecture-design/references/gates-recovery-and-git.md#L30) | Verified (`evals/forward-tests.md:L63`) |
| **M5** | `accepted` | Добавлено 2-вариантное меню восстановления при чужих незакоммиченных файлах в целевых путях батча. | [`gates-recovery-and-git.md`](skills/guide-architecture-design/references/gates-recovery-and-git.md#L31) | Verified (`evals/forward-tests.md:L63`) |
| **m1** | `accepted` | Пути `feedback` добавлены в список обязательной проверки префлайта. | [`gates-recovery-and-git.md`](skills/guide-architecture-design/references/gates-recovery-and-git.md#L9) | Verified (`evals/forward-tests.md:L63`) |
| **m2** | `accepted` | При сбое PR CLI сохраняется локальная сессионная ветка `agent/session-<ID>` с выдачей инструкции владельцу. | [`workflow-modes.md`](skills/guide-architecture-design/references/workflow-modes.md#L30) | Verified (`evals/forward-tests.md:L65`) |
| **m3** | `accepted` | Время закрытия многоходной сессии фиксируется заново в момент вызова инструмента закрытия. | [`operating-contract.md`](skills/guide-architecture-design/references/operating-contract.md#L49) | Verified (`evals/forward-tests.md:L63`) |
