#!/usr/bin/env python
import re
from sys import exit

infile = '/home/bakerlu/pst_output/2011'
words = ['can\'t', 'unable', 'sorry', 'apologies', 'AIR', 'failure']
regex = re.compile(r'%s' % '|'.join(words))

def parse(file):
	with open(file, 'r') as f:
		out = f.read()

	match = regex.findall(out)
	matches = {}
	for word in words:
		matches[word] = match.count(word)

	if sum(matches.values()) == 0:
		raise ValueError('Result set is empty')
	else:
		return matches

def classify(result_dict):
	#CSS font sizes
	font_sizes = [10,20,30]
	max_num = max(result_dict.values())
	#Interval
	step = max_num / len(range(0,2))

	for word, count in result_dict.items():
		font_size_index = count / step
		print '<p style="font-size:%dpx">%s - %d</p>' % (font_sizes[font_size_index], word, count)
		#print '<p style="font-size:%dpx">%s</p>' % (font_sizes[font_size_index], word)
	
if __name__ == '__main__':
	try:
		matches = parse(infile)
	except ValueError, error:
		print error
		exit(1)

	classify(matches)
