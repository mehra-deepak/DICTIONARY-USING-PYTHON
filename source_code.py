import json # for collection of words
from difflib import get_close_matches
#Difflib is a library of functions in Python that
# compares sequences and strings and get_close_matches() 
# is a function in difflib that returns close matches to a string


collection = json.load(open("collection.json"))

def word_meaning(word):
    word = word.lower() # to convert to lowercase
    if word in collection:
        return collection[word]
    elif len(get_close_matches(word, collection.keys())) > 0: #wrapped inside len becuase it gets executed only when users enters something
        yn = input("Are you looking for the word %s ? Enter Y for Yes or N for No: " % get_close_matches(word, collection.keys())[0])
        if yn == "Y":
            return collection[get_close_matches(word, collection.keys())[0]]
        elif yn == "N":
            return "Word not found. Please try again."
        else:
            return "Please enter either Y or N"
    else:
        return "No word entered"

print('\n***** WELCOME TO THE PYTHON ENGLISH DICTIONARY *****\n')
word = input("Enter word: ")
output = word_meaning(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


