# When you create an object and assign it to a variable, the variable only refers to the object
# and does not represent the object itself! That is, the variable name points to that part of
# your computer’s memory where the object is stored. This is called binding the name to the object.

print("Simple Assignment")

shoplist = ['apple', 'mango', 'carrot', 'banana']

# mylist is just another name pointing to the same object!
mylist = shoplist

print("Id of mylist: ", id(mylist))
print("Id of shoplist: ", id(shoplist))

# I purchased the first item, so I remove it from the list
del shoplist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)

# Notice that both shoplist and mylist print the same list without the 'apple'
# confirming that they point to the same object.

print('\nCopy by making a full slice.')
# Make a copy by doing a full slice
mylist = shoplist[:]
# Remove first item
del mylist[0]

print('shoplist is', shoplist)
print('mylist is', mylist)

# Notice that now the two lists are different
