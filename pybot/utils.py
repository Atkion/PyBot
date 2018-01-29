import time
import cfg
from time import sleep
import urllib, json

def send(sock, msg):
    sock.send("PRIVMSG #{} :{} \r\n".format(cfg.CHAN, msg).encode("utf-8"))

def ban(sock, user):
    chat(sock, ".ban {}".format(user))

def timeout(sock, user, seconds=600):
    chat(sock, ".timeout {}".format(user, seconds))

"""def threadFillOpList():
    while True:
        try:
            url = "http://tmi.twitch.tv/group/user/octamouselabs/chatters"
            req = urllib.Request(url, headers={"accept": "*/*"})
            response = urllib.urlopen(req).read()
            if response.find("502 Bad Gateway") == -1:
                cfg.OPLIST.clear()
                data = json.loads(response)
                for p in data["chatters"]["moderators"]:
                    cfg.oplist[p] = "mod"
                for p in data["chatters"]["global_mods"]:
                    cfg.oplist[p] = "global_mod"
                for p in data["chatters"]["admin"]:
                    cfg.oplist[p] = "admin"
                for p in data["chatters"]["staff"]:
                    cfg.oplist[p] = "staff"
        except:
            'do nothing'
        sleep(5)"""
