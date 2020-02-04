Input, print and numbers
---

### "Sum of three numbers
```.py
# This program reads three numbers and prints their sum:
a = int(input()) # Gets an input
b = int(input())
c = int(input())
print(a + b + c) # Prints the sum of the inputs
```

### "Square"
```.py
#Read an integer:
a = int(input()) # Gets an input
print(a**) # Prints the square of the input
```

### "Apple Sharing"
```.py
# This program determines how many apples (out of K) N students get, and how many are leftover
n = int(input())
k = int(input())
print("Each of the {} students will get {} apples. There will be {} left over.".format(n, k/n, k%n))
```

### "Previous and Next"
```.py
# This program reads an integer number and prints its previous and next numbers

a = int(input())
print("The next number for the number {} is {}.".format(a, a+1))
print("The previous number for the number {} is {}.".format(a, a-1))
```

### "Two Timestamps"
```.py
#Given two timestamps, this program calculates how many seconds is between them

hour1 = int(input())
min1 = int(input())
sec1 = int(input())

hour2 = int(input())
min2 = int(input())
sec2 = int(input())

print((sec2 - sec1) + (min2*60 - min1*60) + (hour2*3600 - hour1*3600))
```

Integer and float numbers
---

### "Last Digit of Integer"
```.py
# This program prints the last digit of an integer 

num = int(input())
print (num%10)
```

### "Tens Digit"
```.py
# This program prints a number's ten digit
num = int(input())
print(num%100//10)
```

### "Car Route"
```.py
# If a car can cover N km a day, this calculates how long it will take that car to travel M km
from math import ceil

n = int(input())
m = int(input())

x = m/n
y = ceil(x)
print(y)
```

### "Digital Clock"
```.py
# Given the minutes since midnight, this program prints the current time

min = int(input())
print("{} {}".format(min//60, min%60))
```


Conditions if then else
---

### "Minimum of Two Numbers"
```.python
# This program prints the smaller of two values
num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(num2)
elif num2 > num1:
    print(num1)
else:
    print("Numbers are the same")
```

### "Sign Function"
```.py
# This program detects the sign of an integer
num = int(input())
if num < 0:
    print("-1")
elif num > 0:
    print("1")
else:
    print("0")
```

### "Rook Move"
```.py
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

if (num1 == num3 or num2 == num4):
    print("YES")
else:
    print("NO")
 ```
 
 ### "Chocolate Bar"
```.py
 # This program determines if a chocolate bar with the dimensions n,m can be split along a line so that one part has k squares
n = int(input())
m = int(input())
k = int(input())

if k < n*m and (k%n == 0 or k%m == 0):
    print("YES")
else:
    print("NO")
 ```
 
 For Loop with Range
 --
 
 ### "Sum of N Numbers"
 ```.python
 # This program adds n nubmer of inputs

n = int(input())
total = 0

for i in range(n):
    total += input()

print(total)
```

### "Number of Zeros"
```.py
n = int(input())
counter = 0

for i in range(n):
    if int(input()) == 0:
        counter += 1

print(counter)
```

### "Lost Card"
```.py
n = int(input())
total = 0
missing_total = 0

for i in range(n):
    total += i

for a in range(n):
    missing_total += int(input()) #it's not letting me do this an I'm not sure why
    lost = missing_total - total 
print(lost)
```
