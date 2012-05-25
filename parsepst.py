#!/usr/bin/env python
import re
import json
from sys import exit

infile = '/home/bakerlu/pst_output/2011'

def load(file):
	"""Load json words file"""
	with open(file, 'r') as f:
		return json.loads(f.read())

words = load('words.json')
regex = re.compile(r'%s' % '|'.join(words))

def parse(file):
	"""
	Opens pst file
	Looks for matches against the compiled regex (words list)
		-Example, r'failure|mistake|problem'
	
	@param file Word list
	@return matches Dictionary of <word match>:<count>
	"""

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

def classify(matches):
	"""
	Select one of three font sizes to represent word occurance in the PST file.
	Output is HTML

	@param result_dict Dictionary of word matches
	"""
	#CSS font sizes
	font_sizes = [10,20,30]
	max_num = max(matches.values())

	#Interval
	step = max_num / len(range(0,2))

	for word, count in matches.items():
		font_size_index = count / step
		print '<p style="font-size:%dpx">%s - %d</p>' % (font_sizes[font_size_index], word, count)
	
if __name__ == '__main__':
	try:
		matches = parse(infile)
	except ValueError, error:
		print error
		exit(1)

	classify(matches)
