# ==============================================================================
# BUSINESS SAGE - TERMINAL UPDATE CHECKER & SELF-UPDATER (POWERSHELL)
# Usage:
#   .\update.ps1 check     (or: bsage check)
#   .\update.ps1 update    (or: bsage update)
# ==============================================================================
$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$RepoRoot = (Resolve-Path $PSScriptRoot).Path
$HarnessDir = Join-Path $RepoRoot "business-sage\agent-harness"
$env:BSAGE_REPO = $RepoRoot
$env:PYTHONPATH = "$HarnessDir;$env:PYTHONPATH"

$PassArgs = if ($args.Count -gt 0) { $args } else { @("update") }

foreach ($cand in @("python", "python3", "py")) {
    if (Get-Command $cand -ErrorAction SilentlyContinue) {
        & $cand -m cli_anything.business_sage @PassArgs
        exit $LASTEXITCODE
    }
}

# Zero-Python Git fallback
$SubCmd = "$($PassArgs[0])".ToLower()
if ($SubCmd -eq "check") {
    git -C $RepoRoot fetch origin main
    $LocalSha  = (git -C $RepoRoot rev-parse HEAD).Trim()
    $RemoteSha = (git -C $RepoRoot rev-parse origin/main).Trim()
    if ($LocalSha -eq $RemoteSha) {
        Write-Host "[OK] Business Sage is UP TO DATE ($($LocalSha.Substring(0,7)))." -ForegroundColor Green
    } else {
        Write-Host "[!] UPDATE AVAILABLE! Run: bsage update" -ForegroundColor Yellow
    }
    exit 0
}

git -C $RepoRoot pull --ff-only origin main
& (Join-Path $RepoRoot "install_business_sage.ps1") -Scope business
