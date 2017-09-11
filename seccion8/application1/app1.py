import json
from difflib import get_close_matches

data=json.load(open('data.json'))

def traslate(w):
    w=w.lower()
    closeMatches = get_close_matches(w,data.keys())
    if w in data:
        return data[w]
    elif len(closeMatches) > 0:
        yn= input('Did you mean %s instead? Enter Y if yes, or N if no.' % closeMatches[0])
        if yn.lower()=='y':
            return data[closeMatches[0]]
        elif yn.lower()=='n':
            return 'The word doesn\'t exist. Please check it.'
        else:
            return 'We didn\'t understand you entry.'
    else:
        return 'The word doesn\'t exist. Please check it.'

word = input('Enter word: ')

output = traslate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
