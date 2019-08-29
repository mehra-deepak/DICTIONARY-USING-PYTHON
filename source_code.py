import json

# opening the json file and loading it to our variable named collection
collection =json.load(open("collection.json"))

# defining the fucntion

def word_meaning:
    word=word.lower() # for case sensitivity
    if word in collection:
        return collection[word]


