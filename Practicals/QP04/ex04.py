"""
Write a function mastermind(g1, g2, g3, c1, c2, c3) to evaluate a single line of a mastermind game.

The function receives 6 single character strings. Each string can be "b" for blue, "w" for white and "y" for yellow. 
The first 3 arguments are the user guess. The last 3 arguments are the correct key. 
Argument g1 is the user guess for the value at argument c1 and so on.

You should give 3 points for each user guess that is completely correct, that is,
the same color at the same position in the key and 1 point if the user guessed the color 
right but at the wrong position (that is, the color exists in the key but at another wrong position).  
See the tests for examples.

Note that one right guess (position or color) counts only once.
"""

# Bruuuute force
def mastermind(g1, g2, g3, c1, c2, c3):
    points = 0
    if (g1 == c1):  # right guess, position 1
        points += 3 # points received
        g1 = -1     # guess used
        c1 = 0      # position used
    if (g2 == c2):  # right guess, position 2
        points += 3
        g2 = -1
        c2= 0
    if (g3 == c3):  # right guess, position 3
        points += 3
        g3 = -1
        c3 = 0
    if (g1 == c2):  # right guess, wrong position
        points += 1
        g1 = -1
        c2 = 0
    if (g1 == c3):  # right guess, wrong position
        points += 1
        g1 = -1
        c3 = 0
    if (g2 == c1):  # right guess, wrong position
        points += 1
        g2 = -1
        c1 = 0
    if (g2 == c3):  # right guess, wrong position
        points += 1
        g2 = -1
        c3 = 0
    if (g3 == c1):  # right guess, wrong position
        points += 1
        g3 = -1
        c1 = 0
    if (g3 == c2):  # right guess, wrong position
        points += 1
        g3 = -1
        c2 = 0
    return points

"""
# IQ solution but hard to explain
def mastermind(g1, g2, g3, c1, c2, c3):
    user = [g1,g2,g3]
    pc   = [c1,c2,c3]
    count = 0
    for i in range(len(user)-1, -1, -1):
        if user[i] == pc[i]:
            user.pop(i)
            pc.pop(i)
            count += 3 
    for i in range(len(user)-1, -1, -1):
        if user[i] in pc:
            count += 1
            pc.pop(pc.index(user[i]))
    return count
"""

"""
print("mastermind("b", "w", "y", "b", "w", "y")")
print(mastermind("b", "w", "y", "b", "w", "y"))
print("mastermind("b", "b", "y", "b", "w", "b")")
print(mastermind("b", "b", "y", "b", "w", "b"))
print("mastermind("b", "w", "y", "w", "y", "w")")
print(mastermind("b", "w", "y", "w", "y", "w"))
print("mastermind("b", "b", "y", "y", "y", "b")")
print(mastermind("b", "b", "y", "y", "y", "b"))
"""