"""
Write a Python function camel_case(phrase) to convert a given string phrase to the camelCase format.

Camel case (sometimes stylized as camelCase or CamelCase, also known as camel caps or more formally 
as medial capitals) is the practice of writing phrases without spaces or punctuation, indicating the 
separation of words with a single "uppercase" (capital) letter, and the first letter always "lowercase" (minuscule).

Hint: Have a look at the common string operations at https://docs.python.org/3/library/string.html 
and the string methods at https://docs.python.org/3.8/library/stdtypes.html#string-methods
"""

import string

def camel_case(phrase):
    res = ""
    upper = True
    for ch in phrase:
        if ch.isalpha():
            if not upper:
                res += ch.upper()
                upper = True
            else:
                res += ch.lower()
        else:
            if res:
                upper = False
    return res

"""
print(camel_case("Testing"))
print(camel_case("One_more_test"))
print(camel_case("NumberOne"))
print(camel_case("What about Now?"))
"""