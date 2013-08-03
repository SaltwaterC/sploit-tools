# sploit-tools

My own tools for easing the task of exploit writing.

## pattern

A simple Python script for replicating the functionality of pattern_create.rb and pattern_offset.rb tools of the Metasploit Framework. Useful for exploit writers than only have a python binary around.

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

TODO: help, error reporting.

Notice: this script does a different job than [bin2hex.py](http://www.bialix.com/intelhex/manual/part3-1.html) of the [intelhex library](http://www.bialix.com/intelhex/manual/part1-1.html), hence the name is different.

### Example

```bash
cat input.hex
48 65 6c 6c
6f20576f726


c64
./hextobin.py input.hex input.bin
cat input.bin
Hello World
```
