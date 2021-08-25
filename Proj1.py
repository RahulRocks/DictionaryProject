import json
from difflib import get_close_matches
 
data = json.load(open("./data.json")) # default mode is read mode

# method that returns the definition of a word
def lookup(word):
	word = word.lower()
	if word in data:
		return data[word]
	# Finding the closest match of the word
	elif len(get_close_matches(word,data.keys())) > 0:
		# Confirming user input
		yn =  input("Did you mean %s instead? Enter Y if yes and N if no. " % get_close_matches(word,data.keys())[0])
		
		if yn == "Y":
			return data[get_close_matches(word,data.keys())[0]]
		elif yn == "N":
			return "The word doesn't exist.Please double check it."
		else:
			return "We didn't understand your entry."
	
	else:
		return "The word doesn't exist. Please double check it."

userword = input("Enter a word: ")
#print(lookup(userword))
output = lookup(userword)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)







