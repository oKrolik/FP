"""
Write a Python program to help the user arrive in Lisbon at time.
Ask the user how many hours and how many minutes she can spend travelling at most.
Return the average velocity (in km/h) that she will need to drive to arrive in time.
 Assume the distance between Porto and Lisbon is 313 km.

Please round the result.
"""
t = int(input())*60+int(input())
print(round(313/(t/60)))