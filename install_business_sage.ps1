# ==============================================================================
# BUSINESS SAGE - UNIVERSAL AUTO-DISCOVERY & EXPLICIT INSTALLER (POWERSHELL)
# Supports:
#   1) Zero-config Smart Auto-Discovery across all drives for Hermes (#1),
#      OpenClaw, Claude, ChatGPT/Codex & Universal Agents:
#        .\install_business_sage.ps1
#        .\install_business_sage.ps1 -Scope all
#   2) Explicit Target Mode (compatible with Launch Guide PDF):
#        .\install_business_sage.ps1 -TargetSkillsDir "$HOME\.hermes\skills" -Scope business -WhatIf
# Safety:
#   - 100% preserves Hermes config.yaml, provider, model, and SOUL.md.
# ==============================================================================
[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [string]$TargetSkillsDir = "",
    [ValidateSet("business", "all")][string]$Scope = "business",
    [switch]$HermesOnly,
    [switch]$CopyFiles,
    [switch]$DryRun,
    [string]$HermesHome = "",
    [string]$CloneDir = ""
)

$ErrorActionPreference = "Stop"
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$RepoOwner = "zidanaisar624"
$RepoName  = "hermes-business-sage-and-agent-skills"
$RepoUrl   = "https://github.com/$RepoOwner/$RepoName.git"

# 1. Resolve local repo root (supports local execution AND remote `irm .../install.ps1 | iex`)
$ScriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { "" }
if ($ScriptDir -and (Test-Path (Join-Path $ScriptDir "skills\business-sage\SKILL.md"))) {
    $RepoRoot = (Resolve-Path $ScriptDir).Path
} else {
    $DefaultBase = if ($CloneDir) { $CloneDir } else { Join-Path $env:LOCALAPPDATA "business-sage-cli\repo" }
    $RepoRoot = $DefaultBase
    Write-Host "[*] Preparing local Business Sage repository at: $RepoRoot" -ForegroundColor Cyan
    if (-not (Test-Path (Join-Path $RepoRoot "skills\business-sage\SKILL.md"))) {
        New-Item -ItemType Directory -Force -Path (Split-Path $RepoRoot -Parent) | Out-Null
        if (Get-Command git -ErrorAction SilentlyContinue) {
            git clone $RepoUrl $RepoRoot
        } else {
            $ZipTmp = Join-Path $env:TEMP "bsage_bootstrap.zip"
            $ExtractTmp = Join-Path $env:TEMP "bsage_bootstrap_extract"
            Invoke-WebRequest -Uri "https://codeload.github.com/$RepoOwner/$RepoName/zip/refs/heads/main" -OutFile $ZipTmp -UseBasicParsing
            if (Test-Path $ExtractTmp) { Remove-Item $ExtractTmp -Recurse -Force }
            Expand-Archive -Path $ZipTmp -DestinationPath $ExtractTmp -Force
            $Inner = Get-ChildItem -Path $ExtractTmp -Directory | Select-Object -First 1
            New-Item -ItemType Directory -Force -Path $RepoRoot | Out-Null
            Copy-Item -Path (Join-Path $Inner.FullName "*") -Destination $RepoRoot -Recurse -Force
        }
    }
}

$EffectiveDryRun = [bool]($DryRun -or $WhatIfPreference)

# 2. Prefer Python deep-discovery harness when Python 3 is available
$PythonCmd = $null
foreach ($cand in @("python", "python3", "py")) {
    if (Get-Command $cand -ErrorAction SilentlyContinue) {
        try {
            $ver = & $cand --version 2>&1
            if ($LASTEXITCODE -eq 0 -and "$ver" -match "Python 3") {
                $PythonCmd = $cand
                break
            }
        } catch {}
    }
}

if ($PythonCmd) {
    $PyArgs = @((Join-Path $RepoRoot "install.py"), "--scope", $Scope, "--export-chatgpt")
    if ($TargetSkillsDir) {
        if (-not [System.IO.Path]::IsPathRooted($TargetSkillsDir)) {
            throw "TargetSkillsDir must be an absolute path."
        }
        $PyArgs += @("--target", ([System.IO.Path]::GetFullPath($TargetSkillsDir)))
    }
    if ($HermesOnly)      { $PyArgs += "--hermes-only" }
    if ($CopyFiles)       { $PyArgs += "--copy" }
    if ($EffectiveDryRun) { $PyArgs += "--dry-run" }
    if ($HermesHome)      { $PyArgs += @("--hermes-home", $HermesHome) }

    & $PythonCmd @PyArgs
    $ExitCode = $LASTEXITCODE
    $BinDir = Join-Path $env:LOCALAPPDATA "business-sage-cli\bin"
    if ((Test-Path $BinDir) -and ($env:PATH -notlike "*$BinDir*")) {
        $env:PATH = "$BinDir;$env:PATH"
    }
    Write-Host "`n[TIP] In PowerShell or CMD anytime, type: bsage check  or  bsage update" -ForegroundColor Green
    exit $ExitCode
}

# 3. Pure PowerShell Zero-Python Fallback
Write-Host "[*] Python 3 not detected -- running Native PowerShell Multi-Drive Discovery..." -ForegroundColor Yellow

$Targets = @()
if ($TargetSkillsDir) {
    $fullTarget = [System.IO.Path]::GetFullPath($TargetSkillsDir)
    $Targets += [PSCustomObject]@{ Label = "Explicit Target ($fullTarget)"; SkillsDir = $fullTarget }
} else {
    $CandHomes = @()
    if ($HermesHome) { $CandHomes += $HermesHome }
    if ($env:HERMES_HOME) { $CandHomes += $env:HERMES_HOME }
    $RegH = [Environment]::GetEnvironmentVariable("HERMES_HOME", "User")
    if ($RegH) { $CandHomes += $RegH }
    $CandHomes += (Join-Path $HOME ".hermes")
    Get-PSDrive -PSProvider FileSystem | ForEach-Object {
        if ($_.Root -and (Test-Path $_.Root)) {
            foreach ($sub in @("HermesData", "Hermes", ".hermes", "Program\HermesData\.hermes")) {
                $CandHomes += (Join-Path $_.Root $sub)
            }
        }
    }
    $Seen = @{}
    foreach ($c in $CandHomes) {
        if ($c -and (Test-Path $c) -and ((Test-Path (Join-Path $c "config.yaml")) -or (Test-Path (Join-Path $c "skills")))) {
            $f = [System.IO.Path]::GetFullPath($c)
            if (-not $Seen.ContainsKey($f)) {
                $Seen[$f] = $true
                $Targets += [PSCustomObject]@{ Label = "Hermes Root ($f)"; SkillsDir = (Join-Path $f "skills") }
            }
        }
    }
}

$CoreSet = @("business-sage", "cli-anything-business-sage")
$SkillFolders = Get-ChildItem -Path (Join-Path $RepoRoot "skills") -Directory | Where-Object {
    (Test-Path (Join-Path $_.FullName "SKILL.md")) -and ($Scope -eq "all" -or ($CoreSet -contains $_.Name))
}

$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
foreach ($t in $Targets) {
    if ($EffectiveDryRun) {
        Write-Host (" [DRY-RUN] {0} -> {1} ({2} skills)" -f $t.Label, $t.SkillsDir, $SkillFolders.Count)
        continue
    }
    New-Item -ItemType Directory -Force -Path $t.SkillsDir | Out-Null
    foreach ($sf in $SkillFolders) {
        $dst = Join-Path $t.SkillsDir $sf.Name
        if (Test-Path -LiteralPath $dst) {
            $bak = Join-Path $t.SkillsDir "$($sf.Name).backup-$Stamp"
            Move-Item -LiteralPath $dst -Destination $bak -Force
        }
        Copy-Item -LiteralPath $sf.FullName -Destination $dst -Recurse -Force
    }
    Write-Host (" [OK] {0} -> {1}" -f $t.Label, $t.SkillsDir) -ForegroundColor Green
}
