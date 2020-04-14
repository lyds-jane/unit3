inputs = input("Enter your first name, Last name, and a number separated by spaces")
data = inputs.split()
i = 0
for line in data:
    i+=1
    if i == 1:
        first = line.lower()
    elif i == 2:
        last = line.lower()
    elif i == 3:
        num = line
        break
print(f'{first}.{last}{num}@uwcisak.jp')
