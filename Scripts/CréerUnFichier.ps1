#Cr�er un fichier dans le r�pertoire E:\PowerShell\Scripts
#Fichier testfile1.txt avec This is a text string, � l'int�rieur

New-Item -Path "E:\PowerShell\Scripts" -Name "testfile1.txt" -ItemType "file" -Value "This is a text string."