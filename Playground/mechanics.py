import math
angle = int(input())*math.pi/180  # convert to radians
cos_angle = math.cos(angle)
sin_angle = math.sin(angle)
print(round((2*18*18*cos_angle*sin_angle)/10))