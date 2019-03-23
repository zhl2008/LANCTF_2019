import libnum
import numpy
#flag = "flag{Do_You_Know_Hill_Is_Secret}"
#assert len(flag) == 32
bits_length = 256
def decode():
	nump = [[] for i in range(bits_length)]
	with open("encrypt.txt","r") as f:
		for i in range(bits_length):
			info = f.readline().strip("\n")
			nump[i] = get_binlist(int(info, 16))
			"""
			for j in range(bits_length):
				nump[j].append(get_binlist(int(info, 16))[j])"""
		f.readline()
		f.readline()
		info = f.readline().strip("\n")
		for i in range(bits_length):
			nump[i].append(get_binlist(int(info,16))[i])
	for i in range(bits_length):
		if nump[i][i] != 1:
			for _ in range(i+1,bits_length,1):
				if nump[_][i] == 1:
					temp = nump[_]
					nump[_] = nump[i]
					nump[i] = temp
		for j in range(i+1,bits_length,1):
			if nump[j][i] == 1:
				for k in range(0,bits_length+1,1):
					nump[j][k] = nump[i][k] ^ nump[j][k]
	for i in range(bits_length-1,-1,-1):
		for j in range(i-1,-1,-1):
			if nump[j][i] == 1:
				for k in range(0,bits_length+1,1):
					nump[j][k] = nump[i][k] ^ nump[j][k]
	res = []
	for i in range(bits_length):
		res.append(nump[i][bits_length])
	info = binlist_number(res)
	assert nump[255][255] != 0
	return libnum.n2s(info)

def generate():
	info_list = []
	for i in range(bits_length):
		temp = libnum.randint_bits(bits_length)
		info_list.append(temp)
	return info_list

def get_binlist(x):
	res = []
	info = bin(x)[2:].strip("L").rjust(bits_length,"0")
	for i in range(len(info)):
		if info[i] == "0":
			res.append(0)
		else:
			res.append(1)
	return res

def binlist_number(l):
	res = ""
	for x in l:
		res += str(x)
	return int(res,2)

print decode()