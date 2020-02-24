SL
--
```.py
import matplotlib.pyplot as pyplot

min_x = -2
max_x = 2
num_points = 1000
step = (max_x-min_x)/num_points

x_axis = list()
for f in range(num_points):
    x_axis.append(min_x + step * f)

y = [((s+1) ** 2 - 1) for s in x_axis]

pyplot.plot(x_axis, y)
pyplot.show()
```

HL
--
```.py
import matplotlib.pyplot as pyplot
from math import sin

min_x = 0
max_x = 30
step = 0.5
num_points = int((max_x - min_x)/step)

x = list()
for f in range(0, num_points):
    x.append(min_x + step * f)

m = [t ** 2 for t in x]
y = list()
for i in m:
    y.append(0.1*sin(0.1*i))

pyplot.plot(x, y)
pyplot.show()
```
