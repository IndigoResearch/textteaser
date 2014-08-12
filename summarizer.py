from parser import Parser

class Summarizer:
  def __init__(self):
    self.parser = Parser()

  def summarize(self, text, title, source, category):
    sentences = self.parser.splitSentences(text)
    titleWords = self.parser.removePunctations(title)
    titleWords = self.parser.splitWords(title)

    # Adding keywords in the keyword variable
    [self.parser.getKeywords(sentence) for sentence in sentences]

    topKeywords = self.getTopKeywords(self.parser.keywords[:10])

  def getTopKeywords(self, keywords):
    # Add getting top keywords in the database here
    return keywords
