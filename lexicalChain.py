from nltk.corpus import wordnet

class LexicalChain:
  def getSynsets(self, word):
    return wordnet.synsets(word)