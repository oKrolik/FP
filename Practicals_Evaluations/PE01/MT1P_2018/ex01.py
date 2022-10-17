num = int(input())
c = num//100
d = num//10%10
u = num%10
print("True") if (c**3)+(d**3)+(u**3) == num else print("False")