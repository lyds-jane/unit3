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

starter = ['I hope you know', 'people notice', 'I want you to know', 'no one can ignore', "don't forget", "remember", "I hope you realize", 'everyone thinks about', "don't underestimate", "I really appreciate", "damn, just look at", "think about", "you don't give yourself enough credit for", "you need to remember", "I can't even describe", "think about how so so so so", 'even Obama knows']

compliments = ['gorgeous', 'smart', 'funny', 'kind', 'loved', 'powerful', 'amazing', 'cute', 'generous', 'beautiful', 'nice', 'appreciated', 'stunning', 'cool', 'impressive', 'inspiring', 'intellegent', 'loving', 'talented', 'valued', 'appreciated', 'adorable', 'sweet', 'friendly', 'energetic', 'charasmatic', 'hardworking']

seed = len(compliments) / 2

import random
random.seed(seed)


print("\nHello {}, it's nice to meet you!".format(name))

num = int(input("\nHow many random compliments would you like? "))

for i in range(0,num):
  if num < len(compliments):
    element = random.randint(0, seed)
    comp = compliments.pop(element)
  else:
    comp = random.choice(compliments)
  print('{}, {} how {} you are\n'.format(name, random.choice(starter), comp))

```
