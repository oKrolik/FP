"""
Write a function primes_difference(n) that given a positive integer n, where n > 3, 
returns the difference between the first prime number greater than n and the first prime number smaller than or equal to n.

A prime number is a natural number greater than 1 that can only be divided by 1 or itself.

For example, for n=45, the function returns 4 = (47-43).

Hint: Write a boolean function is_prime(n) to check whether a number n is prime or not.
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    return True

def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

def prev_prime(n):
    while not is_prime(n):
        n -= 1
    return n

def primes_difference(n):
    return next_prime(n) - prev_prime(n)

"""
print("primes_difference(74)")
print(primes_difference(74))
print("primes_difference(60)")
print(primes_difference(60))
print("primes_difference(10)")
print(primes_difference(10))
print("primes_difference(193)")
print(primes_difference(193))
"""