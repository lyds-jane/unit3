List Practice
===

#1 - Even Indices
--
```.py
numbers = input().split()

for i in range(len(numbers)):
  if i % 2 == 0:
    print(numbers[i])
```

#2 - Even Elements
--
```.py
numbers = [int(i) for i in input().split()]

for i in numbers:
  if i % 2 == 0:
    print(i)
```

#3 - Greater Than Previous
---
```.py
numbers = [int(i) for i in input().split()]

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        print(numbers[i])
```

$4 - Neighbours of the Same Sign
--
```.py
numbers = [int(i) for i in input().split()]

for i in range(0, len(numbers)-1):
    if (numbers[i] > 0 and numbers[i+1] > 0) or (numbers[i] < 0 and numbers[i+1] < 0):
        print(numbers[i], numbers[i+1])
        break
```

#5 - Greater Than Neighbours
--
```.py
numbers = [int(i) for i in input().split()]
counter = 0

for a in range(1, len(numbers)-1):
    if numbers[a-1] < numbers[a] > numbers[a+1]:
        counter += 1
print(counter)
```
