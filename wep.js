#!/usr/bin/env node

var p = require('path');
var crypto = require('crypto');

var showHelp = function () {
	console.log('./' + p.basename(process.argv[1]) + ' \'string to convert to four WEP 40 keys and a WEP 104 key\'');
	console.log('./' + p.basename(process.argv[1]) + ' -h => shows this help');
}

function binToHex(chr) {
	return ('0' + chr.toString(16)).substr(-2).toUpperCase();
}

var wep40 = function (str) {
	var pseed = [0, 0, 0, 0];
	var k64 = ['', '', '', ''];
	var i, j, tmp;
	
	for (i = 0; i < str.length; i++) {
		pseed[i%4] ^= str.charCodeAt(i);
	}
	
	randNumber = pseed[0] | (pseed[1] << 8) | (pseed[2] << 16) | (pseed[3] << 24);
	
	for (i = 0; i < 4; i++) {
		for (j = 0; j < 5; j++) {
			randNumber = (randNumber * 0x343fd + 0x269ec3) & 0xffffffff;
			tmp = (randNumber >> 16) & 0xff;
			k64[i] += binToHex(tmp);
		}
		
		console.log('WEP 40 key%d: %s', i + 1, k64[i]);
	}
}

var padTo64 = function (str) {
	var i, n, ret = '';
	
	n = 1 + (64 / (str.length));
	
	for (i = 0; i < n; i++)
	{
		ret += str;
	}
	
	return ret.substring(0, 64);
}

var wep104 = function (str) {
	str = padTo64(str);
	var ret = crypto.createHash('md5').update(str).digest('hex').toUpperCase();
	
	console.log('WEP 104 key: %s', ret.substring(0, 26));
}

var wepKeys = function () {
	str = process.argv.slice(2).join(' ');
	console.log('The used string: =>%s<=', str);
	
	wep40(str);
	wep104(str);
}

if (process.argv[2] === '-h' || process.argv.length === 2) {
	showHelp();
} else {
	wepKeys();
}
