"""
Convert the following diagram to computer code in Python.

The operations should be done sequentially.
Be aware of the precedence of the operations and that operands higher up in
the diagram have precedence over operands lower down.
"""
a = int(input())*3-5
b = (int(input())+6)//4
c = int(input())**2
print(a+b)
print(b-c)