#Créer un fichier dans le répertoire E:\PowerShell\Scripts
#Fichier testfile1.txt avec This is a text string, à l'intérieur

New-Item -Path "E:\PowerShell\Scripts" -Name "testfile1.txt" -ItemType "file" -Value "This is a text string."