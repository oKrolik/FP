"""
Write a Python function adigits(a, b, c) that receives three integers,
each one with a single decimal digit and returns the lowest integer number
that can be assembled with the three digits given as parameters.
"""

def adigits(a, b, c):
    return min(a, b, c)*100 + (a + b + c - max(a, b, c) - min(a, b, c))*10 + max(a, b, c)

"""
print("adigits(1, 2, 3)")
print(adigits(1, 2, 3))
print("adigits(9, 1, 9)")
print(adigits(9, 1, 9))
print("adigits(9, 1, 8)")
print(adigits(9, 1, 8))
print("adigits(0, 1, 0)")
print(adigits(0, 1, 0))
"""
