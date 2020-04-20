import json


data=json.load(open('data.json')) # Load 'data.json' into data variable.

def translate(word):
    # Function 'translate' takes the word variable which 
    # is found in line 16 and searches for it in 'data'. 
    if word in data:
        return data[word]
    else:
        return 'This word does not exist!'

# Stores user input into 'word' variable
# formatting the word to lowercase.
word = input('Enter word: ').lower()                                 
print(translate(word))
