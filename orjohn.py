#!/usr/bin/env python

import sys, csv
import sploit

def show_help():
	print sys.argv[0] + " input.csv"
	print "\tinput.csv - the USER$ table dump as CSV by using tools like SQL Scratchpad"

def orjohn():
	try:
		with open(sys.argv[1], 'rb') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='"')
			try:
				for row in reader:
					if len(str(row[3])) == 16:
						print str(row[1]).lower() + ":0$" + row[1] + "#" + row[3]
			except IndexError:
				sploit.show_error("The input file must be a valid CSV file that uses , as delimiter and \" as quote char.")
	except IOError:
		sploit.show_error("You need to specify an input CSV file.")

if __name__ == "__main__":
	if len(sys.argv) != 2:
		show_help()
	else:
		orjohn()
