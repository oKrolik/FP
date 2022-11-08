"""
Write a function mastermind(guesses, codes) to evaluate a single line of a mastermind game.

The function receives two lists of single character strings. Each string can be "b" for blue, "w" for white and "y" for yellow. 
The first argument is the user guesses list and the second argument is the codes list containing the correct answer. 
Each guess corresponds to the correct key in the same position, so the first element of the guesses list corresponds to the first element in the correct list and so forth. 
Both list arguments have the same length, but can vary in length between tests.

You should return a pair of integers: the first integer is the number of matches in corresponding position and the second integer is the number of matches in an incorrect position.

Note that one right guess (position or color) counts only once.
"""

def mastermind(guesses, codes):
    countg = 0
    countc = 0
    for i in range(len(guesses)-1, -1, -1):
        if guesses[i] == codes[i]:
            guesses.pop(i)
            codes.pop(i)
            countg += 1 
    for i in range(len(guesses)-1, -1, -1):
        if guesses[i] in codes:
            countc += 1
            codes.pop(codes.index(guesses[i]))
    return (countg, countc)


print(mastermind(["b", "w", "y"], ["b", "w", "y"]))
# (3, 0)
print(mastermind(["b", "b", "y"], ["b", "w", "b"]))
# (1, 1)
print(mastermind(["b", "w", "y"], ["w", "y", "w"]))
# (0, 2)
print(mastermind(["b", "y"], ["y", "b"]))
# (0, 2)
