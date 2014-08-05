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

for sentence in parser.splitSentences(input['text']):
  print sentence
  print parser.getSentenceLengthScore(sentence)