# C:\Users\donan\OneDrive\OneDrive Documents\PowerShell\Microsoft.PowerShell_profile.ps1

console = $host.ui.rawui
$console.backgroundcolor = "white"
$console.foregroundcolor = "black"
$host.privatedata.FormatAccentColor = "Magenta"
$host.privatedata.ErrorAccentColor = "Red"
$host.privatedata.ErrorForegroundColor = "Cyan"
$host.privatedata.ErrorBackgroundColor = "White"
$host.privatedata.WarningForegroundColor = "Blue"
$host.privatedata.WarningBackgroundColor = "White"
$host.privatedata.DebugForegroundColor = "Blue"
$host.privatedata.DebugBackgroundColor = "White"
$host.privatedata.VerboseForegroundColor = "Blue"
$host.privatedata.VerboseBackgroundColor = "White"
$host.privatedata.ProgressForegroundColor = "White"
$host.privatedata.ProgressBackgroundColor = "Blue"

Set-PSReadLineOption -Colors @{ "Command"="`e[97;94m" }
Set-PSReadLineOption -Colors @{ "Member"="`e[95m" }
Set-PSReadLineOption -Colors @{ "Number"="`e[95m" }
Set-PSReadLineOption -Colors @{ "ListPredictionSelected"="`e[38;5;238m" }
Set-PSReadLineOption -Colors @{ "Type"="`e[33;40m" }

# set-location C:\Users\donan\OneDrive\OneDrive Documents\PowerShell\Microsoft.PowerShell_profile.ps1
Set-Location C:\Users\donan
clear-host
