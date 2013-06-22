#!/usr/bin/env python
# -*- coding: utf-8 -*-

import text_munger as tm
import os.path

class WordBase():
	'Saves and fetches words from a file'

	def __init__(self, filename):
		self.filename = filename
		self.words = self.loadBaseFromFile()

	def hasWord(self, word):
		'Checks if a clean version of the word exists in WordBase'
		return tm.clean_word(word) in self.words

	def addWord(self, word):
		'Adds a clean version of the word to the WordBase'
		self.words.add(tm.clean_word(word))

	def saveWordsFromText(self, text):
		'Saves clean versions of the words in the text to the WordBase'
		new_words = set(tm.extract_words(text))
		for w in new_words:
			self.addWord(w)
		self.saveBaseToFile()
		return new_words

	def saveBaseToFile(self):
		'Saves the words currently in memory to the WordBase file'
		with open(self.filename,'a') as f:
			for w in self.words:
				f.write('%s\n' % w)

	def loadBaseFromFile(self):
		'Loads words from the WordBase file into memory'
		if not os.path.isfile(self.filename):
			return set([])
		with open(self.filename,'r') as f:
			res = []
			for line in f:
				res.append(line.strip())
		return set(res)

	def getNumberOfWords(self):
		'Returns the number of words in memory'
		return len(self.words)