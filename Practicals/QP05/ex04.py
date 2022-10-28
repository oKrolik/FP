"""
A directed multi-graph is a graph in which two vertices may be connected by multiple edges, 
such as the graph drawn in the figure:

A possible representation of a multi-graph is as a tuple of pairs, each representing a single edge. 
For example, the multi-graph of the figure would be represented 
as (('A','B'), ('A','C'), ('B','C'), ('C','B'), ('A','B')).

A more succinct representation would be as a tuple of triples, each representing a multi-edge 
associated with a multiplicity. The same graph would then be represented 
as (('A',2,'B'), ('A',1,'C'), ('B',1,'C'), ('C',1,'B')).

Write a Python function multi(g) that given a multi-graph g as a tuple of pairs, 
returns its representation as a tuple of triples with multiplicities. 
The order of triples in the tuple is irrelevant.
"""

"""
def multi(g):
    return

print(tuple(sorted(multi((('A','B'),('A','C'),('B','C'),('C','B'),('A','B'))))))
print(tuple(sorted(multi(()))))
print(tuple(sorted(multi(((1,2),(2,3),(3,4))))))
print(tuple(sorted(multi((('A','B'),('B','A'))))))

"""

def multi(g):
    res = ()
    aux = ()
    for i in g:
        (x, y) = i
        res += ((x, g.count(i), y),)
    for i in res:
        if i not in aux:
            aux += (i,)
    return (aux)

"""
print(tuple(sorted(multi((('A','B'),('A','C'),('B','C'),('C','B'),('A','B'))))))
print(tuple(sorted(multi(()))))
print(tuple(sorted(multi(((1,2),(2,3),(3,4))))))
print(tuple(sorted(multi((('A','B'),('B','A'))))))
"""