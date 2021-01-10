# Use this interpreter, by typing 'python dsl_interpreter.py simple.dsl' into the console.
# If you want to use some other .dsl file, just change the path :)

import sys

# my functions:
# (could be outsourced in it own module)

functions = {'plus': lambda a, b: a + b,
             'minus': lambda a, b: a - b,
             'times': lambda a, b: a * b,
             'divided_by': lambda a, b: a / b}

variables = {}

# check if exactly two files are given (dsl_interpreter.py and simple.dsl)
if len(sys.argv) != 2:
    sys.exit(1)

# open .dsl and go through each line
with open(sys.argv[1]) as file:
    for line in file:
        line = line.strip()
        # check if the line is a comment
        if not line or line[0] == '*':
            continue
        parts = line.split()

        # check the instructions for each line and execute them
        if parts[1] == 'display':
            print(variables[parts[0]])

        elif parts[1] == 'equals':
            a = int(parts[2]) if parts[2].isdigit() else variables[parts[2]]
            b = int(parts[4]) if parts[4].isdigit() else variables[parts[4]]

            variables[parts[0]] = functions[parts[3]](a, b)









