import json
from difflib import get_close_matches
 
data = json.load(open("./data.json")) # default mode is read mode

# method that returns the definition of a word
def lookup(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys())) > 0:
		return "Did you mean %s instead?" % get_close_matches(word,data.keys())[0]
	else:
		return "The word doesn't exist. Please double check it."

userword = input("Enter a word: ")
print(lookup(userword))







