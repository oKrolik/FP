"""
Given a tuple of size > 3, write a Python function triplet(tup) that finds a triplet (a, b, c) 
where a, b, c are elements of tup, such that their sum is zero (a + b + c = 0).

In case there is more than one triplet that sums up to zero, return the first occurrence 
when searching by lexicographical order of indexes. In case there are none, return an empty tuple, ().
"""

def triplet(tup):
    found = False
    for i in range(len(tup)-2):
        for j in range(i+1, len(tup)-1):
            for k in range(j+1, len(tup)):
                if (tup[i] + tup[j] + tup[k] == 0):
                    found = True
                    return (tup[i], tup[j], tup[k])
    if (found == False):
        return ()

print(triplet((-8, 0, 4, -2, -1, 1, 2)))
print(triplet((-1, 1, 1, 1)))
print(triplet((-4, 3, 0, -2, -1, -3)))
print(triplet((-1, 0, -5, -2, 4, 5, 15, 21, 42, 3)))