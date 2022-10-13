"""
Write a Python script that prints a square filled with the # character for a given dimension, greater or equal to 3.

The square centre must be filled with either one or four zeros (0), depending on whether the dimension is odd or even.

For example for dimension 4 the, output is:

####
#00#
#00#
####
and for dimension 5, the output is:

#####
#####
##0##
#####
#####

"""
x = int(input())

if x % 2 != 0:
    for i in range(x//2):
        print ('#'*x)
    print (int(x//2)*'#'+'0'+'#'*int(x//2))
    for i in range(x//2):
        print ('#'*x)
else:
    for i in range(x//2-1):
        print ('#'*x)
    print (int(x//2-1)*'#'+'00'+'#'*int(x//2-1))
    print (int(x//2-1)*'#'+'00'+'#'*int(x//2-1))
    for i in range(x//2-1):
        print ('#'*x)