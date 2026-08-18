# Windows PowerShell helper script to sync skills/ and plugins/ directories to alex-kassel/skills repository
$ErrorActionPreference = "Stop"
$RepoRoot = $PSScriptRoot | Split-Path -Parent

Write-Host "🚀 Syncing skills/ and plugins/ directories to alex-kassel/skills repository..." -ForegroundColor Cyan

$TempDir = Join-Path ([System.IO.Path]::GetTempPath()) ([System.Guid]::NewGuid().ToString())
git clone https://github.com/alex-kassel/skills.git $TempDir

$TargetSkills = Join-Path $TempDir "skills"
$TargetPlugins = Join-Path $TempDir "plugins"

if (Test-Path $TargetSkills) { Remove-Item -Recurse -Force $TargetSkills }
if (Test-Path $TargetPlugins) { Remove-Item -Recurse -Force $TargetPlugins }

Copy-Item -Recurse -Force (Join-Path $RepoRoot "skills") $TargetSkills
Copy-Item -Recurse -Force (Join-Path $RepoRoot "plugins") $TargetPlugins

Push-Location $TempDir
try {
    git add skills plugins
    $Status = git status --porcelain
    if ($Status) {
        git commit -m "sync(release): update skills/ and plugins/ from architecture-skills maintainer repo"
        git push origin main
        Write-Host "✅ Release sync completed successfully!" -ForegroundColor Green
    } else {
        Write-Host "✅ No changes to sync." -ForegroundColor Yellow
    }
} finally {
    Pop-Location
    Remove-Item -Recurse -Force $TempDir
}
