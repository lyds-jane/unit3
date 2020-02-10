Map, Filter, and Reduce
===

The map, filter, and reduce functions help the process of dealing with lists in python. 
This video also briefly went over lambda expressions as simple ways to write expressions in only one line.

Map
---

The map function puts a list through a function, and returns and iteration of the converted list.

For example:
```.py
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
double = lambda n: n * 2
map(numbers, double)
# This will double all the numbers in the list. The first value is the list, the second is the function it is applied to.
```

Filter
---
Filter sorts through a list and eliminates values deemed unecessary. 

For example:
```.py
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
filter(lambda n: n % 2 > 0, numbers)
# This will filter out all the even numbers of the list. The first value is the condition, the second is the list.
```

Reduce
--
Reduce is no longer a built-in function in Python, as it can be easily replaced by a for loop.
The basic logic of it was that it would take a function with two inputs, and systematically apply it to a list.

Here is an example for loop that can be used in place of the reduce function:
```.py
numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
product = 1
for n in numbers:
  product = product * n
```
