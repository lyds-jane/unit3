# Paying with strings

# read the text from the file
from functools import reduce

file = open("text.txt", "r")

extract = file.read()

# Counting words
words = extract.split()
print("Number of words is {}".format(len(words)))

# Checking if certain words are in text
for a in ["house", "worker", "master", "hard", "responsible", "skillful"]:
    print("Checking word '" + a + "' in the text. Found if True.")
    print(a in words)

# Counting total characters and letters
lengthOfText = len(extract)
# How do we ONLY get letters?
# Using C thinking
num_letters = 0
for symbol in extract:
    if symbol.isalpha():
        num_letters += 1
print(f'There are {num_letters} out of {lengthOfText} total characters')

# Printing in lowercase
print(extract.lower())

# Printing all numbers with more than 5 characters with "#"
print("#".join(list(filter(lambda a: len(a) > 5, words))))

# Adding all ORD values for the text
totalSum = 0
for l in extract:
    totalSum += ord(l)
print(totalSum)

customers = [{'name':'John', 'address':'london'},
             {'name':'Anna', 'address':'london'}]

for customer in customers:
    for key, value in customers.items():
        print(f'The key is {key} amd the value is {value}')
