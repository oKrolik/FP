from math import pi

shape = str(input())
r = float(input())
if shape == "sphere":
    result = (4/3)*pi*(r**3)
if shape == "cylinder":
    h = float(input())
    result = pi*h*(r**2)
if shape == "cone":
    h = float(input())
    result = (1/3)*pi*h*(r**2)
print(round(result, 1))