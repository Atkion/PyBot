#bot.py
# The code for our bot
import cfg
import utils
from time import sleep
import random, subprocess, os, threading, re, socket, time
import streamLabsUtils
#Command Modules
giveaway = []
isOpen = "Closed"

def main():
    # Variables for Commands

    # Networking functions
    s = socket.socket()
    s.connect((cfg.HOST, cfg.PORT))
    s.send("PASS {}\r\n".format(cfg.PASS).encode("utf-8"))
    s.send("NICK {}\r\n".format(cfg.NICK).encode("utf-8"))
    s.send("JOIN #{}\r\n".format(cfg.CHAN).encode("utf-8"))
    s.send("JOIN #{}\r\n".format("octamouselabs").encode("utf-8"))

    CHAT_MSG = re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+")
    utils.send(s, "Joined Channel")


    while True:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)
            message = CHAT_MSG.sub("", response)
            arguments = message.split(" ")
            print (username+message)
            f = open('chatLog.txt','a') # Get the old Refresh Code from the file we saved
            f.write(username+message)
            f.close()
            # Custom Commands
            if "!time" in str(message):
                utils.send(s, username+", it is currently " + time.strftime("%I:%M %p %Z on %A, %B %d, %Y."))
                print (cfg.NICK+" :It is currently " + time.strftime("%I:%M %p %Z on %A, %B %d, %Y."))
            elif "!giveaway" in str(message):
                if username in cfg.OPLIST:
                    def findWinner():
                        if len(giveaway) == 0:
                            utils.send(s, "The giveaway has ended with no entries.")
                        else:
                            winningNumber = random.randint(0, len(giveaway)) - 1
                            print ("Giveaway list is "+str(giveaway))
                            winningUser = giveaway[winningNumber]
                            utils.send(s, winningUser+", you've won the giveaway! PogChamp Look in your PMs for additional info.")
                            utils.send(s, "/w "+winningUser+" This is an automated message. If you just won a sub giveaway, you should recieve your reward in stream shortly. If you won a card, PM the Octas for your code! Congratulations again!")
                    def openClose():
                        global isOpen
                        isOpen = "Open"
                        sleep(10)
                        isOpen = "Closed"
                        utils.send(s, "The giveaway is closed! You may no longer enter.")
                        sleep(1)
                        utils.send(s, "/me is rolling the dice...")
                        findWinner()
                    def giveawayCom():
                        global giveaway
                        giveaway = []
                        utils.send(s, "A giveaway has just begun! For the next 3 minutes, do !enter to put in your ticket!")
                        t = threading.Thread(target=openClose)
                        t.start()
                    giveawayCom()
                else:
                    utils.send(s, username+", you need to be an admin to perform that action!")
            elif "!enter" in str(message):
                if isOpen == "Open":
                    if username in giveaway:
                        utils.send(s, username+", you've already entered this giveaway!")
                    else:
                        giveaway.append(username)
                else:
                    utils.send(s, "There is no giveaway currently happening!")

            elif "!getdonations" in str(message):
                streamLabsUtils.getDonations()

            elif "!customalert" in str(message):
                if username in cfg.OPLIST:
                    alerttype = arguments[2]
                    message = arguments[3]
                    streamLabsUtils.customAlert(message, alerttype)
                else:
                    utils.send(s, username+", you need to be an admin to perform that command!")

            elif "!createdonation" in str(message):
                if username in cfg.OPLIST:
                    amount = arguments[2]
                    streamLabsUtils.createDonation(username, amount)
                else:
                    utils.send(s, username+", you need to be an admin to perform that command!")

            elif "!testalert" in str(message):
                if username in cfg.OPLIST:
                    alerttype = arguments[2]
                    streamLabsUtils.testAlert(alerttype)
                else:
                    utils.send(s, username+", you need to be an admin to perform that command!")

            elif "!tentacles" in str(message):
                streamLabsUtils.getPoints(username)

            elif "!pet" in str(message):
                if (arguments[2] == "octamouse"):
                    utils.send(s, "Awwww, thanks, "+username)
                else:
                    utils.send(s, "Good boy! "+username+" has pet "+arguments[2])

        sleep(0.3)




if __name__ == "__main__":
    main()
