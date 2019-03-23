#!/usr/bin/env python2
import SocketServer
import socket
import base64
import os
from Crypto.Cipher import AES  
from secret import FLAG
import libnum

BLOCK_SIZE = 32
mask = int("FF"*BLOCK_SIZE,16)
def generate():
    KEY = os.urandom(BLOCK_SIZE)
    return KEY

def add(KEY,number,dec):
    key = libnum.s2n(KEY)
    key = (key + number) & mask
    KEY = libnum.n2s(key).rjust(BLOCK_SIZE,"\x00")
    dec = dec + (BLOCK_SIZE - len(dec)%BLOCK_SIZE)*"\x00"
    assert len(dec)%BLOCK_SIZE == 0
    AES_ECB = AES.new(KEY, AES.MODE_ECB)
    return AES_ECB.encrypt(dec)

def xor(KEY,number,dec):
    key = libnum.s2n(KEY)
    key = (key ^ number) & mask
    KEY = libnum.n2s(key).rjust(BLOCK_SIZE,"\x00")
    dec = dec + (BLOCK_SIZE - len(dec)%BLOCK_SIZE)*"\x00"
    assert len(dec)%BLOCK_SIZE == 0
    AES_ECB = AES.new(KEY, AES.MODE_ECB)
    return AES_ECB.encrypt(dec)

def recv_exact(s, length):
    buf = ''
    while length > 0:
        data = s.recv(length)
        if data == '':
            raise EOFError()
        buf += data
        length -= len(data)
    return buf

def recv_int(s):
    size = recv_exact(s, 4)
    size = int(size)
    return size

def main(s):
    try:
        KEY = generate()
        try_times = 2
        s.sendall("Welcome to Lanctf !!!\n")
        s.sendall("There is some magic in the Math world !!!\n")
        while True:
            s.sendall("you can choose what you want here\n")
            a = s.recv(3)
            if a == "xor":
                s.sendall("send how long the number you want to xor\n")
                size = recv_int(s)
                s.sendall("send the number you want to xor\n")
                m = recv_exact(s, size)
                number = int(m)
                dec = "Lancet is a excellent world, don't you think so??"
                res = xor(KEY,number,m)
                s.send("res:{res}\n".format(res=res.encode("hex")))
            elif a == "add":
                s.sendall("send how long the number you want to add\n")
                size = recv_int(s)
                s.sendall("send the number you want to add\n")
                m = recv_exact(s, size)
                number = int(m)
                res = add(KEY,number,m)
                s.send("res:{res}\n".format(res=res.encode("hex")))
            elif a == "ppp":
                if try_times <= 0:
                    break
                s.sendall("you got a magic\n")
                m = recv_exact(s, BLOCK_SIZE)
                if str(m) == KEY:
                    s.sendall("OH!How do you get it\n")
                    s.sendall(FLAG)
                    break
                else:
                    s.sendall("math math math\n")
            else:
                s.sendall("there is no magic\n")
        s.close()
    except Exception,e:
        print str(e)
        s.close()
        pass

class TaskHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        main(self.request)

if __name__ == '__main__':
    SocketServer.ThreadingTCPServer.allow_reuse_address = True
    server = SocketServer.ThreadingTCPServer(('0.0.0.0', 1341), TaskHandler)
    server.serve_forever()
