def defm(n):
    lista = []
    for x in n:
        if x not in lista:
            lista.append(x)
    return lista

def isomorphic(astring1, astring2):
    uni = list(zip(defm(astring1),  defm(astring2)))
    r = {}
    for x, y in uni:
        r[x] = y
    new_string = ''
    for i in range(len(astring1)):
        new_string = new_string + r.get(astring1[i], '_')
    if new_string == astring2:
        return "'{}' and '{}' are isomorphic because we can map: {}".format(astring1, astring2, uni)
    return "'{}' and '{}' are not isomorphic".format(astring1, astring2)

print(isomorphic('ab', 'aa'))
# 'ab' and 'aa' are not isomorphic
print(isomorphic('paper', 'title'))
# 'paper' and 'title' are isomorphic because we can map: [('p', 't'), ('a', 'i'), ('e', 'l'), ('r', 'e')]
print(isomorphic('foo', 'bar'))
# 'foo' and 'bar' are not isomorphic
print(isomorphic('turtle', 'tletur'))
# 'turtle' and 'tletur' are isomorphic because we can map: [('t', 't'), ('u', 'l'), ('r', 'e'), ('l', 'u'), ('e', 'r')]
