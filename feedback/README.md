# Skill Feedback

Store one observed skill problem per Markdown file. Name records `YYYY-MM-DD-<skill>-<short-topic>.md`; add a numeric suffix if a name already exists. Copy `TEMPLATE.md` and never overwrite another record.

Statuses: `observed`, `accepted`, `implemented`, `verified`, `rejected`, `superseded`. Treat `observed`, `accepted`, and `implemented` as unresolved.

- Working-project agents may create `observed` records only when the consuming project's durable instructions authorize the external write. Read this file and copy `TEMPLATE.md` before creating a record.
- Always notify the owner after recording feedback. Stop before an affected action when following or bypassing the suspected rule would change project behavior or state.
- Feedback is evidence, not an approved skill change. Only a separate owner-authorized maintenance session may triage records or edit skills.
- Recommend maintenance at session close when there are at least three unresolved records, one repeated problem, or one serious problem that blocked or risked an incorrect mutation. Also recommend review before a new project or stable skill release.
