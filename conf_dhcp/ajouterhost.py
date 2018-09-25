#!/usr/bin/python3
import subprocess

mac = input('MAC address :')
os = input('OS : ')
ip = input('Adresse IP : ')
nom = ip
file = "/etc/dhcp/"+nom

# Créer un fichier host
with open(file, "a") as fichier:
	fichier.write("host testing {\n  hardware ethernet ")
	fichier.write(mac)
	fichier.write(';\n  filename "')
	fichier.write(os)
	fichier.write('/pxelinux.0";\n  fixed-address ')
	fichier.write(ip)
	fichier.write(";\n}")

# Ajoute le fichier host créer à dhcpd.conf
with open("/etc/dhcp/dhcpd.conf", "a") as fichier:
        fichier.write('include "{}";'.format(file))


# Redémarre le service DHCP
subprocess.run(["systemctl", "restart", "isc-dhcp-server.service"])
