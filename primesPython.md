Prime Numbers in Python
===

Prime number: A number that can only be devided by 1 and itself.

Version 1: Divide n by all numbers between 2 and n-1
--
This code uses a for loop from 2 to n-1 to test n by every possible divisor. If n module the number is ever equal to 0, the code returns false.

In order to test the time, the following code is used:

```.py
import time

t0 = time.time()
##run function with big range for n
t1 = time.time()
print("Time taken: ", t1 - t0)
```

This is effective, but very slow. In order to speed this up, the number of divisors needs to be reduced. 

Version 2:
---
The number of divisors can be halved by only testing up to the square root of n, as the factors repeat themselves after that.

This code has the same logic as version one. This time, however, the range of the for loop is only from 2 to one more than the maximum divisor.

In order to find the maximum divisor, the following mathematic sequence is used:

```.py
import math

max_divisor = math.floor(math.sqrt(n))
# math.sqrt finds the square root of a number and math.floor rounds the number down.
```

Version 3:
----
It can be halved again by first testing if the number is even, then testing only the odd divisors.

This code's for loop uses a step of two in it, so that only the odd numbers are tested.

This is how the for loop is defined:

```.py
for d in range(3, 1 + max_divisor, 2)
# The 3rd number, in this case 2, is the step for the for loop
```

Version three is much faster than versions one and two. This shows the proper use of DRY, as well as the important of computational thinking.
