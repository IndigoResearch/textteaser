from parser import Parser

class Summarizer:
  def __init__(self):
    self.parser = Parser()

  def summarize(self, title, source, category):
    sentences = self.parser.splitSentences(text)
    titleWords = self.parser.removePunctations(title)
    titleWords = self.parser.splitWords(title)

    for sentence in sentences:
      parser.getKeywords(sentence)