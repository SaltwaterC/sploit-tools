# sploit-tools

My own tools for easing the task of exploit writing.

## pattern

A simple Python script for replicating the functionality of pattern_create.rb and pattern_offset.rb tools of the Metasploit Framework. Useful for exploit writers than only have a python binary around. About 25 times faster than the MSF implementation which is as slow as molasses.

Simply invoke the script without arguments or junk arguments in order to get the help.

### Examples

```bash
# create a 128 bytes buffer
./pattern.py create 128
Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae

Created a buffer of 128 bytes

# find the string offset
./pattern.py offset Ab0A
Pattern found at position: 30

# WARNING: valid hex values are not decoded if they are part of the ACTUAL buffer
# the hex decoding is a fallback measure for the input
./pattern.py offset Ab0Ab1
Pattern found at position: 30

# decode a hex value to a string offset
./pattern.py offset 41306241
hex pattern decoded as: Ab0A
Pattern found at position: 30

# decode another representation of the hex value to a string offset
# use this representation of a hex value in order to force the decoding
./pattern.py offset 0x41306241
hex pattern decoded as: Ab0A
Pattern found at position: 30

# find multiple offsets for patterns exceeding 20280 bytes
# 20280 bytes is the maximum unique bytes for the Aa0 pattern
./pattern.py offset Aa0 30000
0
20280
```

## hextobin

Converts a hex string from an input file to a binary string that's written to an output file. Strips all the whitespace found into the input file.

Notice: this script does a different job than [hex2bin.py](http://www.bialix.com/intelhex/manual/part3-1.html) of the [intelhex library](http://www.bialix.com/intelhex/manual/part1-1.html), hence the name is different.

### Examples

```bash
# with input file and output file
cat input.hex
48 65 6c 6c
6f20576f726


c64
./hextobin.py input.hex output.bin
cat output.bin
Hello World

# with input from STDIN
cat input.hex | ./hextobin.py - output.bin

# with output to STDOUT
./hextobin.py intput.hex -
Hello World

# with input from STDIN and output to STDOUT
cat input.hex | ./hextobin.py - -
Hello World
```

## orjohn

Helper script for formatting a USER$ CSV dump to a file that John the Ripper understands. This scripts expects the hashes used by Oracle up to 11g, including 11g. Doesn't work with the new hashing scheme that 11g Release 1 supports. [References](http://marcel.vandewaters.nl/oracle/security/password-hashes) about how Oracle hashes the passwords.

### Example

```bash
cat oracle.csv
"0","SYS","1","4DE42795E66117AE","0","2","12-May-2002 04:18:08 PM","15-Jan-2007 07:43:33 AM","","","0","","1","","","0","0","SYS_GROUP","","","","","","",""
"1","SYSTEM","1","970BAA5B81930A40","0","2","12-May-2002 04:18:08 PM","15-Jan-2007 07:43:33 AM","","","0","","1","","","0","0","SYS_GROUP","","","","","","",""
"2","WMSYS","1","7C9BA362F8314299","0","2","12-May-2002 04:44:32 PM","12-May-2002 04:44:32 PM","15-Jan-2007 07:42:31 AM","15-Jan-2007 07:42:31 AM","0","","1","","","9","0","DEFAULT_CONSUMER_GROUP","","","","","","",""

./orjohn.py oracle.csv
sys:0$SYS#4DE42795E66117AE
system:0$SYSTEM#970BAA5B81930A40
wmsys:0$WMSYS#7C9BA362F8314299

./orjohn.py oracle.csv > oracle.txt

john --format:oracle oracle.txt
Loaded 3 password hashes with 3 different salts (Oracle 10 DES [32/64])
SYSTEM           (system)
SYS              (sys)
WMSYS            (wmsys)
guesses: 3  time: 0:00:00:00 DONE (Tue Aug 20 17:46:21 2013)  c/s: 300  trying:
Use the "--show" option to display all of the cracked passwords reliably

john --format:oracle oracle.txt --show
sys:SYS
system:SYSTEM
wmsys:WMSYS

3 password hashes cracked, 0 left
```
