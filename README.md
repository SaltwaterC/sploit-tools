# pattern

A simple Python script for replicating the functionality of pattern_create.rb and pattern_offset.rb tools of the Metasploit Framework. Useful for exploit writers than only have a python binary around.

The implementation is limited to 20280 bytes buffers which is the maximum length for a unique string of the Aa0 pattern. In practice, I didn't need more, but at the same time I barely scratched the subject of exploit writing.

Simply invoke the script without arguments or junk arguments in order to get the help.

## Examples

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
```
