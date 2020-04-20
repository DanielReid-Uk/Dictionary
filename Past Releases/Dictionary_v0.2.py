import json
from difflib import get_close_matches # Allows us to compare likeness of 'word' with 'data.json'

data = json.load(open('data.json'))

def translate(word):
    # Function 'translate' takes the word variable which 
    # is found in line 16 and searches for it in 'data'. 
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        # If word can not be found first time around and 'get_close_matches' has 
        # at least one likely match, then run this statement. 
        answer=input('Did you mean %s instead? enter Y/N: ' %get_close_matches(word, data.keys())[0])
        if answer.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        else:
         return 'This word you wanted does not exist!'   
    else:
        return 'This word does not exist!'

word = input('Enter word: ')
print(translate(word))
