ts = float(input()) # 1.5km, 2 km/h
tc = float(input()) #  40km, 20km/h
tr = float(input()) #  10km, 8 km/h

vs = 1.5  / ts
vc = 40.0 / tc
vr = 10.0 / tr

total = ts + tc + tr

if (total > 4):
    print("Time")
elif (vs < 2):
    print("Swimming")
elif (vc < 20):
    print("Cycling")
elif (vr < 8):
    print("Running")
else:
    print(total)