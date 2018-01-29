
import cfg
import utils
from time import sleep
import random, subprocess, os, threading, re, socket, time
import streamLabsUtils


def main():
    s = socket.socket()
    s.connect(("sockets.streamlabs.com", 25))
    s.send("TOKEN {}\r\n".format(cfg.SOCKETTOKEN).encode("utf-8"))
    while True:
        response = s.recv(1024).decode("utf-8")
        print (response)
        f = open('socketLog.txt','a')
        f.write(response)
        f.close()

if __name__ == "__main__":
    main()
