# Windows PowerShell helper script to sync skills/ and plugins/ directories to alex-kassel/skills repository
$ErrorActionPreference = "Stop"
$RepoRoot = $PSScriptRoot | Split-Path -Parent

Write-Host "🚀 Syncing skills/ and plugins/ directories to alex-kassel/skills repository..." -ForegroundColor Cyan

$TempDir = Join-Path ([System.IO.Path]::GetTempPath()) ([System.Guid]::NewGuid().ToString())
git clone https://github.com/alex-kassel/skills.git $TempDir

# Clean out old top-level tracked files and directories in temp repo (except .git)
Get-ChildItem -Path $TempDir -Exclude ".git" | Remove-Item -Recurse -Force

# Copy fresh directories and root README
$TargetSkills = Join-Path $TempDir "skills"
$TargetPlugins = Join-Path $TempDir "plugins"
$TargetReadme = Join-Path $TempDir "README.md"

Copy-Item -Recurse -Force (Join-Path $RepoRoot "skills") $TargetSkills
Copy-Item -Recurse -Force (Join-Path $RepoRoot "plugins") $TargetPlugins

if (Test-Path (Join-Path $RepoRoot "skills\README.md")) {
    Copy-Item -Force (Join-Path $RepoRoot "skills\README.md") $TargetReadme
}

Push-Location $TempDir
try {
    git add -A
    $Status = git status --porcelain
    if ($Status) {
        git commit -m "sync(release): purge stale legacy folders and update skills/ and plugins/"
        git push origin main
        Write-Host "✅ Release sync completed successfully!" -ForegroundColor Green
    } else {
        Write-Host "✅ No changes to sync." -ForegroundColor Yellow
    }
} finally {
    Pop-Location
    Remove-Item -Recurse -Force $TempDir
}
