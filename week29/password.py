import random
results = []
times = int(input("How many passwords would you like?"))
for i in range(times):
    password = list()
    for a in range(20):
        ref = int(random.randrange(33,126,1))
        add = str(chr(ref))
        password.append(add)
    pwd = "".join(password)
    results.append(pwd)

print(results)
