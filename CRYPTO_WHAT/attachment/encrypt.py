import libnum
from secret import flag
assert len(flag) == 32
bits_length = 256
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

def encrypt(info_list):
	flag_backup = libnum.s2n(flag)
	enc_flag_binlist = []
	for i in range(bits_length):
		info = info_list[i]
		flag_temp = flag_backup
		res = 0
		# this is the first step
		while info != 0:
			temp = info & 1
			info = info >> 1
			res = res << 1
			res += flag_temp & temp
			flag_temp = flag_temp >> 1
		# this is the first step
		# this is not end >:<
		enc_flag = 0
		while res != 0:
			enc_flag += res & 1
			res = res >> 1
		# this is not end >:<
		enc_flag = enc_flag & 1
		# what is this
		enc_flag_binlist.append(enc_flag)
	return binlist_number(enc_flag_binlist)

info_list = generate()
encryption = encrypt(info_list)

#write the result
result = open("encrypt.txt","w")
for x in info_list:
	result.write(hex(x)[2:-1] + "\n")
result.write("\n\n")
result.write(hex(encryption)[2:-1])