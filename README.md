# pattern

A simple Python script for replicating the functionality of pattern_create.rb and pattern_offset.rb tools of the Metasploit Framework. Useful for exploit writers than only have a python binary around.

The implementation is limited to 20280 bytes buffers which is the maximum length for a unique string of the Aa0 pattern. In practice, I didn't need more, but at the same time I barely scratched the subject of exploit writing.

Simply invoke the script without arguments or junk arguments in order to get the help.
