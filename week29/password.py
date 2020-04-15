import random
results = []

for i in input("How many passwords would you like?"):
    password = list()
    for a in range(20):
        ref = int(random.randrange(33,176,1))
        add = str(chr(ref))
        password.append(add)
    pwd = "".join(password)
    results.append(pwd)

print(results)
