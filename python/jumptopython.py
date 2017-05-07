
# -*- coding: utf-8 -*- 



# python practice_jumpToPython.py

#Author: eric kim
#Date : 2017-03-21



print("Hello World")

# ""
food = "Python's favorite food is perl"
print food

# ''
say = '"Python is very easy." he says.'
print say

# \
food1 = 'Python\'s favorite food is perl'
say1 = "\"Python is very easy.\" he says."

print food1, say1


multiline = "Life is too short\nYou need python"
print multiline


multiline1 = '''
	Life is  too short
	You need python
	'''
print multiline1

multiline2 = """
	Life is too short
	You need python
	"""
print multiline2


# ESCAPE CODE

# Concatenation Operation
## Addition
head = "Python"
tail = " is fun!"
print head + tail #Python is fun!

## Multiply
a = "python"
print a * 2  #'pythonpython'


## Multiply application
print("=" * 50)		#==================================================
print("My Program")	#My Program
print("=" * 50)		#==================================================


## String Indexing (가리키기) & Slicing (잘라내기)
### Indexing
aa = "Life is too short, You need Python"
     #0123456789012345678901234567890123
     #0       1       2        3  
print aa[0], aa[1], aa[2], aa[3], aa[12], aa[20] # L, i, f, e, s, o
print aa[-1], aa[-2], aa[-5] # n, o , y 뒤에서 부터 읽음 *0부터 시작하지 않는 까닭은 +0 == -0


### Slicing
aa = "Life is too short, You need Python"
bb_indexing = aa[0] + aa[1] + aa[2] + aa[3]
bb_slicing = aa[0:4]
print bb_indexing, bb_slicing	#Life Life






