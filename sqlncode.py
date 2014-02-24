#!/usr/bin/env python

import sys

str_to_ncode = " ".join(sys.argv[1:])
print "String to encode: =>" + str_to_ncode + "<="

print "MySQL HEX: 0x" + str_to_ncode.encode("hex")

dec_str = list(bytearray(str_to_ncode))
print "MySQL DEC: CHAR(" + ",".join(str(c) for c in dec_str) + ")"
