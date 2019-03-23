from pwn import *

#io = process("./avoid_crash")
#io = remote("127.0.0.1", 1234)
io = remote("10.139.0.73", 1234)


p = process("./test")

for i in range(10):
    s = p.recvline()
    io.sendafter("The rocky limit is: ", s)

print io.recvline()
io.interactive()
