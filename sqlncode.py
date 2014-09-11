#!/usr/bin/env python

import sys
import sploit

def show_help():
	print sys.argv[0] + " 'string to be encoded'"
	print sys.argv[0] + " -h => shows this help"
	print
	print "Since -h is reserved for this help, here's the encoded stuff for '-h':"
	print
	print "MySQL HEX: 0x2d68"
	print "MySQL DEC: CHAR(45,104)"
	print
	print "Spared you the trouble for doing things \"the hard way\"."

def sqlncode():
	string = sploit.bare_words()
	
	print "MySQL HEX: 0x" + string.encode("hex")
	
	dec_str = list(bytearray(string))
	print "MySQL DEC: CHAR(" + ",".join(str(c) for c in dec_str) + ")"

if __name__ == "__main__":
	try:
		if sys.argv[1] == "-h":
			show_help()
		else:
			sqlncode()
	except IndexError:
		show_help()
