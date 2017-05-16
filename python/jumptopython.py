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
# 2017.05.10 (Wed) pg 56~60
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

## 2.10 문자열 바꾸기 (replace (바뀌게될 문자열, 바꿀 문자열))
a510_9 = "Life is too short"
print a510_9.replace("Life", "Your leg") # 'Your leg is too short' Life 를 Your leg로 변경

## 2.11 문자열 나누기 (split)
a510_10 = "Life is too short"
print a510_10.split() # split with whitespace 

a510_10_1 = "a:b:c:d"
print a510_10_1.split(';') #';'를 기준으로 쪼개기

####################################
# 2017.05.11 (Wed) pg 60~pg 64
# 고급 무자열 포매팅
####################################

# 3. 고급 문자열 포매팅 [format]
## 3.1 숫자 바로 대입하기 (format) ->  "{0}".format(x) 를 이용하여 x값을 바로 안에 넣는다.
print "I eat {0} apples.".format(4) #I eat 4 apples

## 3.2 문자열 바로 대입하기
print "I eat {0} apples.".format("five") #I eat five apples.

## 3.3 숫자 값을 가진 변수로 대입하기
number511 = 5
print "I eat {0} apples." .format(number511) # I eat 5 apples.

## 3.4 2개 이상의 값 넣기
number511_1 = 10
day511 = "three"
print "I ate {0} apples. so I was sick for {1} days.".format(number511_1, day511)
# I ate 10 apples. so I was sick for three days

## 3.5 이름으로 넣기
print "I ate {number511_2} apples. so I was sick for {day511_1} days.".format(number511_2=1, day511_1 =3)
# I ate 1 apples. so I was sick for 3 days

## 3.6 인덱스와 이름을 혼용해서 넣기
print "I ate {0} apples. so I was sick for {day511_2} days.".format(10, day511_2 = 5)
# I ate 10 apples. so I was sick for 5 days

## 3.7 왼쪽 정렬 (:<x)
print "{0:<10}".format("hi") # 문자열왼쪽 정렬 나머지 정렬 

## 3.8  오른쪽 정렬
print "{0:>10}".format("hi") # 문자열을 오른쪽에 입력 후 나머지 정렬

## 3.9 가운데 정렬
print "{0:^10}".format("hi") # 문자열을 중간에 넣고 양쪽으로 같은 수 정렬

## 3.10 공백 채우기
print "{0:=^10}".format("hi") # 공백 문자 대신 =를 입력  ====hi====
print "{0:!<20}".format("hi") # 왼쪽 정렬 -> 문자열 이볅 -> 나머지 ! 로 채움 hi!!!!!!!!!!!!!!!!!!

## 3.11  소수점 표현하기
y511 = 3.42134234
print "{0:0.4f}".format(y511) # 0.4를 이용하여 소수점 4자리까지만 출력, 3.4213 
print "{0:10.4f}".format(y511) # 길이가 10개인 문자열에 0.4인데 소수점 자리수 를 오른쪽 끝에 삽입 후 공백 출력 -> '    3.4213'

## 3.12 { 또는 } 문자 표현하기
print "{{ and }}".format() #문자 그대로 사용하고 싶은 경우 {{ }}를 이용 -> "{ and }"


#======= pg63 ======= 
# 02-3 리스트 자료형 (List)
# 리스트는 어떠한 자료형도 포함가능하다. (java로 치면 array같은 느낌)
# 2-3-1리스트의 생성
# : 대괄호 []로 감싸주고 각 요소들은 쉼표로 구분 
#   리스트명 = [요소1, 요소2, 요소3, ...]
odd511 = [1, 3, 5, 7, 9] 
print odd511 # -> [1, 3, 5, 7, 9]

a511 = [ ] # 비어있는 리스트  
print a511  # -> []

b511 = [1, 2, 3] # 숫자를 요소로 가지고 있는 리스트
print b511 # -> [1, 2, 3]

c511 = ['Life', 'is', 'too', 'short'] # 문자열 요소로 하는 리스트
print c511 # ['Life', 'is', 'too', 'short']

d511 = [1, 2, 'Life', 'is']  # 숫자와 문자열을 함께 요소값으로 가지고 있는 리스트
print d511 # -> [1, 2, 'Life', 'is']

e511 = [1,2, ['Life', 'is']]  # 숫자와 리스트 자체를 요소값으로 가지고 있는 리스트 
print e511 # -> [1, 2, ['Life', 'is']]


# 2-3-2 : 리스트의 인덱싱과 슬라이싱
a511_1 = [1,2,3]
print a511_1 # -> [1,2,3]
print a511_1[0] # -> 1
print a511_1[0] + a511_1[2] #-> 1 + 3 = 4
print a511_1[-1] # -> 마지막 요소값 3 
print a511_1[-2] # -> 마지막에서 두 번째 요소값 2


####################################
# 2017.05.12 (Thurs) pg65~pg67
# 고급 무자열 포매팅
####################################
a512_1 = [1, 2, 3, ['a', 'b', 'c']]
print a512_1 # -> [1, 2, 3, ['a', 'b', 'c']]
print a512_1[0] # -> 1
print a512_1[-1] # -> ['a', 'b', 'c']
print a512_1[3] # ->  ['a', 'b', 'c']

# [2중 리스트에서 인덱싱 하기]
print a512_1[-1][0] #  -> a : 내부 리스트의 인덱스 요소 출력 [1, 2, 3, ['a', 'b', 'c']] 안에서 a를 출력하고 싶다.
print a512_1[-1][1] # -> b
print a512_1[-1][2] # -> c

# [3중 리스트에서 인덱싱 하기]
a512_2 = [1, 2, ['a', 'b', ['Life', 'is'] ] ] 
print a512_2[2][2][0] # -> 'Life'


## 리스트 슬라이싱 (나누기)
a512_3 = [1, 2, 3, 4, 5]
print a512_3[0:2] # -> [1,2]

#** 문자열 슬라이싱
a512_4 = "12345"
print a512_4[0:2] # -> '12'

a512_5 = [1, 2, 3, 4, 5]
b512_1 = a512_5[:2] #a512_5의 처음요소 부터 두번째 요소까지 [ a512_4[0], a512_4[1] ]
c512_1 = a512_5[2:] #a512_5의 두번째 요소부터 끝까지
print a512_4 # [1, 2, 3, 4, 5]
print b512_1 # [1, 2] 
print c512_1 # [3, 4, 5]


####################################
# 2017.05.14 (Sun) pg67
####################################

####################################
# 2017.05.15 (Mon) pg67~74
####################################

#중첩된 리스트에서 슬라이싱하기
a515_1 = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print a515_1[2:5] #2번째 요소부터 5-1 요소까지 -> [3, ['a', 'b', 'c'], 4]
print a515_1[3][:2] #3번째 요소 내부의처 처음에서 2-1까지 -> ['a', 'b']

## 리스트 연산자
## 1) 리스트 더하기 
a515_2 = [1,2,3]
b515_1 = [4, 5, 6]
print a515_2 + b515_1 # 요소별로 합친다 -> [1, 2,3,4,5,6]

## 2) 리스트 반복하기
a515_3 = [1, 2, 3]
print str(a512_3[2]) + "hi"  # 숫자 3을 문자 '3'으로 변환 후 연산 -> 3hi


# 리스트의 수정, 변경과 삭제
## 1. 리스트에서 하나의 값 수정하기
a513_4 = [1, 2, 3]
a513_4[2] = 4
print a513_4 # -> [1, 2, 4]

## 2. 리스트에서 연속된 범위의 값 수정하기
print a513_4[1:2] # -> [2]
a513_4[1:2] = ['a', 'b', 'c']
print a513_4 # -> ['1', 'a', 'b', 'c', '4']

## [리스트 수정할 때 주의할 점]
a513_4[1] = ['a', 'b', 'c']
print a513_4 #-> ['1', ['a', 'b', 'c'], 'b', 'c', '4']

## 3. [] 사용해 리스트 요소 삭제하기
a513_4[1:3] = [ ]
print a513_4 # 1요소에서 3-1까지 공백으로 만들기 -> [1, 'c', 4]

## 4. del 함수 사용해 리스트 요소 삭제하기
print a513_4 # -> [1, 'c', 4]
del a513_4[1] # 1번 요소 삭제
print a513_4 # -> [1, 4]


# 리스트 관련 함수들
## 1. 리스트에 요소 추가(append)
## : 덧붓이다, 첨부하다 예) append(x)는 리스트의 맨 마지막에 x를 추가하는 함수
a513_5 = [1,2,3]
a513_5.append(4)
print a513_5 # 리스트 뒤에 4를 추가한다. -> [1,2,3,4]

a513_5.append([5,6])
print a513_5 # -> 기존 리스트의 마지막에 [5,6] 추가 -> [1,2,3,4,[5,6]]  *리스트 모양으로 들어감

## 2. 리스트 정렬 (sort)
a513_6 = [1,4,3,2]
a513_6.sort()
print a513_6 # 리스트 내 숫자를 정렬 -> [1,2,3,4]

## 3. 리스트 뒤집기(reverse)
a513_7 = ['a', 'b', 'c']
a513_7.reverse()
print a513_7 # 리버스 -> ['c', 'b', 'a']

## 4. 위치 반환 (index)
a513_8 = [1,2,3]
print a513_8.index(3) # 요소값 3을 가지고 있는 숫자의 위치 리턴  -> 2
print a513_8.index(1) # 요소값 1을 가지고 있는 숫자의 위치 리터 -> 0
# print a515_8.index(0) # -> 0이라는 값이 없으니까 error를 뿜는다.

## 5. 리스트에 요소 삽입 (insert)
## insert(a, b) : a번째 위치에 b를 삽입하는 함수
a515_9 = [1,2,3]
a515_9.insert(0,4) # 0번째 자리에 4를 삽입 -> [4,1,2,3]
print a515_9
a515_9.insert(3,5) # 3번째 자리에 5를 삽입 -> [4,1,2,5,3]
print a515_9

## 6. 리스트 요소 제거(remove)
a515_10 = [1,2,3, 1, 2, 3]
a515_10.remove(3) # 리스트 내부에서 첫번째 나오는 값 제거
print a515_10 # [1,2,1,2,3]
a515_10.remove(3) # [1,2,1,2]
print a515_10 

## 7. 리스트 요소 끄집어내기 (pop)
a515_11 = [1,2,3]
print a515_11.pop() # 마지막 있는 3 리턴 후 요소 제거 -> 3
print a515_11 # [1, 2]

a515_12 = [1,2,3]
print a515_12.pop(1) # a515_12[1] 안의 요소 끄집어 내고 삭제하기 -> 2
print a515_12 # -> [1,3]

## 8. 리스트에 포함된 요소 x의 개수 세기(count)
a515_13 = [1,2,3,1]
print a515_13.count(1) # 1이 몇 개있는지 count  -> 2

## 9. 리스트 확장 (extend)
## : extend(x)에서 x에는 리스트만 올 수 있음.  원래 a 리스트에 X 리스트를 더함
a515_14 = [1,2,3]
a515_14.extend([4,5])
print a515_14 # [1,2,3]에 [4,5]를 추가해서 [1,2,3,4,5]가 됨
b515_2 = [6, 7]
a515_14.extend(b515_2) 
print a515_14 # [1,2,3,4,5]에 [6,7]를 확장해서 -> [1,2,3,4,5,6,7]



####################################
# 2017.05.16 (Tues) pg75
####################################
# 튜플 자료형
# 리스트와 다른 점 : 리스트는 [], 튜플은 ()
# 				: 리스트는 생성, 삭제, 수정 가능 / 튜플은 변경 불가

t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a', 'b', ('ab', 'cd'))

print t1 # -> ()
print t2 # -> (1,)
print t3 # -> (1, 2, 3)
print t4 # -> (1, 2, 3)
print t5 # -> ('a', 'b', ('ab', 'cd'))

