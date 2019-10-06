import sys

print('The command line arguments are: ')
for arg in sys.argv:
    print (arg)

print ('\n\nThe PYTHONPATH is', sys.path)


if __name__ == '__main__':
    print ('\nThe program is being run by itself.')
else:
    print ('I am being imported from another module.')
