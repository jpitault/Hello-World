#test des property d'un objet

$file=Get-Item "E:\PowerShell\tests\computercollection.xml"
Get-ItemProperty $file
$file.Name
$file.FullName
$file.LastWriteTime
