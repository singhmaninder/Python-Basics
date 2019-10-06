# Basic operations on a dictionary

user_info = {
    'Maninder Singh': 'singhmaninder1001@gmail.com',
    'Sam': 'sam@gmail.com',
    'Larry': 'larry@gmail.com'
}

print('Maninder\'s email address is {}.'.format(user_info['Maninder Singh']))

# Deleting a key value pair

del user_info['Larry']

print('\nThere are {} contacts in address book now.'.format(len(user_info)))


for name, email in user_info.items():
    print('Name:', name)
    print('Email:', email)

# Adding a new key in dictionary
user_info['John'] = 'john@gmail.com'

if 'John' in user_info:
    print("\nJohn's email address is {}.".format(user_info['John']))
