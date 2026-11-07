# ==============================================================================
# UNIVERSAL AUTO-DISCOVERY INSTALLER (POWERSHELL 5.1 / 7+) - BUSINESS SAGE
# Defaults to Scope="all" (49 skills) or pass -Scope business for the 2 core skills.
# ==============================================================================
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$TargetSkillsDir = "",
    [ValidateSet("business", "all")][string]$Scope = "all",
    [switch]$HermesOnly,
    [switch]$CopyFiles,
    [switch]$DryRun,
    [string]$HermesHome = "",
    [string]$CloneDir = ""
)

$Delegate = Join-Path $PSScriptRoot "install_business_sage.ps1"
if (Test-Path $Delegate) {
    & $Delegate @PSBoundParameters
    exit $LASTEXITCODE
}

$RepoOwner = "zidanaisar624"
$RepoName  = "hermes-business-sage-and-agent-skills"
$RemoteScript = "https://raw.githubusercontent.com/$RepoOwner/$RepoName/main/install_business_sage.ps1"
Invoke-Expression (Invoke-RestMethod -Uri $RemoteScript)
