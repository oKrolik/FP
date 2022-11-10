"""
We want to write a function that helps in producing change in Euro coins for a given money amount. 
In the Euro denomination there are coins for 2€, 1€, 50c, 20c, 10c, 5c, 2c and 1c. 
If we want to give change using the least amount of coins, we should always use the largest coin for the amount left. 
For example, to pay 3.45€ we should use coins 2€, 1€, 20c, 20c (again) and finally 5c.

Write a function change(amount) that receives a certain amount and returns a list with the least number of coins to pay that amount.
To avoid round-off errors both the amount and coins are positive integers (the number of cents).
"""

def change(amount):
    lst = []
    while amount > 0:
        if (amount >= 200):
            amount -= 200
            lst.append(200)
        elif (amount >= 100):
            amount -= 100
            lst.append(100)
        elif (amount >= 50):
            amount -= 50
            lst.append(50)
        elif (amount >= 20):
            amount -= 20
            lst.append(20)
        elif (amount >= 10):
            amount -= 10
            lst.append(10)
        elif (amount >= 5):
            amount -= 5
            lst.append(5)
        elif (amount >= 2):
            amount -= 2
            lst.append(2)
        elif (amount >= 1):
            amount -= 1
            lst.append(1)
    return lst
            


print(change(345))
# [200, 100, 20, 20, 5]
print(change(500))
# [200, 200, 100]
print(change(17))
# [10, 5, 2]
print(change(6))
# [5, 1]