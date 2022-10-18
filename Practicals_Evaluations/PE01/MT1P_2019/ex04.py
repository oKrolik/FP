tS = float(input())
tC = float(input())
tR = float(input())
tT = tS + tC + tR
vS = 1.5/tS
vC = 40.0/tC
vR = 10.0/tR

if (tT > 4):
    print("Time")
elif (vS < 2):
    print("Swimming")
elif (vC < 20):
    print("Cycling")
elif (vR < 8):
    print("Running")
else:
    print(tT)