import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def ret_def(word):
    word = word.lower()
    if word in data.keys():
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:  # in case user enters words like USA or NATO
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("did you mean %s instead? Enter Y or N : " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."


    else:
        return "The word doesn't exist. Please double check it."


word = input("\n Enter a word : ")
output = ret_def(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


