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
    keywordList = [keyword['word'] for keyword in topKeywords]

    for sentence in sentences:
      sbsFeature = self.sbs(sentence, topKeywords, keywordList)

      print sbsFeature

  def sbs(self, sentence, topKeywords, keywordList):
    sentence = self.parser.removePunctations(sentence)
    words = self.parser.splitWords(sentence)
    score = 0.0

    if len(words) == 0:
      return 0

    for word in words:
      word = word.lower()
      index = -1

      if word in keywordList:
        index = keywordList.index(word)

      if index > -1:
        score += topKeywords[index]['count']

    return 1.0 / abs(len(words)) * score

  def dbs(self, sentence, topKeywords):
    None