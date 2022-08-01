# 1. TASK: print "Hello World"
import string
from tokenize import Number
print("Hello World")
# 2. print "Hello Michael!" with the name in a variable
name = "Michael"
print( "Hello", name )	# with a comma
print("Hello " + name)	# with a +
# 3. print "Hello 42!" with the number in a variable
Number = 42
print( "Hello", Number )	# with a comma
print("Hello" + str(Number) )	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "kbbq"
print("I love to eat {} and {}" .format (fave_food1, fave_food2) ) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}" ) # with an f string

string= "this is upper?"
print(string.upper())

string= "IS THIS LOWER?"
print(string.lower())

