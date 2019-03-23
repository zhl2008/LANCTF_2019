from pwn import *
import base64
import libnum

BLOCK_SIZE = 32
p = remote("127.0.0.1",1341)

def xor(number):
    p.sendafter("you can choose what you want here\n","xor")
    p.sendafter("send how long the number you want to xor\n",str(len(str(number))).rjust(4,"0"))
    p.sendafter("send the number you want to xor\n",str(number))
    return p.recvline()

def add(number):
    p.sendafter("you can choose what you want here\n","add")
    p.sendafter("send how long the number you want to add\n",str(len(str(number))).rjust(4,"0"))
    p.sendafter("send the number you want to add\n",str(number))
    return p.recvline()

def guess_key(key):
    p.sendafter("you can choose what you want here\n","ppp")
    p.recvuntil("you got a magic\n")
    p.send(key)
    info = p.recvline()
    if info == "OH!How do you get it\n":
        return p.recv()
    else:
        return False

def xor_add_oracle():
    known = ""
    for i in range(BLOCK_SIZE*8 - 1):
        xor_res = xor(1<<i)
        add_res = add(1<<i)
        if xor_res == add_res:
            known = "0" + known
        else:
            known = "1" + known
    key = "1" + known
    info = guess_key(libnum.n2s(int(key,2)))
    if info != False:
        return info
    else:
        key = "0" + known
        return guess_key(libnum.n2s(int(key,2)))

flag = xor_add_oracle()
print flag
p.close()
