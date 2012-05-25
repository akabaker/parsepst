#!/usr/bin/env python

import re
import subprocess
infile = 'pst_output/2011'
words = ['no', 'can\'t', 'unable', 'sorry', 'apologies']
regex = re.compile(r'%s' % '|'.join(words))

def parse(file):
	with open(file, 'r') as f:
		out = f.read()

	match = regex.findall(out)
	for word in words:
		print '%s,%d' % (word,match.count(word))

if __name__ == '__main__':
	parse(infile)

#read_pst('/home/bakerlu/2011.pst', '/home/bakerlu/pst_out2')
#def read_pst(pstfile, outdir):
#	subprocess.Popen('readpst %s -o %s' % (pstfile, outdir), shell=True, stdout=subprocess.PIPE).communicate()	
