from parser import Parser
from summarizer import Summarizer

def getInput():
  with open('input.txt') as file:
    content = file.readlines()

  # remove unnecessary \n
  content = [c.replace('\n', '') for c in content if c != '\n']

  title = content[0]
  text = content[1:-1]

  return {'title': title, 'text': ' '.join(text)}

# #####################

input = getInput()

# parser = Parser()
# sentences = parser.splitSentences(input['text'])
# title = input['title']
# title = parser.removePunctations(title)
# title = parser.splitWords(title)

# for i, sentence in enumerate(sentences):
#   sentence = parser.removePunctations(sentence)
#   sentence = parser.splitWords(sentence)
#   parser.getKeywords(sentence)

#   print parser.getSentenceLengthScore(sentence)
#   print parser.getSentencePositionScore(i, len(sentences))
#   print parser.getTitleScore(title, sentence)

# keywords = sorted(parser.keywords, key = lambda x: -x['count'])

# for keyword in keywords:
#   print keyword

summarizer = Summarizer()
summarizer.summarize(input['text'], input['title'], 'Undefined', 'Undefined')