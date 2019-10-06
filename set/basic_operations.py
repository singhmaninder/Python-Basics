# Sets are unordered collection of simple objects.
# They are used when existence of an object in a collection
# is more important than the order or how many times it occurs.

countries = set(['India', 'Sri Lanka', 'Pakistan', 'Bangladesh'])

print('India' in countries)
print('USA' in countries)

new_countries = countries.copy()
new_countries.add('China')

print("new_countries is a superset of countries: {}.".format(new_countries.issuperset(countries)))

print("Union of new_countries and countries is: {}".format(new_countries | countries))

countries.remove('Pakistan')

print("Intersection of new_countries and countries is: {}".format(new_countries & countries))