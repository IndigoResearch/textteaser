from lexicalChain import LexicalChain

lc = LexicalChain()
synsets = lc.getSynsets('family')

for synset in synsets:
  print synset.lemma_names()