#!/usr/bin/python3

# Envoie et réception des messages par IRC, utilisation de 2 threads
import socket, sys, threading


# On définit des variables globales
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "chat.freenode.org" # Server
channel = "##bot-testing" # Channel
botnick = "aquoibonBot" # Le nom du bot
adminname = "Aquoibon" # Mon nom IRC
exitcode = "bye " + botnick



# Fonctions dont on a besoin.

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

# On peut se servir de sendmsg pour parler en privé, ou alors on fait une fonction whisper
def whisper(msg, user):
    ircsock.send(bytes("PRIVMSG "+ user + " :" + msg.strip("\n\r") + "\n", "UTF-8"))


# On va essayé de Threadé pour pouvoir parler avec le bot. Donc on sépare les instructions en 2
class ThreadEmission(threading.Thread):
    # objet thread gérant l'émission des messages
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.ircsock = conn     # réf. du socket de connexion

    def run(self):
        while 1:
            message_emis = input()
            chan = "##bot-testing"
            sendmsg(message_emis, chan)

class ThreadReception(threading.Thread):
    # objet thread gérant la réception et le tri des messages
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.ircsock = conn     # réf. du socket de connexion

    def run(self):
        while 1:
            ircmsg = ircsock.recv(2048).decode("UTF-8")
            ircmsg = ircmsg.strip("\n\r")
            print(ircmsg)
            # et on répond au ping
            if ircmsg.find("PING :") != -1:
                ping()
            # Si on reçoit le message FIN on s'arrête, le tout dans un PRIVMSG
            if ircmsg.find("PRIVMSG") != -1:
                name = ircmsg.split("!",1)[0][1:]
                message = ircmsg.split("PRIVMSG",1)[1].split(":",1)[1]
                if name.lower() == adminname.lower() and message.rstrip() == exitcode:
                    sendmsg("oh...okay. :'(")
                    ircsock.send(bytes("QUIT \n", "UTF-8"))
                    return



# Pour se connecter à IRC, on a besoin de notre variable "ircsock". IRC est généralement sur le port
# 6667 ou 6697 (avec SSL). Ici on utilise 6667. On a besoin du nom du serveur ("server").
# On doit ensuite se présenter au serveur.

ircsock.connect((server, 6667)) # On se connecte au serveur avec le port 6667
# ensuite on remplit une espèce de formulaire avec dans tous les champs le nom du bot
ircsock.send(bytes("USER "+ botnick +" "+ botnick +" "+ botnick +" "+ botnick + "\n", "UTF-8"))
ircsock.send(bytes("NICK "+ botnick +"\n", "UTF-8")) # On prend comme nom pour le bot "botnick"

# on rejoint le chan
joinchan(channel)

# on appel nos threads
th_E = ThreadEmission(ircsock)
th_R = ThreadReception(ircsock)
th_E.start()
th_R.start()
