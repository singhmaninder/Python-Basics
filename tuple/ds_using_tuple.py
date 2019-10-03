# To indicate start and stop of tuple
# even though parentheses are optional.
# Explicit is better than implicit.

zoo = ('python', 'elephant', 'penguin')
print 'Number of animals in the zoo is {}.'.format(len(zoo))

new_zoo = 'monkey', 'camel', zoo
print 'All the animals in new zoo are {}.'.format(new_zoo)
print 'Animals brought from old zoo are {}.'.format(new_zoo[2])
print 'Last animal brought from old zoo is {}.'.format(new_zoo[2][2])
print 'Number of animals in new zoo is {}.'.format(len(new_zoo) - 1 + len(new_zoo[2]))