#!/usr/bin/env python

import sys, binascii, md5
import sploit

def show_help():
	print sys.argv[0] + " 'string to convert to four WEP 40 keys and a WEP 104 key'"
	print sys.argv[0] + " -h => shows this help"

def wep_40(string):
	pseed = [0, 0, 0, 0]
	k64 = ["", "", "", ""]
	
	for i in range(0, len(string)):
		pseed[i%4] ^= ord(string[i])
	
	rand_number = pseed[0] | (pseed[1] << 8) | (pseed[2] << 16) | (pseed[3] << 24)
	
	for i in range(0, 4):
		for j in range(0, 5):
			rand_number = (rand_number * 0x343fd + 0x269ec3) & 0xffffffff;
			tmp = (rand_number >> 16) & 0xff;
			k64[i] += binascii.hexlify(chr(tmp)).upper()
		
		print "WEP 40 key" + str(i + 1) + ": " + k64[i]

def pad_to_64(string):
	ret = ""
	rep = 1 + (64 / len(string))
	
	for n in range(0, rep):
		ret += string
	
	return ret[:64]

def wep_104(string):
	string = pad_to_64(string)
	ret = md5.new(string).hexdigest()
	ret = ret.upper()
	
	print "WEP 104 key: " + ret[:26]

def wep_keys():
	string = sploit.bare_words()
	
	wep_40(string)
	wep_104(string)

if __name__ == "__main__":
	try:
		if sys.argv[1] == "-h":
			show_help()
		else:
			wep_keys()
	except IndexError:
		show_help()
