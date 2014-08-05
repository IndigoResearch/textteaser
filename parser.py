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

  # Jagadeesh, J., Pingali, P., & Varma, V. (2005). Sentence Extraction Based Single Document Summarization. International Institute of Information Technology, Hyderabad, India, 5.
  def getSentencePositionScore(self, i, sentenceCount):
    normalized = i / (sentenceCount * 1.0)

    if normalized > 0 and normalized <= 0.1:
      return 0.17
    elif normalized > 0.1 and normalized <= 0.2:
      return 0.23
    elif normalized > 0.2 and normalized <= 0.3:
      return 0.14
    elif normalized > 0.3 and normalized <= 0.4:
      return 0.08
    elif normalized > 0.4 and normalized <= 0.5:
      return 0.05
    elif normalized > 0.5 and normalized <= 0.6:
      return 0.04
    elif normalized > 0.6 and normalized <= 0.7:
      return 0.06
    elif normalized > 0.7 and normalized <= 0.8:
      return 0.04
    elif normalized > 0.8 and normalized <= 0.9:
      return 0.04
    elif normalized > 0.9 and normalized <= 1.0:
      return 0.15
    else:
      return 0