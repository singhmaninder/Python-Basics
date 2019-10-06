# Frozenset is a new class that has the characteristics of a set.
# But its elements cannot be changed once assigned.
# While tuples are immutable lists, frozensets are immutable sets.

# Sets being mutable are unhashable, so they can't be used as dictionary keys.
# On the other hand, frozensets are hashable and can be used as keys to a dictionary.


A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([10, 11, 12, 13])

print("A is disjoint B: {}".format(A.isdisjoint(B)))
print("A is disjoint C: {}".format(A.isdisjoint(C)))
print("A union B {}.".format(A | B))
print("A intersection B {}.".format(A & B))
# print("Update A: {}".format(A.add(5)))
# AttributeError: 'frozenset' object has no attribute 'add'