"""
Write a Python function mask_data(data, n_characters, position) that receives a string data 
and returns the masked string in which the first or last n_characters characters are masked as an asterisk, 
according to position.
The position admits two values: 'begin' — indicating that masking must consider the first n_characters 
characters of the original string — and 'end' — indicating that masking must consider the last n_characters 
of the original string.

If n_characters is zero then the function must return the original string. 
If n_characters is greater than the total of characters of the string or less than zero then the function 
must return all the characters masked by asterisks.
"""

def mask_data(data, n_characters, position):
    if position == "begin":
        res = n_characters * "*" + data[n_characters:]
    if position == "end":
        res = data[:(len(data)-n_characters)] + n_characters * "*"
    return res


print(mask_data("764987002", 4, "begin"))
print(mask_data("John Wick", 0, "begin"))
print(mask_data("202101298", 5, "end"))
print(mask_data("910432409", 4, "end"))