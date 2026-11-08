[CmdletBinding(SupportsShouldProcess)]
param(
    [ValidateSet('Codex','Claude','Agents')]
    [string[]]$Targets = @('Codex','Claude','Agents')
)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path $PSScriptRoot -Parent
$skillNames = @('using-im','implanner','imteacher','imsupervisor','imreflect','imcompanion')
$targetRoots = @{
    Codex = Join-Path $env:USERPROFILE '.codex\skills'
    Claude = Join-Path $env:USERPROFILE '.claude\skills'
    Agents = Join-Path $env:USERPROFILE '.agents\skills'
}
$runName = (Get-Date -Format 'yyyyMMdd-HHmmss') + '-' + [guid]::NewGuid().ToString('N').Substring(0,8)
$backupRoot = Join-Path $projectRoot ('backups\' + $runName)
$installed = @()
foreach ($runtime in $Targets) {
    $runtimeRoot = $targetRoots[$runtime]
    foreach ($name in $skillNames) {
        $sourceDir = Join-Path $projectRoot ('skills\' + $name)
        if (-not (Test-Path -LiteralPath (Join-Path $sourceDir 'SKILL.md'))) { throw "Missing source: $sourceDir" }
        $targetDir = Join-Path $runtimeRoot $name
        if (-not $PSCmdlet.ShouldProcess($targetDir, 'Back up existing skill, copy source and verify file hashes')) { continue }
        if (Test-Path -LiteralPath $targetDir) {
            $backupDir = Join-Path $backupRoot ($runtime + '\' + $name)
            New-Item -ItemType Directory -Path (Split-Path $backupDir -Parent) -Force | Out-Null
            Copy-Item -LiteralPath $targetDir -Destination $backupDir -Recurse
        }
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
        Get-ChildItem -LiteralPath $sourceDir -Force | Copy-Item -Destination $targetDir -Recurse -Force
        foreach ($file in Get-ChildItem -LiteralPath $sourceDir -Recurse -File) {
            $relative = $file.FullName.Substring($sourceDir.Length).TrimStart('\')
            $destination = Join-Path $targetDir $relative
            if ((Get-FileHash -LiteralPath $file.FullName).Hash -ne (Get-FileHash -LiteralPath $destination).Hash) {
                throw "Hash mismatch: $destination"
            }
        }
        $installed += [pscustomobject]@{ runtime=$runtime; skill=$name; path=$targetDir }
    }
}
if ($installed.Count -gt 0) {
    New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
    $installed | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $backupRoot 'installation.json') -Encoding utf8
}
$installed | Format-Table -AutoSize
if (Test-Path -LiteralPath $backupRoot) { Write-Output "Backup and manifest: $backupRoot" }
