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
        # On prend l'info que le serveur irc nous envoie (en bytes), on le met dans "ircmsg" et on enlève le retour à la ligne.
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)

        # On regarde si dans ce message il y a PRIVMSG. Dans IRC, un message se trouve sous la forme : ":[Nick]!~[hostname]@[IP Address]PRIVMSG[channel]:[message]" donc on sépare chacun des éléments dans une variable.
        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!',1)[0][1:]
            message = ircmsg.split('PRIVMSG',1)[1].split(':',1)[1]

            # On commence par vérifié que le nom de celui qui a envoyé le message est inférieur à 17 caractères
            if len(name) < 17:
                # Ensuite si, dans le message on trouve une salutation pour le bot, on répond dans le général.
                if message.find('Hi ' + botnick) != -1:
                    sendmsg("Hello " + name + "!")

                # On regarde aussi si il y a une commande dans le message
                if message[:5].find('.tell') != -1:
                    target = message.split(' ', 1)[1]
                    if target.find(' ') != -1:
                        message = target.split(' ', 1)[1]
                        target = target.split(' ')[0]
                    else:
                        target = name
                        message = "Could not parse. The message should be in the format of '.tell [target] [message]' to work properly."
                    sendmsg(message, target)

                # Maintenant on va regarder si le bot a vu un message d'arrêt de la part de l'admin
                if name.lower() == adminname.lower() and message.rstrip() == exitcode:
                    sendmsg("oh...okay. :'(")
                    ircsock.send(bytes("QUIT \n", "UTF-8"))
                    return

            # Si le message n'est pas un PRIVMSG, ça peut quand même être un ping, donc on répond.
        else:
            if ircmsg.find("PING :") != -1:
                ping()

# On appel la fonction main
main()

        
