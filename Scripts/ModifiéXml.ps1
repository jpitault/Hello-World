#Test modifié un xml déjà rempli

#on invoque le xml
$file="E:\PowerShell\tests\ComputerInfo.xml"
$xml=[xml](Get-Content $file)

#on modifie les valeurs du xml
$xml.computercollection.computer_info.biosmanufacturer="test1"
$xml.computercollection.computer_info.osversion="test2"
$xml.ComputerCollection.computer_info.Memory="test3"
$xml.ComputerCollection.computer_info.Processor="test4"

#on sauvegarde les modifications
$xml.Save($file)


#on lance le xml pour vérifié
Invoke-Item "$file"