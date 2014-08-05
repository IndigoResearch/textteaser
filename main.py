from parser import Parser

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

parser = Parser()
sentences = parser.splitSentences(input['text'])

for i, sentence in enumerate(sentences):
  print sentence
  print i
  # print parser.getSentenceLengthScore(sentence)
  print parser.getSentencePositionScore(i, len(sentences))