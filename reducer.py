#!/usr/bin/env python

from operator import itemgetter
import sys

def singleWordCountReducer():
	current_word = None
	current_count = 0
	word = None

	while True:
	#for line in sys.stdin:
		line = sys.stdin.readline()
		if not line:
			break

		f = open('/home/hadoop/Desktop/lab2/wordcoount/reduceInput.txt', 'wa')
		f.write(line+'\n')
		f.close()

		line = line.strip()

		word, count = line.split('\t')

		try:
			count = int(count)
		except ValueError:
			continue

		if current_word == word:
			current_count += count
		else:
			if current_word:
				# emit only if count exceeds 5
				# this filters alot of words with count just 1
				if current_count > 5:
					print('%s\t%s' % (current_word, current_count))

			current_count = count
			current_word = word

	if current_word == word:
		# emit only if count exceeds 5
		# this filters alot of words with count just 1
		if current_count > 5:
			print('%s\t%s' % (current_word, current_count))

if __name__ == '__main__':
	singleWordCountReducer()