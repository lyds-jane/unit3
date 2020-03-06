## 1. Onboarding
```.py
# game loop
while 1:
    enemy_1 = input()  # name of enemy 1
    dist_1 = int(input())  # distance to enemy 1
    enemy_2 = input()  # name of enemy 2
    dist_2 = int(input())
    
    if dist_1 < dist_2:
        print(enemy_1)
    else:
        print(enemy_2)
        # distance to enemy 2
```

## 2. The Descent
```.py
import sys
import math

# game loop
while True:
    highest = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        if(mountain_h > highest):
            highest = mountain_h
            place = i
    print(place)
 ```
 
## 3. Power of Thor
 ```.py
 import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
x = initial_tx
y = initial_ty
    
while True:
    remaining_turns = int(input())
    if(light_x < x):
        if(light_y < y):
            print("NW")
            y -= 1
        if(light_y > y):
            print("SW")
            y += 1
        else:
            print("W")
        x -= 1
    elif(light_x > x):
        if(light_y < y):
            print("NE")
            y -= 1
        if(light_y > y):
            print("SE")
            y += 1
        else:
            print("E")
    else:
        if(light_y < y):
            y -= 1
            print("N")
        if(light_y > y):
            y += 1
            print("S")
```
 
