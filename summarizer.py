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
    for keyword in keywords:
      articleScore = 1.0 * keyword['count'] / wordCount
      keyword['totalScore'] = articleScore * 1.5

    return keywords

  def computeScore(self, sentences, titleWords, topKeywords):
    keywordList = [keyword['word'] for keyword in topKeywords]

    for sentence in sentences:
      sentence = self.parser.removePunctations(sentence)
      words = self.parser.splitWords(sentence)

      sbsFeature = self.sbs(words, topKeywords, keywordList)
      dbsFeature = self.dbs(words, topKeywords, keywordList)

      print 'sbs: %f' % sbsFeature
      print 'dbs: %f' % dbsFeature

  def sbs(self, words, topKeywords, keywordList):
    score = 0.0

    if len(words) == 0:
      return 0

    for word in words:
      word = word.lower()
      index = -1

      if word in keywordList:
        index = keywordList.index(word)

      if index > -1:
        score += topKeywords[index]['totalScore']

    return 1.0 / abs(len(words)) * score

  def dbs(self, words, topKeywords, keywordList):
    k = len(list(set(words) & set(keywordList))) + 1
    summ = 0.0
    firstWord = {}
    secondWord = {}

    for i, word in enumerate(words):
      if word in keywordList:
        index = keywordList.index(word)

        if firstWord == {}:
          firstWord = {'i': i, 'score': topKeywords[index]['totalScore']}
        else:
          secondWord = firstWord
          firstWord = {'i': i, 'score': topKeywords[index]['totalScore']}
          distance = firstWord['i'] - secondWord['i']

          summ += (firstWord['score'] * secondWord['score']) / (distance ** 2)


    return (1.0 / k * (k + 1.0)) * summ