import text_munger as tm

class WordBase():
	'Saves and fetches words to a file'

	def __init__(self, filename):
		self.filename = filename
		self.words = self.loadBaseFromFile()

	def hasWord(self, word):
		return tm.clean_word(word) in self.words

	def addWord(self, word):
		self.words.add(tm.clean_word(word))

	def saveWordsFromText(self, text):
		new_words = set(tm.extract_words(text))
		for w in new_words:
			self.addWord(w)
		self.saveBaseToFile()
		return new_words

	def saveBaseToFile(self):
		with open(self.filename,'a') as f:
			for w in self.words:
				f.write('%s\n' % w)

	def loadBaseFromFile(self):
		with open(self.filename,'r') as f:
			res = []
			for line in f:
				res.append(line.strip())
		return set(res)

	def getNumberOfWords(self):
		return len(self.words)