
# Changer l'adresse IP de LanInt
$Adresseip = Read-Host -Prompt 'Nouvelle adresse IP'

$Mask = Read-Host -Prompt 'Le masque de sous réseau'

$Gateway = Read-Host -Prompt 'La passerelle'

Write-Host "L'adresse IP est '$Adresseip' , le masque '$Mask' , la gateway '$Gateway' "

netsh int ip set address "LanInt" static $Adresseip $Mask $Gateway 1 
