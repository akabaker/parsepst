#!/usr/bin/env python

import re
import subprocess
import operator
infile = '/home/bakerlu/pst_output/2011'
words = ['no', 'can\'t', 'unable', 'sorry', 'apologies']
regex = re.compile(r'%s' % '|'.join(words))

def parse(file):
	with open(file, 'r') as f:
		out = f.read()

	match = regex.findall(out)
	matches = {}
	for word in words:
		#print '%s,%d' % (word,match.count(word))
		matches[word] = match.count(word)
	

def classify(result_list):
	largest = 50
	large = 35
	medium = 25
	small = 10

	#Sort the list of tuples by the second key in the tuple, (numeric value)
	sorted_words = sorted(result_list, key=operator.itemgetter(1))
	sorted_words_len = len(sorted_words)

	#for i in xrange(sorted_words_len):
	#	print sorted_words.pop()
	largest_word, largest_value = sorted_words[-1:][0]

if __name__ == '__main__':
	#parse(infile)
	words_n_counts = [('apologies',32), ('sorry', 74), ('unable', 181), ("can't", 107), ('no', 39884)]
	classify(words_n_counts)
