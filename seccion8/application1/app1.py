import json

data=json.load(open('data.json'))

def traslate(w):
    w=w.lower()
    if w in data:
        return data[w]
    else:
        return 'The word doesn\'t exist. Please check it.'

word=input('Enter word: ')

print(traslate(word))
