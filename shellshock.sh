#!/bin/bash

bold=$(tput bold)
normal=$(tput sgr0)

function cve_2014_6271
{
	echo "${bold}Testing $1 for CVE-2014-6271${normal}"
	env x="() { :;}; echo VULNERABLE" $1 -c "" 2>/dev/null
}

function cve_2014_7169
{
	echo "${bold}Testing $1 for CVE-2014-7169${normal}"
	rm -f echo
	env x='() { (a)=>\' $1 -c "echo echo VULNERABLE" >/dev/null 2>&1
	cat echo 2>/dev/null
	rm -f echo
}

for path in ${PATH//:/ }
do
	if [ -f "$path/sh" ]
	then
		cve_2014_6271 "$path/sh"
		cve_2014_7169 "$path/sh"
		echo
	fi
	if [ -f "$path/bash" ]
	then
		cve_2014_6271 "$path/bash"
		cve_2014_7169 "$path/bash"
		echo
	fi
done
