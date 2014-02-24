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

def sqlncode(argv):
	str_to_ncode = " ".join(argv[1:])
	print "String to encode: =>" + str_to_ncode + "<="
	
	print "MySQL HEX: 0x" + str_to_ncode.encode("hex")
	
	dec_str = list(bytearray(str_to_ncode))
	print "MySQL DEC: CHAR(" + ",".join(str(c) for c in dec_str) + ")"

if __name__ == "__main__":
	if sys.argv[1] == '-h':
		show_help()
	else:
		sqlncode(sys.argv)
