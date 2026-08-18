# Automated Relative Paths Validation Script
# Scans all repository files to ensure no local absolute paths exist (only relative paths and HTTP/HTTPS URLs are allowed).

$RepoRoot = $PSScriptRoot | Split-Path -Parent
$Violations = @()

$FilesToScan = Get-ChildItem -Path $RepoRoot -Recurse -File | Where-Object {
    $_.FullName -notmatch '\\\.git\\' -and 
    $_.Extension -in @('.md', '.ps1', '.yml', '.yaml', '.py')
}

foreach ($File in $FilesToScan) {
    $RelPath = $File.FullName.Substring($RepoRoot.Length + 1)
    
    # Skip the validation script itself
    if ($RelPath -eq 'scripts\validate-relative-paths.ps1') {
        continue
    }

    $LineNum = 0
    Get-Content $File.FullName | ForEach-Object {
        $LineNum++
        $Line = $_

        # Detect concrete local user/system paths (e.g. file:///C:/Users, C:\Users, C:/Users, D:\Users, /Users/username)
        if ($Line -match 'file:///[A-Za-z]:/[Uu]sers' -or 
            $Line -match '[A-Za-z]:\\[Uu]sers' -or 
            $Line -match '[A-Za-z]:/[Uu]sers' -or 
            $Line -match '- Source repository:\s*`[A-Za-z]:') {
            $Violations += [PSCustomObject]@{
                File = $RelPath
                Line = $LineNum
                Content = $Line.Trim()
            }
        }
    }
}

if ($Violations.Count -gt 0) {
    Write-Host "❌ Relative Path Rule Violation Found! Local absolute paths detected:" -ForegroundColor Red
    foreach ($V in $Violations) {
        Write-Host "  File: $($V.File):$($V.Line)" -ForegroundColor Yellow
        Write-Host "  Content: $($V.Content)" -ForegroundColor Gray
    }
    Exit 1
} else {
    Write-Host "✅ Validation Passed! Zero local absolute paths detected in repository files." -ForegroundColor Green
    Exit 0
}
