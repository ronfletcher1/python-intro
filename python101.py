print "Hello World"
print ("Hello World P3")
print """
    It was a dark and stormy night.
   A murder happened
    """
    # a variable is jsut a fast way to refer to something else
    # variables do not make the program faster.
    # they make the program slower
    # Variables make it easier for us to write programs

theBestClass = "the 11-18 immersive"
print theBestClass
    
#    Data Types
#    - Programming languages see different types of variables
#    differently
    # - String - English stuff
    # - Number - I think you know what this is. Something with numbers (or - or e)
    #print 3.e10+"Joe"
    # Floats, integers
    # -- float = it has a . in it
    # -- integer - has no .
    # -Booleans - true or false, on or off, 1 or 0
    # -List - list of things. a single variable with a bunch of parts
    # Dictionaries - variable of variables
    # Objects - super Dictionaries

    # Primitive Data Types = string, number, Boolean

month = "November"
print type (month)
date = 13
print type (date)
dateAsFloat = 13.0
print type(dateAsFloat)
aBool = True
print type(aBool)
aList = []
print type (aList)
aDictionary = {}
print type (aDictionary)

#concatenate is programming speal for add things together
first = "Ron"
last = "Fletcher"
fullName = first + " " + last;
print fullName


fourteen = 10 + 4
print fourteen
fourteen = "10" + "4"
print fourteen

# fourteen = 10 + "4"
# print fourteen

# cast = change a variable to a new data type
# fourteen = int("10") + 4
# fourteen = int("ten") + 4

# Math = +, -, /, *, %
print 2 + 2
print 2 - 2
print 2 / 2
print 2 * 2

# % = modulus.  Modulus divides the number and gives you the remainder
print 2 % 2
print 2 % 3
print 2**3
print 10**87
print "-" * 20
print "Ron " * 20




# Input
# Python 2 = raw_input
# Python 3 = input
name = raw_input ("what is yout name?")
print name 
print type(name)

# conditionals
# a single = sign, means set the left to whatever is on the right
# two = signs, means compare what's on the left, to whatever is on the right
print 2 ==2
print 2 ==1
print 2 =="2"
secret_number = 5;
if (secret_number ==3):
    print "Secret number is 5";
else:
    print "Secret number is not 3"

game_on = True
i = 0;
while(game_on = true)
    i+ = 1
    if(i == 10):
        game_on = false
    else:
        print "Game on!!!"

