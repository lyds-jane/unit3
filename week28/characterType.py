# This program counts the number of letters and digits in a string

# Create counters
letters = 0
digits = 0

# get string
string = input("Enter your text here")

# read the type of each character
for char in string:
    if char.isdigit():
        digits+=1

    elif char.isalpha():
        letters+=1

# print the final counters
print(f"There are {letters} letters and {digits} digits.")
