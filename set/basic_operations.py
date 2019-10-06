# A set is an unordered collection of items.
# Every element is unique (no duplicates) and must be immutable (which cannot be changed).
# However, the set itself is mutable. We can add or remove items from it.

# Sets are mutable. But since they are unordered, indexing have no meaning.
# We cannot access or change an element of set using indexing or slicing. Set does not support it.


countries = set(['India', 'Sri Lanka', 'Pakistan', 'Bangladesh'])

print("Iterate over a set")
for country in countries:
	print('Country: ', country)

print('\nIndia' in countries)
print('USA' in countries)

new_countries = countries.copy()
new_countries.add('China')
new_countries.add('China')
new_countries.add('England')
new_countries.add('Canada')

print("new_countries are: {}.".format(new_countries))

print("\nnew_countries is a superset of countries: {}.".format(new_countries.issuperset(countries)))
print("countries is a subset of new_countries: {}.".format(countries.issubset(new_countries)))

# While using discard() if the item does not exist in the set, it remains unchanged.
# But remove() will raise KeyError exception in such condition.
countries.remove('Pakistan')
countries.discard('Pakistan')

print("\nUnion of new_countries and countries is: {}".format(new_countries | countries))
print("Intersection of new_countries and countries is: {}".format(new_countries & countries))
print("Disjoint of new_countries and countries is: {}".format(new_countries.isdisjoint(countries)))

# Clear a set.
countries.clear()
print("\nLength of countries: {}".format(len(countries)))
