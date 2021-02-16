#!/usr/bin/env python
# coding: utf-8


# Clean Code Cheat Sheet

# 1) Naming Conventions

# variable should be all_lower_case_with_underscores
# CONSTANTS should be ALL_CAPS_WITH_UNDERSCORES
# functions should be all_loser_case_with_underscores
# modules should be all lower case and only only one word if possible

# 2) Only one statement per line

# bad example
a = 1; b = 1 

# good example
a = 1
b = 1

# 3) Short statement (not longer than 79 characters (PEP 8))
# use '/' to make one statement to a multiline statement, if necessary

# bad example
using_some_function_with_a_lot_of_parameters(parameter_number_1, parameter_number_2, parameter_number_3, parameter_number_4, parameter_number_5)

# good example 
using_some_function_with_a_lot_of_parameters(parameter_number_1, 
                                             parameter_number_2, 
                                             parameter_number_3, 
                                             parameter_number_4, 
                                             parameter_number_5)

# 4) Code in containers, so it is easier to comment something out
# This can be helpful if you want to test a specific operation, without a certain step

# bad example
a = (1 + 2 + 
     3 + 5 + 8 + 13)

# good example
a = (
    1 + 2 
     + 3 + 5 # each of this 3 blocks can be commented out and the code would still work
     + 8 + 13
    )

# 5) Be consistent
# What ever you do, be consistent through out the project. A good example is double quotes("") vs. single quotes(''),
# where it does not really matter which one of them you choose. Just decide on one and stick to it.

# bad example
a = "a"
b = 'b'

# good example
a = "a"
b = "b"

# 6) The use of white spaces
# Never use multiple whitespaces after each other. 
# Use exactly one whitespace before and after mathematical operators and one whitespace after commas.
# No whitespace before a comma.

# bad example
a=     "hallo"

# good example
a = 1 + 2 + sum(1, 4)

# 7) Delete old / bad code
# Out commented code should not last longer than one coding session. Before committing or saving the project, DELETE unused code.
# You may think you will use it again, but this is probably not the case. I will only confuse you in the future or makes the code
# much more complicated than it has to be.

# 8) Make comments only if necessary. Good variable names can be better than comments. 
# Never make a comment just that you have made one. It is better to have good code without
# even one comment than having code that is contradict to the comments. 
# Also unnecessary comments can confuse yourself and others in the future.

# bad example
# calculating profit by subtracting the expenses from the revenue
a = b - c

# good example
profit = revenue - expenses

# 9) But use comments if necessary! If you aren't sure if a comment is necessary or not: just make one.

# 10) Make if statements as simple as possible

# bad example 
if not (some_function().and_some_oter_function() != (a + b + c)):

# good example
part_a = some_function().and_some_oter_function()
part_b = a + b + c
if part_a == part_b:

# 11) Try to make as few statement blocks as possible

# bad example
if a:
    if b:
        if c:
            a = 5
    if not b:
        if c:
            a = 4
        
# good example
if a and c: # this makes only sense, if the if statements stay uncomplicated
    if b:
        a = 5
    elif:
        a = 4

# 12) Make tests simple. Multiple simple tests are better than one complicated one. 
# This also makes it easier to identify the root of the problem if tests fail.

# bad example
def test_something():
    
    a = do_one_big_thing_that_does_not_has_his_own_test()
    b = do_anoter_big_thing_that_does_not_has_his_own_test(a)
    c = and_a_third_big_thing_that_does_not_has_his_own_test(b)
    
    self.assertEqual(c, "expected result")
    
# good example
def test_one():
    a = do_one_big_thing_that_does_not_has_his_own_test()
    self.assertEqual(a, "expected result")
    
def test_two():
    b = do_anoter_big_thing_that_does_not_has_his_own_test("a")
    self.assertEqual(b, "expected result")
    
def test_two():
    c = and_a_third_big_thing_that_does_not_has_his_own_test("b")
    self.assertEqual(c, "expected result")

# 13) Using f-strings as often as possible
# There are many ways to include variable values dynamically in a string, but f-strings are by far the most intuitive way to do so.
# Therefore f-strings should be used instead of other approaches like str.format() or adding strings with "+"

# bad example
"This %s %s bad example!" % ("is", "a")

# good example
f"This {'is'} a good {'example'}!"

# 14) Never deleting or adding values to a list, while iterating through it
# It is a very bad idea, to change the number of indexes in a list, while iterating over it.
# The following example will show why:

# bad example
l = [1, 2, 0, 0]
for val in l:
	if val == 0:
		l.remove[val]
print(a)   # -> [1, 2, 0]

# Why is there still a zero in the printed list, shouldn't they have all been remove?
# No, because when the first zero was removed, the second one changed its index from 3 to 2 and was therefore skipped.

# good example
l = l[var for var in l if var != 0]

# 15 Opening files in a with block
# with makes has the advantage, that the file gets automatically closed, when leaving the code block

# bad example
file = open("file.csv")
# do something
file.close() # never forget to close the file

# good example
with open("file.csv") as file:
	# do something

# 16) Write functions with only a few parameters
# Try to use as few arguments in your function as possible. 2 or less is desirable.

# bad example
def make_something(a, b, c, d):

# good example
def make_something(x):
	# use "sub"-parameters by referring them like this:
	a = x.a
	b = x.b
	c = x.c
	d = x.d

# 17) Don't write your own code
# whenever there is a library available, that can make your project easier, use it!
# using library's means having less code and therefore less bad code

# 18) Use a config file
# The use of a config file is very important, to keep all configurations in one place.
# The config file should contain all numerical and string variables, that are build from
# hard coded values. All those variables should be made global (look at the correct naming conventions).
# A config file makes it much more easy for you and other to understand the code.
# This can also solves the "magic numbers" problem.