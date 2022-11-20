romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def roman_to_integer(astring):
    r = 0
    for x in range(len(astring)-1):
        if romans[astring[x]] >= romans[astring[x+1]]:
            r += romans[astring[x]]
        else:
            r -= romans[astring[x]]
    r += romans[astring[-1]]
    return r

print(roman_to_integer('XV'))
# 15
print(roman_to_integer('LXXXIV'))
# 84
print(roman_to_integer('XLIII'))
# 43
print(roman_to_integer('MMMCMXCIX'))
# 3999

