#Remplir un fichier .xml

#On assume definit la variable $xml avec la commande : . .\ImporterXml.ps1


#On définit des variables avec les informations à rentrer
$Bios=Get-WmiObject -class Win32_Bios | select -ExpandProperty Manufacturer 
$OsVersion=Get-WmiObject -class win32_operatingsystem | select -ExpandProperty Caption
$Memory=Get-WmiObject -class win32_operatingsystem | select @{Name= "Memory Installed";Expression={"{0:N2}" -f ($_.TotalVisibleMemorySize/1MB)}} | Select -ExpandProperty "Memory Installed"
$Process=Get-WmiObject -Class Win32_Processor | select -ExpandProperty Name


#On rentre la variable dans le xml, en lui donnant la qualité de string
$xml.computercollection.computer_info.biosmanufacturer=$Bios.ToString()
$xml.computercollection.computer_info.osversion=$OsVersion.ToString()
$xml.ComputerCollection.computer_info.Memory=$Memory.ToString()
$xml.ComputerCollection.computer_info.Processor=$Process.ToString()


#On sauvegarde la variable xml dans un nouveau fichier
$xml.Save("E:\PowerShell\tests\ComputerInfo.xml")