from summarizer import Summarizer


def getInput():
    with open('input.txt') as file:
        content = file.readlines()

    # remove unnecessary \n
    content = [c.replace('\n', '') for c in content if c != '\n']

    title = content[0]
    text = content[-(len(content) - 1):]

    return {'title': title, 'text': ' '.join(text)}

# #####################

input = getInput()
input['text'] = input['text'].decode("ascii", "ignore")

input['text'] = " ".join(input['text'].replace("\n", " ").split())

summarizer = Summarizer()
result = summarizer.summarize(input['text'], input['title'], 'Undefined', 'Undefined')
result = summarizer.sortScore(result)
result = summarizer.sortSentences(result[:30])

print 'Summary:'

for r in result:
    print r['sentence']
    # print r['totalScore']
    # print r['order']
