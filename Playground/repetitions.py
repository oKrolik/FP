"""
Write a Python script that given a string text and a number num
prints a new string consisting of text repeated num times, separated by hyphens (-).

Update: The separator was changed. Instead of a space, it is now a hyphen (-).
"""
word = str(input())
print((word + '-') * (int(input()) - 1) + word)