
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
# a[시작 번호: 끝 번호] 끝 번호는 포함되지 않음
aa = "Life is too short, You need Python"
bb_indexing = aa[0] + aa[1] + aa[2] + aa[3]
bb_slicing = aa[0:4]
print bb_indexing, bb_slicing	#Life Life
print aa[0:3] #Lif 0 <= aa < 3
print aa[:] # print from the beginning to the end
print aa[19:-7] # You need (from 19 to -7 ) don't include -7's index


### 2017.05.08
#split string by slicing
aaa = "20010331Rainy"
date = aaa[:8]
weather = aaa[8:]

print date #20010331
print weather #Rainey

aaaa = "20010331Rainy"
year1 = aaa[:4]
day1 = aaa[4:8]
weather1 = aaa[8:]
print year1 #2001
print day1 #0331
print weather1 #Rainy


## Pithon -> Python
aaaa = "Pithon"
print aaaa[1]
'i'
aaaa[:1]
'P'
aaaa[2:]
'thon'
print a[:1] + 'y' + a[2:] #Python

# String Formatting
print "I eat %d apples." %3 #I eat 3 apples.
print "I eat %s apples." % "five" #I eat five apples.

number = 10
print "I eat %d apples. " % number #I eat 10 apples

number1 = 100
day = "three"
print "I ate %d apples. so I was sick for %s days. " % (number1, day) # I ate 100 apples. so I was sick fro three days.

#String format codes
# %s = 문자열(String)
# %c = 문자1개 (character)
# %d = 정수(Integer)
# %f = 부동소수 (floating-point)
# %o = 8진수
# %x =  16진수
#L %% = Literal % (문자 % 자체)

# Examle)
print "I have %s apples" %3
print "rate is %s" %3.234 # rate is 3.024















