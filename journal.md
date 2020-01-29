29/01/2020
---

### What I did
* Created basic python programs
* Experiemented with using and changing arrays:
```
val = [10, 45, 6, 34, 12, 34, 56, 67, 78, 89, 56, 5, 4]

switch = 5

while switch != 0:
  switch = 0
  for i in range(0, len(val)-1):
    current_val = val[i]
    next_val = val[i+1]
    if current_val > next_val:
      holder = val[i]
      val[i] = val[i+1]
      val[i+1] = holder
      switch += 1
  print(val)
```

### What I learned
* Basic python syntax, including:

&rightarrow; Arrays

&rightarrow; Loops

&rightarrow; Variable declaration

&rightarrow; Built-in functions like .capitalize

### Questions I have
* What are we going to do with python?

### Other
I experimented with Python to make a random compliment generator. This taught me about the random function, as well as more uses for arrays. 
```


name = input('Your name is: ')

compliments = ['gorgeous', 'smart', 'funny', 'kind', 'loved', 'powerful', 'amazing', 'cute', 'generous', 'beautiful', 'nice', 'gentle', 'appreciated', 'stunning', 'cool', 'impressive', 'inspiring', 'intellegent', 'loving', 'talented', 'valued', 'appreciated', 'adorable', 'sweet', 'friendly', 'energetic', 'charasmatic', 'hardworking']

seed = len(compliments) / 2

import random
random.seed(seed)


print("Hello", name, "it's nice to meet you")

num = int(input("How many random compliments would you like? "))
print("")

for i in range(0,num):
  element = random.randit(0, seed)
  print('{}, you are so {}'.format(name, compliments.pop(element)))
  print("")
```
