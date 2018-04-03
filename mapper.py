#!/usr/bin/env python

'''
1. removed stop words
2. stemming of words
3. combiner implementation for each line
'''

import sys

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import re

# list of stop words
stopwordsList = stopwords.words('english')

# object of stemmer class
ps = PorterStemmer()

# compile a pattern to check if word contains
# .,!?') at its end'
symbolPatternAtEnd = re.compile("[\.,!?'\)\]\}%\":;><|-]*$")
symbolPatternAtStart = re.compile("[\.,!?'\)\]\}%\":;><|-]*$")

# combiner dictionary
# structure to imitate associative array
combiner = {}

# iterate over all the lines in the stdin
for line in sys.stdin:

	# remove leading and trailing whitespaces
	line = line.strip()

	# split the line into list of words
	words = line.split()

	for word in words:

		# remove punctuation at the end of the word if any
		s = re.findall(symbolPatternAtEnd, word)[0]
		if len(s) > 0:
			word = word[:-1 * (len(s))]

		# remove punctuation at the start of the word if any
		s = re.findall(symbolPatternAtStart, word)[0]
		if len(s) > 0:
			word = word[len(s):]

		# if the word is not in stop words list
		if not word in stopwordsList and not word[:5] == 'https':
			# stem the word
			stemmedWord = ps.stem(word)

			# add word to combiner dictionary
			# if word is already present in dictionary
			# then increment the count
			if stemmedWord in combiner:
				count = combiner.get(stemmedWord) + 1
				combiner.update({stemmedWord:count})
			# if word is not present in dictionary then
			# add the word with count 1
			else:
				combiner.update({stemmedWord:1})
		
# emit word counts from combiner
for word in combiner.keys():
	print('%s\t%s' % (word, str(combiner.get(word))))