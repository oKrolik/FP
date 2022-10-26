"""
Write a Python function rm_letter_rev(ch, s) that removes all occurrences of
a given character ch (case sensitive) from the given string s (case sensitive)
and returns the resulting string with its characters in the reverse order.
"""

def rm_letter_rev(ch, s):
    res = ""
    for c in s:
        if c != ch:
            res = c + res
    return res

print(rm_letter_rev("s", "A style guide is about consistency")) # ycnetinoc tuoba i ediug elyt A
print(rm_letter_rev(" ", "a nut for a jar of tuna")) # anutforajaroftuna
print(rm_letter_rev("a", "Perfectly good sentence with no need to remove letters")) # srettel evomer ot deen on htiw ecnetnes doog yltcefreP
print(rm_letter_rev("l", "Please let me keep my letters!")) # !srette ym peek em te esaeP