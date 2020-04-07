# This program calculates a dog's age

humanYears = int(input("Enter the dog's age in human years: "))
dogYears = 0

if humanYears <= 2:
    dogYears = humanYears * 10.5
else:
    dogYears += (humanYears - 2) * 4
    dogYears += 21

print(f'In dogs' years, that is {dogYears}')
