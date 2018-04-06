#!/usr/bin/env python

'''
1. removed stop words
2. lemmatizing of words
3. combiner implementation for each line
'''

'''
1. for each word in the top10 list, do we find count the
   number of <top10 word, any word that is its neighbor>

2. for each word in the top10 list, do we find count the
   number of <top10 word1, top10 word2> basically top10 words
   being  neighbors of each other?
'''

import sys
import argparse

import nltk
from spacy.lang.en.stop_words import STOP_WORDS
from nltk.stem import WordNetLemmatizer

import re

class Mapper:

	def __init__(self):
		# initializing empty combiner dictionary
		self.combiner = {}

	def cooccurrenceMapper(self, cooccurrenceList):
		# iterate over all the lines in the stdin
		for line in sys.stdin:
			# split line into formatted words
			words = formatInputWords(line)

			# iterate over neighbours
			for word1, word2 in zip(words[:-1], words[1:]):
				if len(word1.strip()) > 0 and len(word2.strip()) > 0:
					# 1 refer above
					# if words of interest are neighbours
					# if word1 in cooccurrenceList and word2 in cooccurrenceList:
					#	key = word1 + '~:::~' + word2 + '_t10'
					#	self.updateCombiner(key)

					# 2 refer above
					# any word is neighbour with word of interest
					if not word1 in STOP_WORDS and not word2 in STOP_WORDS:
						if word1 in cooccurrenceList or word2 in cooccurrenceList:
							key = word1 + ' ' + word2
							self.updateCombiner(key)

	def updateCombiner(self, key, count=1):
		if key in self.combiner:
			self.combiner.update({key:(self.combiner.get(key)+1)})
		else:
			self.combiner.update({key:1})

	def emitWords(self):
		for key, value in self.combiner.items():
			print '%s\t%s' % (key, str(value))

def formatInputWords(line):
	# lemmatizing object
	lemmatizer = WordNetLemmatizer()
	# remove leading and trailing whitespaces
	line = line.strip()
	# split the line into list of words
	words = line.split()
	# convert to ascii encoding
	words = [unicode(word, errors='ignore').encode('ascii') \
			 for word in words]
	# remove leading and trailing symbols from words
	words = [removeLeadingAndTrailingSymbolsFromWord(word) \
			 for word in words]
	# lemmatize words
	words = [(lemmatizer.lemmatize(word)).lower() for word in words]

	return words

def removeLeadingAndTrailingSymbolsFromWord(word):
	# compile a pattern to check if word contains
	# .,!?') at its end'
	symbolPatternAtEnd = re.compile("[\+\=\[_/\@\*\$\&\#\.,!?'\(\)\]\}%\":;><|\-0-9]*$")
	symbolPatternAtStart = re.compile("^[\+\=\[_/\@\*\&\$\#\.,!?'\(\)\]\}%\":;><|\-0-9]*")
	# remove punctuation at the end of the word if any
	s = re.findall(symbolPatternAtEnd, word)[0]
	if len(s) > 0:
		word = word[:-1 * (len(s))]
	# remove punctuation at the start of the word if any
	s = re.findall(symbolPatternAtStart, word)[0]
	if len(s) > 0:
		word = word[len(s):]

	return word

def updateStopWords():
	# adding couple of stop words
	STOP_WORDS.add("i'm")
	STOP_WORDS.add("isn't")
	STOP_WORDS.add("let's")
	STOP_WORDS.add("ha")
	STOP_WORDS.add("according")
	STOP_WORDS.add("want")
	STOP_WORDS.add("like")

if __name__ == '__main__':
	ap = argparse.ArgumentParser()
	ap.add_argument('-f', '--filepath', required=True,
		help='file path of the top ten words')
	args = vars(ap.parse_args())

	with open(args['filepath'], 'r') as f:
		lines = f.readlines()

	cooccurrenceList = [word.strip() for word in lines]
	
	updateStopWords()

	mapper = Mapper()
	mapper.cooccurrenceMapper(cooccurrenceList)
	mapper.emitWords()

'''
hadoop jar /home/hadoop/hadoop/contrib/hadoop-streaming-2.6.0.jar -file cooccurrenceMapper.py -file reducer.py -file top10wordsTwitter.txt -mapper './cooccurrenceMapper.py -f ./top10wordsTwitter.txt' -reducer reducer.py -input tweets_small_data -output tweets_small_data_cooccurrence
'''