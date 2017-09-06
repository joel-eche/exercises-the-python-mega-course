import json

data=json.load(open('data.json'))

def traslate(w):
    return data[w]

word=input('Enter word: ')

print(traslate(word))
