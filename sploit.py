import os, sys

def show_error(msg):
        sys.stderr.write(os.linesep * 2 + "ERROR: " + msg + os.linesep * 3)
        sys.exit(1)
