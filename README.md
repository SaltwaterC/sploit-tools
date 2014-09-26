# sploit-tools

My own tools for easing the task of pentesting / exploit writing.

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

## sqlncode

Simple MySQL string to HEX and string to CHAR() encoder. Why? Because [online encoders](http://www.waraxe.us/sql-char-encoder.html) take me out of the CLI and I haven't found one by searching the almighy Google. If it takes me less time to actually write a tool than to find it, then something is really wrong with the SERP.

### Example

```bash
# The most basic usage.
The used string: =>/etc/passwd<=
MySQL HEX: 0x2f6574632f706173737764
MySQL DEC: CHAR(47,101,116,99,47,112,97,115,115,119,100)

# The quotes, as expected, are ignored.
./sqlncode.py "/etc/passwd"
The used string: =>/etc/passwd<=
MySQL HEX: 0x2f6574632f706173737764
MySQL DEC: CHAR(47,101,116,99,47,112,97,115,115,119,100)
./sqlncode.py '/etc/passwd'
The used string: =>/etc/passwd<=
MySQL HEX: 0x2f6574632f706173737764
MySQL DEC: CHAR(47,101,116,99,47,112,97,115,115,119,100)

# Yes, it has bare words. Beware of whitespaces at the start / end of the string!
./sqlncode.py this tool supports bare words when you don\'t need whitespaces at the start or at the end of the string
The used string: =>this tool supports bare words when you don't need whitespaces at the start or at the end of the string<=
MySQL HEX: 0x7468697320746f6f6c20737570706f727473206261726520776f726473207768656e20796f7520646f6e2774206e65656420776869746573706163657320617420746865207374617274206f722061742074686520656e64206f662074686520737472696e67
MySQL DEC: CHAR(116,104,105,115,32,116,111,111,108,32,115,117,112,112,111,114,116,115,32,98,97,114,101,32,119,111,114,100,115,32,119,104,101,110,32,121,111,117,32,100,111,110,39,116,32,110,101,101,100,32,119,104,105,116,101,115,112,97,99,101,115,32,97,116,32,116,104,101,32,115,116,97,114,116,32,111,114,32,97,116,32,116,104,101,32,101,110,100,32,111,102,32,116,104,101,32,115,116,114,105,110,103)
```

## wep

Uses an input string to generated WEP keys by using the so called "[de facto standard](http://stackoverflow.com/questions/2890438/how-can-i-generate-40-64-bit-wep-key-in-python)". This algorihm is used by various router vendors to generate the WEP keys by using a password. Examples: Linksys, Netgear, Belkin, DLink.

The code was ported from a pure JavaScript implementation. A node.js version is also available. A convenience wrapper written in bash is also available. It tries to run the Python implementation. If python isn't in $PATH, it falls back to node. If node isn't in $PATH, it presents an error message.

The reason why this script exists is the fact that my WiFi lab uses a Netgear router. Pentesting WiFi has the bad habbit of leaving me without Internet connection. Hence, a generator that runs on my machine is often required instead of using an online generator. A Perl implementation is available on [WiGLE.net](https://wigle.net/jigle/wep.pl).

### Example

```bash
# The Python version
/wep.py foobar
The used string: =>foobar<=
WEP 40 key1: A4BEB3B8EC
WEP 40 key2: B697E900C8
WEP 40 key3: B5D2BB755B
WEP 40 key4: 197EA2ABE7
WEP 104 key: 49D68437B1FFB0DB3FDF2D4A93

./wep.py foo bar
The used string: =>foo bar<=
WEP 40 key1: 94CE6E1345
WEP 40 key2: 3DE0C45DB6
WEP 40 key3: 6F69BDE821
WEP 40 key4: BCC9F992B9
WEP 104 key: 5F8FDCB2090ACEB521077F4BC3

# The node.js version
./wep.js foobar
The used string: =>foobar<=
WEP 40 key1: A4BEB3B8EC
WEP 40 key2: B697E900C8
WEP 40 key3: B5D2BB755B
WEP 40 key4: 197EA2ABE7
WEP 104 key: 49D68437B1FFB0DB3FDF2D4A93

./wep.js foo bar
The used string: =>foo bar<=
WEP 40 key1: 94CE6E1345
WEP 40 key2: 3DE0C45DB6
WEP 40 key3: 6F69BDE821
WEP 40 key4: BCC9F992B9
WEP 104 key: 5F8FDCB2090ACEB521077F4BC3
```

The same bare words support from sqlncode was implemented here. The above examples apply.

## shellshock

Easily test the system for the presence of CVE-2014-6271 and CVE-2014-7169 - also known as [Shellshock](http://en.wikipedia.org/wiki/Shellshock_%28software_bug%29). The script iterates all the $PATH directories, looking for bash and sh. Some systems, like OS X, also use bash for sh.

If the word *VULNERABLE* is in the output, then the shell isn't patched. I am doing Captain Obvious here. Yes, it's **THAT** serious.

For OS X, [a pull request](https://github.com/Homebrew/homebrew/pull/32671) for CVE-2014-7169 is pending for Homebrew, while the system provided bash/sh needs to be [manually patched](http://apple.stackexchange.com/a/146851).

### Example

```bash
# on a patched system it doesn't show anything
./shellshock.sh
Testing /bin/sh for CVE-2014-6271
Testing /bin/sh for CVE-2014-7169

Testing /bin/bash for CVE-2014-6271
Testing /bin/bash for CVE-2014-7169

# on a vulnerable OS X
./shellshock.sh
Testing /usr/local/bin/bash for CVE-2014-6271
Testing /usr/local/bin/bash for CVE-2014-7169
VULNERABLE

Testing /bin/sh for CVE-2014-6271
VULNERABLE
Testing /bin/sh for CVE-2014-7169
VULNERABLE

Testing /bin/bash for CVE-2014-6271
VULNERABLE
Testing /bin/bash for CVE-2014-7169
VULNERABLE
```
