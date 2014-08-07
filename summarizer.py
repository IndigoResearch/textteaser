from parser import Parser

class Summarizer:
  def __init__(self):
    self.parser = Parser()

  def summarize(self, text, title, source, category):
    sentences = self.parser.splitSentences(text)
    titleWords = self.parser.removePunctations(title)
    titleWords = self.parser.splitWords(title)

    [self.parser.getKeywords(sentence) for sentence in sentences]

    print self.parser.keywords