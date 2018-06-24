#Remplir un fichier .xml étape par étape

#Variable pour le fichier xml final
$file="E:\PowerShell\tests\testnuspec.xml"

#On crée le squelette pour le xml
$template = "<package xmlns='http://schemas.microsoft.com/packaging/2015/06/nuspec.xsd'>
<metadata>
<id />
<title />
<version />
<authors />
<owners />
<description />
</metadata>
<files>
    <file src='tools\**' target='tools'/>
</files>
</package>
"

#on doit sauvegarder notre squelette xml pour pouvoir le réinvoquer
$template | out-file E:\PowerShell\tests\testnuspectemp.xml

#on invoque le fichier xml vide
$xml=[xml](Get-Content E:\PowerShell\tests\testnuspectemp.xml)

#On demande à l'utilisateur de remplir les champs
$id = Read-Host "Quelle est l'id du package ?"
Write-Host "ID choisit : $id"
$xml.package.metadata.id=$id.ToString()

$title = Read-Host "Quel est le titre du package ?"
$xml.package.metadata.title=$title.ToString()

$version = Read-Host "Quelle est la version du package ?"
$xml.package.metadata.version=$version.ToString()

$authors = Read-Host "Quel est l'auteur du package ?"
$xml.package.metadata.authors=$authors.ToString()

$owners = Read-Host "Quel est le propriétaire du package ?"
$xml.package.metadata.owners=$owners.ToString()

$description = Read-Host "Quel est la description du package ?"
$xml.package.metadata.description=$description.ToString()


#$xml | out-file E:\PowerShell\tests\testnuspec.xml
$xml.Save("E:\PowerShell\tests\testnuspec.xml")