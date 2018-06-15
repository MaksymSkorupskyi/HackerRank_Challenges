# These are here so you can change them to customize the program
# easily.

import sys


def ask_yes_no(question):
    while True:
        answer = input(question + ' (y or n) ')
        if answer == 'Y' or answer == 'y':
            return True
        if answer == 'N' or answer == 'n':
            return False


def greet():
    with open(filename, 'r') as f:
        for line in f:
            print(line.rstrip('\n'))


default_greeting = "Hello World!"
filename = "greeting.txt"

try:
    greet()
except OSError:
    print("Cannot read '%s'!" % filename, file=sys.stderr)
    if ask_yes_no("Would you like to create a default greeting file?"):
        with open(filename, 'w') as f:
            print(default_greeting, file=f)
        greet()
