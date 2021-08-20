
import json
data = json.load(open("./data.json")) # default mode is read mode

# method that returns the definition of a word
def translate(word):
	return data[word]

word = input("Enter a word: ")
print(translate(word))







