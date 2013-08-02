#!/usr/bin/env python

import binascii, sys, re

pattern = re.compile(r"\s+")

with open(sys.argv[1]) as hexfile:
	hexstring = "".join(re.sub(pattern, "", line) for line in hexfile)

binstring = binascii.unhexlify(hexstring)

with open(sys.argv[2], "w") as binfile:
	binfile.write(binstring)
