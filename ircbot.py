#!/usr/bin/python3
import socket


# On définit des variables globales
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.net" # Server
channel = "##bot-testing" # Channel
botnick = "IamaPythonBot" # Le nom du bot
adminname = "Aquoibon" # Mon nom IRC
exitcode = "bye " + botnick


# Pour se connecter à IRC, on a besoin de notre variable "ircsock". IRC est généralement sur le port
# 6667 ou 6697 (avec SSL). Ici on utilise 6667. On a besoin du nom du serveur ("server").
# On doit ensuite se présenter au serveur.

ircsock.connect((server, 6667)) # On se connecte au serveur avec le port 6667
# ensuite on remplit une espèce de formulaire avec dans tous les champs le nom du bot
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick +" "+ botnick + "\n", "UTF-8"))
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # On prend comme nom pour le bot "botnick"


# On définit maintenant des fonctions utiles pour le bot.

# Rejoindre un channel (à l'intérieur d'un serveur)
# Après avoir envoyé la commande "JOIN" on attend que le serveur nous envoie le message : "End of /NAMES list". C'est ce message qui nous indique que nous avons bien rejoint le channel.
def joinchan(chan): # join channel(s).
    ircsock.send(bytes("JOIN "+ chan +"\n", "UTF-8"))
    ircmsg = ""
    while ircmsg.find("End of /NAMES list.") == -1:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

# Fonction Ping Pong, pour répondre au requête PING du serveur, qui vérifie si on est toujours là.
def ping():
    ircsock.send(bytes("PONG :pingis\n", "UTF-8"))

# Fonction pour envoyer un message à "target". Le ":" entre la cible et le message laisse le serveur séparé la cible et le message
def sendmsg(msg, target=channel):
    ircsock.send(bytes("PRIVMSG "+ target +" :"+ msg +"\n", "UTF-8"))

# La fonction Main. La partie continue du bot, elle va appelé les autres fonctions et recevoir les infos du serveur ainsi que déterminé quoi faire avec.
def main():
    joinchan(channel)
    while 1:
        
