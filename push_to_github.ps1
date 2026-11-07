# ==============================================================================
# SAFE NON-FORCE GITHUB PUBLISHER - BUSINESS SAGE REPOSITORY
# Usage:
#   .\push_to_github.ps1 -RepoUrl "https://github.com/zidanaisar624/hermes-business-sage-and-agent-skills.git"
#   .\push_to_github.ps1 -DryRun
# ==============================================================================
[CmdletBinding()]
param(
    [string]$RepoUrl = "https://github.com/zidanaisar624/hermes-business-sage-and-agent-skills.git",
    [string]$Branch = "main",
    [string]$CommitMessage = "feat: publish Business Sage v2.0.0 & 49 Collaborative AI Agent Skills",
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Test-Path ".git")) {
    git init -b $Branch
}

$ExistingOrigin = ""
try { $ExistingOrigin = (git remote get-url origin 2>$null) } catch {}
if (-not $ExistingOrigin) {
    git remote add origin $RepoUrl
} elseif ($ExistingOrigin -ne $RepoUrl -and $PSBoundParameters.ContainsKey("RepoUrl")) {
    git remote set-url origin $RepoUrl
}

Write-Host "=== Target GitHub Remote ===" -ForegroundColor Cyan
git remote -v
Write-Host "`n=== Repository Status ===" -ForegroundColor Cyan
git status --short

if ($DryRun) {
    Write-Host "`n[DRY-RUN] No git commit or push executed." -ForegroundColor Yellow
    exit 0
}

git add -A
$Pending = git status --porcelain
if ($Pending) {
    git commit -m $CommitMessage
}
git branch -M $Branch
git push -u origin $Branch
Write-Host "`n[OK] Published safely to $RepoUrl (without --force)!" -ForegroundColor Green
