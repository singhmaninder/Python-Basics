emplist = ['John', 'David', 'Mark', 'Mike', 'James', 'Curry']
name = 'Maninder Singh'

# Indexing or Subscription operation
print("Employee 0 is {}.".format(emplist[0]))
print("Employee 1 is {}.".format(emplist[1]))
print("Employee 2 is {}.".format(emplist[2]))
print("Employee 3 is {}.".format(emplist[3]))

print("\nEmployee -1 is {}.".format(emplist[-1]))
print("Employee -2 is {}.".format(emplist[-2]))
print("Employee -3 is {}.".format(emplist[-3]))
print("Employee -4 is {}.".format(emplist[-4]))

print("\nCharacter 0 is {}.".format(name[0]))
print("Character 1 is {}.".format(name[1]))
print("Character 2 is {}.".format(name[2]))
print("Character 3 is {}.".format(name[3]))
print("Character 4 is {}.".format(name[4]))
print("Character 5 is {}.".format(name[5]))
print("Character 6 is {}.".format(name[6]))
print("Character 7 is {}.".format(name[7]))

# Slicing on a list
# The start position is included but the end position is excluded from the sequence slice.
print("\nEmployee list from 1 to 3 is {}.".format(emplist[1:3]))
print("Employee list from 2 to end is {}.".format(emplist[2:]))
print("Employee list from 1 to -1 is {}.".format(emplist[1:-1]))
print("Employee list from start to end is {}.".format(emplist[:]))

# You can also provide a third argument for the slice called step size.
# The default value of step size is 1.

print("\nEmployee list with step size 1 is {}.".format(emplist[::1]))
print("Employee list with step size 2 is {}.".format(emplist[::2])) # When step size is 2, we get the items with position 0, 2,..
print("Employee list with step size 3 is {}.".format(emplist[::3])) # When step size is 3, we get the items with position 0, 3,..
print("Employee list with step size 4 is {}.".format(emplist[::4])) # When step size is 4, we get the items with position 0, 4,..
print("Employee list with step size 5 is {}.".format(emplist[::5])) # When step size is 5, we get the items with position 0, 5,..
print("Employee list with step size -1 is {}.".format(emplist[::-1])) # When step size is -1, we get the reverse list.
print("Employee list with step size -2 is {}.".format(emplist[::-2])) # When step size is -2, we get the items with position -1, -3, -5,...
print("Employee list with step size -3 is {}.".format(emplist[::-3])) # When step size is -3, we get the items with position -1, -4, -7,...
