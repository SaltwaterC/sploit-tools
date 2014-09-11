import os, sys

def show_error(msg):
	sys.stderr.write(os.linesep * 2 + "ERROR: " + msg + os.linesep * 3)
	sys.exit(1)

def bare_words():
	string = " ".join(sys.argv[1:])
	print "The used string: =>" + string + "<="
	return string
