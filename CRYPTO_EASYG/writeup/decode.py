import string
import random
import base64
from secret import flag

chars = string.printable[:64]
BLOCK_SIZE = len(flag)
res = ""

def xor(a,b):
	res = ""
	assert len(a) == len(b)
	for i in range(len(a)):
		res += chr(ord(a[i])^ord(b[i]))
	return res

f = open("give_to_player","r")
info = f.readline().strip("\n")
dec = info.split(":")[0]
enc = info.split(":")[1]
key = xor(dec,base64.b64decode(enc))
f.readline()
f.readline()
f.readline()
flag = f.readline().strip("\n")
flag = xor(key,base64.b64decode(flag))
print flag