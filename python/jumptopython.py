
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
# L %% = Literal % (문자 % 자체)

# |Example|
print "I have %s apples" %3
print "rate is %s" %3.234 # rate is 3.234 -> 여기서 3.234는 string format으로 저장된다.

####################################
# 2017.05.09 (Tues) pg 55~56 
# 1. 문자열 포맷 코드
# 2. 포맷 코드와 숫자 함께 사용하기
# 내일 공부 : 2) 소수점 표현하기 부터 시작
####################################

#1. Formatting Operator (%d) 와 % 를 같이 사용할 때는 ---> %%
# 무슨 말이냐면 %라는 기호를 쓰고 싶은데 그 앞에 숫자는 바꾸고 싶음. 그런데 %d % 하면 인식을 못함 
# 파이썬 룰에 따라서 %d%%로 써줘야지 %d 가 % 뒤에 입력된 숫자를 입력 받음
# |Example|
# Wrong : "Error is %d%." % 98 
# Fixed : "Error is %d%%." %98 #Error is 98%.
print "Error is %d%%." % 95  #Error is 95%.

#2. 포맷 코드와 숫자 함께 사용하기
#1)정렬과 공백
print "%10s" % "hi" #'	hi' -> 이런식으로 hi 앞에 공백이 생긴채 출력된다.
# 통역 : 길이가 10개인 문자열에서 hi를 오른쪽에 정렬하고 나머지는 공백 즉, 10칸 중 2칸은 hi가 들어가있고 나머지 8칸은 비어있음

print "%-10sjane." % 'hi' #'hi        jane.' -> hi를 왼쪽 정렬, 나머지 공백


####################################
# 2017.05.10 (Wed) pg 56
# 소수점 표현하기
# 
# 내일 공부 : 
####################################
# 1. 소수점 표현
print "%0.4f" % 3.42134234 # 소수점 4번째 자리까지만 나타내고 싶은 경우 사용. -> 3.4213
print "%10.4f" % 3.42134234 # 소수점 4자리까지만 표현 및 10개 문자열 중 오른쪽 정렬 

# 2. 문자열 관련 함수들
## 2.1 무자 개수 세기 (count)
a510_0 = "hobby"
print a510_0.count('b') # b 의 개수를 a510라는 문자열에서 카운트 후 반환

## 2.2 위치 알려주기 (find)
a510_1 = "Python is best choice"
print a510_1.find('b') #b의 위치 출력 -> 10
print a510_1.find('k') #k의 위치 출력 * 만약에 없으면 -1 반환

## 2.3 위치 알려주기2 (index)
a510_2 = "Life is too short"
print a510_2.index('t') # 문자열 중 t가 제일 먼저 나온 위치 반환 -> 8, 없으면 오류 출력
#print a510_2.index('t')

## 2.4 문자열 삽입 (join)
a510_3 = ","
print a510_3.join('abcd') # 문자열 사이에 , 삽입 -> a,b,c,d 출력

## 2.5 소문자 -> 대문자 변환 (upper)
a510_4 = "hi"
print a510_4.upper() # HI

## 2.6 대문자 -> 소문자 변환 (lower)
a510_5 = "HI"
print a510_5.lower() # hi

## 2.7 왼쪽 공백 지우기 (lstrip)
a510_6 = " hi "
print a510_6.lstrip() # 'hi '

## 2.8 오른쪽 공백 지우기 (rstrip)
a510_7 = " hi "
print a510_7.rstrip() # ' hi'

## 2.9 양쪽 공백 지우기 (strip)
a510_8 = " hi "
print a510_8.strip() # 'hi'

## 2.10 무자열 바꾸기 (replace (바뀌게될 문자열, 바꿀 문자열))
a510_9 = "Life is too short"
print a510_9.replace("Life", "Your leg") # 'Your leg is too short' Life 를 Your leg로 변경

## 2.11 문자열 나누기 (split)
a510_10 = "Life is too short"
print a510_10.split() # split with whitespace 

a510_10_1 = "a:b:c:d"
print a510_10_1.split(';') #';'를 기준으로 쪼개기

# 3. 고급 문자열 포매팅


















