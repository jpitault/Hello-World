#Créer un dossier si il n'existe pas



#On demande quel nom de dossier
$dossier=Read-Host "Quel dossier vous voulez ?"

if ( -not (Test-Path -Path "E:\PowerShell\tests\$dossier")) {
    Write-Host "Le dossier n'existe pas, donc on le crée !"
    New-Item -Path E:\PowerShell\tests\$dossier -ItemType "directory"
}
else{
    Write-Host "Ce dossier existe déjà."
}