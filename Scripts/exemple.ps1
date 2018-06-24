Function Get-WMIServices
{
Get-WmiObject win32_service |
Select-Object State,Name,DisplayName,StartMode
}

$Result = Get-WMIServices

Echo "Script terminé."