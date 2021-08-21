
import json
data = json.load(open("./data.json")) # default mode is read mode

# method that returns the definition of a word
def lookup(word):
	if word in data:
		return data[word]
	else:
		return "The word doesn't exist. Please double check it."

userword = input("Enter a word: ")
print(lookup(userword))







