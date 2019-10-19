""" When the values in a dictionary are collections (lists, dicts, etc.) then in
    this case, the value (an empty list or dict) must be initialized the first time
    a given key is used. While this is relatively easy to do manually,
    the defaultdict type automates and simplifies these kinds of operations.


    A defaultdict works exactly like a normal dict, but it is initialized with a
    function (“default factory”) that takes no arguments and provides the default
    value for a nonexistent key.

    A defaultdict will never raise a KeyError. Any key that does not exist gets the
    value returned by the default factory.
 """

from collections import defaultdict
ice_cream = defaultdict(lambda: 'Vanilla')

ice_cream['Mike'] = 'Butter Scotch'
ice_cream['John'] = 'Strawberry'

print(ice_cream)
print(ice_cream['David'])

""" Output
    defaultdict(<function <lambda> at 0x7f4d052daa60>, {'John': 'Strawberry', 'Mike': 'Butter Scotch'})
    Vanilla
"""


"""
	In the next example, we start with a list of states and cities. We want to build a
	dictionary where the keys are the state abbreviations and the values are lists of all
	cities for that state. To build this dictionary of lists, we use a defaultdict with a
	default factory of list. A new list is created for each new key.
"""
city_list = [('TX','Austin'), ('TX','Houston'), ('NY','Albany'), ('NY', 'Syracuse'),('NY', 'Buffalo'),
('NY', 'Rochester'), ('TX', 'Dallas'), ('CA','Sacramento'), ('CA', 'Palo Alto'), ('GA', 'Atlanta')]

cities_by_state = defaultdict(list)

for state, city in city_list:
    cities_by_state[state].append(city)

print(cities_by_state)

""" Output
    defaultdict(<class 'list'>, {'GA': ['Atlanta'], 'TX': ['Austin', 'Houston', 'Dallas'],
    'NY': ['Albany', 'Syracuse', 'Buffalo', 'Rochester'], 'CA': ['Sacramento', 'Palo Alto']})
"""
