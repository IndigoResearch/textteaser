import nltk.data

class Parser:
  def __init__(self):
    self.ideal = 20.0

  def getSentenceLengthScore(self, sentence):
    wordList = self.splitWords(sentence)

    return (self.ideal - abs(self.ideal - len(wordList))) / self.ideal

  def splitSentences(self, text):
    tokenizer = nltk.data.load('file:trainer/english.pickle')

    return tokenizer.tokenize(text)

  def splitWords(self, sentence):
    return sentence.lower().split()
