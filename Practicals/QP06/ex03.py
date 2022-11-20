"""
Write a Python function local_minima(alist) that receives a list alist and returns a 
list with all local minima for each neighborhood of three elements.

For example, if alist=[4, 2, 2, 5, 1], then we have 3 neighborhoods: 
(i) [4, 2, 2]; 
(ii) [2, 2, 5]; 
(iii) [2, 5, 1].

In this case, there is only one local minima: [1].

Notice that 2 is never a local minimum because it has another value equal to it in the neighborhood.
"""

def local_minima(lst):
    return [y for i, y in enumerate(lst)
            if ((i == 0) or (lst[i - 1] >= y))
            and ((i == len(lst) - 1) or (y < lst[i+1]))]
print(local_minima([10, 3, 3, 14, 5, 7, 4]))
# [3, 5, 4]
print(local_minima([0, 3, 3, 14, 5, 7, 4]))
# [0, 3, 5, 4]
print(local_minima([2, 1, 1, 1, 7, 3, 1]))
# [1, 1]
print(local_minima([5, 1, 43, 21, 5, 63, 1, 5, 5, 5]))
# [1, 1, 5, 5, 1, 1, 1]
