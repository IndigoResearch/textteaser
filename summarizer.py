from parser import Parser

class Summarizer:
  def __init__(self):
    self.parser = Parser()

  def summarize(self, text, title, source, category):
    sentences = self.parser.splitSentences(text)
    titleWords = self.parser.removePunctations(title)
    titleWords = self.parser.splitWords(title)
    (keywords, wordCount) = self.parser.getKeywords(text)

    topKeywords = self.getTopKeywords(keywords[:10], wordCount, source, category)

    result = self.computeScore(sentences, titleWords, topKeywords)

  def getTopKeywords(self, keywords, wordCount, source, category):
    # Add getting top keywords in the database here
    return keywords

  def computeScore(self, sentences, titleWords, topKeywords):
    None

  def sbs(sentence, topKeywords):
    None

  def dbs(sentence, topKeywords):
    None