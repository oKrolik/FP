"""
Consider the sentence: "I ate half of the cheesecake my two roommates made.".

    1- Write a Python program that stores the sentence in chunks in different variables,
as follows: first variable - “I ate”, second variable - “half”,
third variable - “of the cheesecake my”, fourth variable - “two”,
fifth variable - “roommates made.”; and prints the sentence using the concatenation of those variables.
    2 -Now, reassign the second variable with float value 0.5 and the fourth variable with integer value 2.
You will get an error message if you try to rerun the program. After you read the error message carefully,
fix the problem without using the string "0.5" or "2".
"""
a = "I ate"
b = "half"
c = "of the cheesecake my"
d = "two"
e = "roommates made."

b = 0.5
d = 2
print(a+" "+str(b)+" "+c+" "+str(d)+" "+e)