"""
Write a Python function var_numbers(number, precision) that returns the variance of all positive integers up to and including number. 
The second parameter defines the precision of the result and has the default value of 2. Use round to approximate the result to the given precision.

Remember the formula of variance:

      N
var(x)=∑    ((xi-x¯)2) / N
      i=1    

where xi is the i-th element of the sequence 1,2,...,number, and x¯ is the average of all those values.

Hint: It is easier if you write an additional function sum_numbers(number) that returns the sum of all
positive integers up to and including number and then use this function in the var_numbers function.
"""

def sum_numbers(number):
    sum = 0
    for i in range(1, number+1):
        sum += i
    return sum

def average(sum, length):
    return sum / length

def var_numbers(number, precision=2):
    res = 0
    for i in range(1, number+1):
        sum = sum_numbers(number)
        avg = average(sum, number)
        res += (i - avg)**2
    return round(res/number, precision)

"""
print("var_numbers(3)")
print(var_numbers(3))
print("var_numbers(10, 1)")
print(var_numbers(10, 1))
print("var_numbers(15, 3)")
print(var_numbers(15, 3))
print("var_numbers(7)")
print(var_numbers(7))
"""