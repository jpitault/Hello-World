# Créer un fichier .xml

$template = "<ComputerCollection version='1.0'>
<computer_info>
<biosmanufacturer />
<osversion />
<Memory />
<Processor/>
</computer_info>
</ComputerCollection> 
"
$template | out-file E:\PowerShell\tests\computercollection.xml