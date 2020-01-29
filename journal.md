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
