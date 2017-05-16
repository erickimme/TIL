#codecademy python 
# link : https://www.codecademy.com/en/courses/introduction-to-python-6WeG3/0/1?curriculum_id=4f89dab3d788890003000096

# Index
#  1. Python Syntax
# 	1) Python Syntax
# 		Variable & Data Types
# 		2. WhiteSpace and Statements
# 		3. Comments
# 		4. Math Operations
# 		5. Review
# 	2) Tip Calculator

#  2.  Strings and Console Output
# 	1) Strings & Console Output
# 	2) Date and Time
# 	3) Python Strings
# 	4) Basic String Operations

# 3. Conditionals and Control Flow
# 	1) Conditionals & Control Flow
# 	2) PygLatin
# 	3) Conditionals and Loops
# 	4) Conditionals in Python
# 	5) Booleans

# 4. Functions
# 	1) Functions
# 	2) Taking a Vacation
# 	3) Functions can return something
# 	4) Intro to Functions

# 5. Lists & Dictionaries
# 	1) Python Lists and Dictionaries
# 	2) A day at the Supermarket
# 	3) Introduction to Python Lists
# 	4) Dictionaries, Oh Lovely Dictionaries

# 6. Student Becomes the Teacher

# 7. Lists and Functions
# 	1) Lists and Functions
# 	2) Battleship!
# 	3) Using Global Variable in Python
# 	4) Differences Between Sets and Lists

# 8. Loops
# 	1) Loops
# 	2) Practice Makes Perfect
# 	3) Emulate a Do While Loops
# 	4) For Else Loop

# 9. Exam Statistics
# 	1) Exam Statistics

# 10. Advanced Topics in Python
# 	1) Advanced Topics in python
# 	2) Introduction to Bitwise Operators
# 	3) Binary
# 	4) Binary and Pac-man
# 	5) Python : Lambda Functions
	
# 11. Introduction to Classes
# 	1) Introduction to Classes
# 	2) Classes
# 	3) Object Oriented Programming Definition
# 	4) Modules Classes and Objects

# 12. File Input and Output
# 	1) File Input/Output
# 	2) What are Buffers For?
# 	3) Python Files

# 13. Python Final Project



############ Starts Here! ############

####1. Python Syntax

###1) Python Syntax
##a. Welcome
print "Welcome to Python!"

##b. Variables
my_variable = 10

##c. Booleans
# Set the variables to the values listed in the instru
my_int = 7
my_float = 1.23
my_bool = True

##d. You've been reassigned
# my_int is set to 7 below. What do you think
# will happen if we reset it to 3 and print the result?

my_int = 7

# Change the value of my_int to 3 on line 8!

my_int = 3

# Here's some code that will print my_int to the console:
# The print keyword will be covered in detail soon!

print my_int # -> 3 None


##e. WhiteSpace
def spam():
    eggs = 12
return eggs
        
print spam()


## f. Whitespace Means Right Space
def spam():
    eggs = 12
    return eggs
     
print spam()

## g. A matter of Interpretation
cats = 3

spam = True

eggs = False


## h. Single Line Comments
#mysterious_variable = 42

## i. Multi-Line Comments
"""
hi
bye
hello
good bye
"""


## j. Math
# Set count_to equal to the sum of two big numbers

count_to = 90+123123

print count_to


## k. Exponentiation
#Set eggs equal to 100 using exponentiation on line 3!

eggs = 10**2

print eggs

## l. Modulo
#Set spam equal to 1 using modulo on line 3!

spam = 3%2

print spam

## m. Review
# review
monty = True #Boolean
python = 1.234 #float
monty_python = python **2

### 2) Tip Calculator
## a. The meal
# Assign the variable meal the value 44.50 on line 3!

meal = 44.50

## b. The Tax
meal = 44.50
tax = 6.75/100

## c. The Tip
# You're almost there! Assign the tip variable on line 5.

meal = 44.50
tax = 0.0675
tip = 0.15

## d. Reassign in a Single Line
# Reassign meal on line 7!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal*tax


## e. The Total
# Assign the variable total on line 8!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)



#### 2.  Strings and Console Output
### 1) Strings & Console Output
## a. Strings
# Set the variable brian on line 3!

brian = "Hello life!"

## b. Practices
# Assign your variables below, each on its own line!
caesar = "Graham"
praline = "John"
viking = "Teresa"

# Put your variables above this line

print caesar
print praline
print viking

## c. Escaping characters
# The string below is broken. Fix it using the escape backslash!

'This isn\'t flying, this is falling with style!'

## d. Access by Index
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]

print fifth_letter


## e. String methods
parrot = "Norwegian Blue"
print len(parrot)

## f. lower()
parrot = "Norwegian Blue"

print parrot.lower()

## g. uppoer()
parrot = "norwegian blue"

print parrot.upper()

## h. str()
"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print str(pi)

## i. Dot Notation
ministry = "The Ministry of Silly Walks"

print len(ministry)
ministry.upper()

## j. Printing Strings
"""Tell Python to print "Monty Python"
to the console on line 4!"""

print "Monty Python"

## k. Printing Variables
"""Assign the string "Ping!" to
the variable the_machine_goes on
line 5, then print it out on line 6!"""

the_machine_goes = "Ping!"
print the_machine_goes

## l. String Concatenation
# Print the concatenation of "Spam and eggs" on line 3!

print "Spam " + "and " + "eggs"

## m. String & Console Output
# Turn 3.14 into a string on line 3!

print "The value of pi is around " + str(3.14)

## n. String Formatting with %, Part 1
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)

s1 = "a"
s2 = "b"
print "testtest %s %s"  % (s1, s2)


"I am a {type}".format(type="string")
my_name = "Michael"

print "Hello, my name is {name}".format(name=my_name)

## o. String Formatting with %, Part2
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)

## p. Review : And Now, For Something Completely Familiar
# Write your code below, starting on line 3!

my_string = "abc"
print len(my_string)
print my_string.upper()


### 2) Date and Time
## a. The datetime Library
from datetime import datetime

## b. Getting the Current Date and Time
from datetime import datetime

now = datetime.now()

print now

## c. Extracting Information
from datetime import datetime

now = datetime.now()

print now
print now.year
print now.month
print now.day

## d. Hot Date
from datetime import datetime
now = datetime.now()

print "%s/%s/%s" % (now.year, now.month, now.day)

## e. Pretty Time
from datetime import datetime
now = datetime.now()

print "%s:%s:%s" % (now.hour, now.minute, now.second)

## f. Grand Finale
from datetime import datetime

now = datetime.now()

print "%s/%s/%s %s:%s:%s" % (now.year, now.month, now.day, now.hour, now.minute, now.second)

### 3) Python Strings
### 4) Basic String Operations




#### 3. Conditionals and Control Flow
### 1) Conditionals & Control Flow
## a. Go With the Flow
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()

## b. Compare Closely!
# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False


## c. Compare... Closelier
# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = False    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = False

# 1**2 <= -1
bool_three = False

# 40 * 4 >= -4
bool_four = True

# 100 != 10**2
bool_five = False

## d. How the Tables Have Turned
# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 3 == 4

# Make me true!
bool_three = 4<=6

# Make me false!
bool_four = 5>100

# Make me true!
bool_five = (4/2 == 2)

## e. To Be and/or Not to Be
"""
     Boolean Operators
------------------------      True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""

## f. And
bool_one = False and False # False
print(bool_one)

bool_two = -(-(-(-2))) == -2 and 4 >= 16**0.5 #false
print(bool_two)

bool_three = 19 % 4 != 300 / 10 / 10 and False #false
print(bool_three)

bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2 #true
print(bool_four)

bool_five = True and True #true
print(bool_five)


## g. Or
bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur' #True
print(bool_one)

bool_two = True or False #True
print(bool_two)

bool_three = 100**0.5 >= 50 or False #False
print(bool_three)

bool_four = True or True # True
print(bool_four)

bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1 #False
print(bool_five)

## h. Not
bool_one = not True #False
print(bool_one)

bool_two = not 3**4 < 4**3 #True
print(bool_two)

bool_three = not 10 % 3 <= 10 % 2 #True
print(bool_three)

bool_four = not 3**2 + 4**2 != 5**2 #True
print(bool_four)

bool_five = not not False   #False
print(bool_five)

## i. This and That (or This, But Not That!)

## j.
## k.


# 	2) PygLatin
# 	3) Conditionals and Loops
# 	4) Conditionals in Python
# 	5) Booleans







