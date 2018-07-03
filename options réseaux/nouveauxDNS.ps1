# changer le DNS

$Adressedns = Read-Host -Prompt 'Le nouveaux DNS'


netsh int ip set dns "LanInt" static $Adressedns primary