import math
from math import pi, tan, cos

g = 9.81
v = 44
theta = 80 * (pi/180)
x = 0.5
y0 = 1

y = y0 + x * tan(theta) - ((g * x**2) / (2 * (v*cos(theta))**2))
print(y)



