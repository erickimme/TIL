# -*- coding: utf-8 -*- 

# Author: eric kim
# Date : 2017-05-12

# Elice Python 코딩 유치원 - 파이썬 주중반 
# 강의 소개 
# 김재원 강사, 이제빈, 배휘동 조교 @월 20:00 
# 2017/4/17 ~ 6/11
# 주차별 커리큘럼
# 	1주차 : 너의 이름은 (4/17)
#	2주차 : 심리테스트 게임 (4/24)
# 	3주차 : 숫자 맞추기 게임 (5/1)
# 	4주차 : 출첵 프로그램	(5/8)
# 	5주차 : 미세먼지 데이터 분석 프로젝트 (5/15)
# 	6주차 : 지하철 공공데이터 분석 프로젝트 1 (5/22)
# 	7주차 : 지하철 공공데이터 분석 프로젝트 2 (5/29)
# 	8주차 : 개인 프로젝트 (6/11)
# 
# 화면 세팅 : 와이드 모드 로 강의 와 코드 작성을 동시에 진행 (개이득)
# 도움 요청 : 막히면 질문 (개이득) -> 추후 질문은 헬프 센터로 이동
# 샌드박스 : 온라인 코딩 에디터 main.py (실습) + note.txt (필기)
# main.py : 단축키 (ctrl + shift + enter)

################################################################
#0주차  : 01 강의 미리보기 
# 1. 테스트 코드 (지하철 분석 프로그램)
'''
import csv
import matplotlib.pyplot as plt
import elice_utils

data = csv.reader(open('./data/subway_2016.csv','r'),delimiter=",")

인원1 = []
인원2 = []
역이름1 = '신림'
호선1 = '2호선'
역이름2 = '강남'
호선2 = '2호선'

for row in data : #데이터 파일을 이터레이트하면서
    if(row[1] == 역이름1 and row[0] == 호선1):  
        #row 리스트의 2번째 요소가 신림이고  row 리스트이 1번째 요소가 2호선이면
        인원1 = row[2:] # 인원1의 리스트에 2번째요소로 입력 ?!  [신림, 2호선, 인원1]
    if(row[1] == 역이름2 and row[0] == 호선2): # 강남이고, 2호선이면
        인원2 = row[2:] # 인원2의 리스트의 2번째부터 입력 [강남, 2호선, 인원2]
    
승차1 = 인원1[::2] #승차1은 인원 1의 2번재 꺼
하차1 = 인원1[1::2] #하차1은  ??

승차2 = 인원2[::2]
하차2 = 인원2[1::2]

import matplotlib.font_manager as fm # matplot library -> 폰트매니저 불러와서 fm이라고 설정
font = fm.FontProperties(fname='./NanumBarunGothic.ttf') # 폰트 나눔고딕 설정
 
labels = []  #라벨이라는 이름의 리스트 생성
x = [] #x라는 이름의 리스트 생성
for i in range(4,28): # 숫자 4 에서 27까지 루프 도는 범위 설정
    labels.append(str(i)+'시') # 라벨 리스트의 값의 마지막 + 시
    x.append(i) # i append 하기
    
plt.xticks(x, labels,rotation='vertical', fontproperties=font) #수직으로 로테이션
plt.plot(x,승차1,'r', label=역이름1+'역 승차') #승차1은 레드 실선으로 표시
plt.plot(x,승차2,'b', label=역이름2+'역 승차') #승차2는 블루 실선으로 표시
plt.ylim(ymax=420000)

plt.xticks(x, labels,rotation='vertical')
plt.plot(x,하차1,'r--', label=역이름1+'역 하차') #하차는 -- (점선으로 표시) 하차1은 빨간색
plt.plot(x,하차2,'b--', label=역이름2+'역 하차') # 하차2는 블루 점선으로 표시
plt.ylim(ymax=420000)

plt.title(역이름1+'역 승하차 인원 vs '+역이름2+'역 승하차 인원  \n # 2016년 6월 티머니카드 제공 데이터', fontproperties=font) #타이틀 설정
plt.legend(prop=font) #레전드 설정

plt.savefig("image.svg", format="svg") # figure 를 이미지로 저장
elice_utils.send_image("image.svg") #이미지 전송
'''


################################################################
# 1주차 (4/17) 02 1강 1부 소개, 2부 실습 및 프로젝트: 너의 이름은
# 수업 내용 : 소개, 기본개념, 파이썬 입/출력, 프로젝트 : 자기소개
################################################################
# 8 주차 목표를 세워 보아요!
#	1. 라이브 강의 빠지지 않기
#	2. 강의 10분 전/후 예습 및 복습
#	3. 파이썬의 문법과 이론 깔끔한 이해 (파이썬 문서를 쉽고 정확하게 읽을 수 있을 정도)
#	4. 프로그래밍 구현 가능
#	5. 천천히 깊게 생각하며 전진하기
################################################################

# 프로그래밍 기본 개념
# 파이선의 입출력
# 입력 : input()
# 출력 : print('abcdefg')


# 실습문제 1 : Hello Elice! =================================
'''
print("Hello Elice!")
'''

# 실습문제 2 : 코멘트/주석 =================================
'''
# ‘#’으로 시작하는 이 문장은 컴퓨터는 인식하지 못하고 여러분만 보실 수 있습니다!
# 자 드시고 싶은 야식을 보이지 않게 써볼까요?

print("밥")
print("치킨")
print("피자")  #피자도 좋다
print("치즈케이크") #치즈케이크가 좋다
'''

# 실습문제 3 : 당근 입력! =================================
'''
#당근 주세요
food = input()

#진짜 당근 준거 맞죠?
print('무엇을 주셨나요?')
print(food)
'''

# 실습문제 4 : 에러 =================================
food = input('음식을 주세요: ')
print(food, '맞죠?')

food1 = input('당근 말고 밥을 주세요 : ')
print(food1, '맞나요?')

# 실습문제 5 : 자기 소개서 =================================
'''
# 아래에 ‘이름, 직업, 취미, 하고 싶은 것, 가고 싶은 곳’ 이라는 문장을 출력하고,
# 각각 name, occupation, hobby, to_do, place 라는 저장 공간에 저장해주세요.

print('이름이 뭔가요?')
name = input()

print('직업이 몬가요?')
occupation = input()

print('전화번호가 몬가요?')
phonenum = input()

print('취미가 몬가요?')
hobby = input()

print('하고 싶은 것 몬가요?')
to_do = input()

print('가고 싶은 곳 몬가요?')
place = input()

print (name, occupation, phonenum, hobby, to_do, place)

print ("이름 : {0} \n 직업 : {1} \n 전화번호 : {2} \n 취미 : {3} \n 하고싶은 것 : {4} \n 가고싶은 곳 : {5}".format(name, occupation, phonenum,hobby, to_do, place ))


# 엘리스가 자동으로 파일로 저장해드립니다. 바꾸지 말아주세요!
import elice_utils
with open('intro.txt', 'w') as fout:
    fout.write('이름: ' + name + '\r\n')
    fout.write('직업: ' + occupation + '\r\n')
    fout.write('취미: ' + hobby + '\r\n')
    fout.write('하고 싶은 것: ' + to_do + '\r\n')
    fout.write('가고 싶은 곳: ' + place + '\r\n')
elice_utils.send_file('intro.txt')
'''



#################################################################
# 2강 1부 : 나이, 채팅 프로그램
# 처리 - 1.연산, 2.논리구조 
# 1. 연산
#	1) 산술 연산 : +, -, *, /, //(내림정수), %(나머지), **(지수)
#	2) 비교 연산 : 
#	3) 논리 연산
#
# 2. 논리구조 
#	1) 순차 구조
#	2) 선택 구조
#	3) 반복 구조
#
#
#
#
#
#
################################################################

## 실습
# ===============계산하기=====================================
'''
print(5+7) # 1+4의 결과 출력
print(12*3) # 10*3의 결과 출력
print(36-11) # 14-42의 결과 출력
print(25/5) # 12/3의 결과 출력

# 일단 실행해본뒤
# 숫자와 연산 기호를 바꾸어가면서 실행해 보아요
'''



# 계산하기 : 더치페이========================
'''
# 실행을 해보세요. 에러가 발생합니다.
# 아래 주석과 코드를 읽어보면서 미완성인 코드를 완성해 보아요.
pork = 9000 # 삼겹살 1인분에 9천원
fried_rice = 4000 # 볶음밥 1인분에 4천원

# 삼겹살 4인분, 볶음밥 2인분의 총 금액을 계산하여, totalprice에 저장해 보아요.
# 더하기 +, 곱하기 *를 사용하세요 (곱하기는 키보드에서 SHIFT + 8을 누르면 됩니다.)
total_price = pork*4 + fried_rice*2
# 친구와 둘이 나누어 내야할 금액을 계산하여, dutchpay에 저장해 보아요.
# 나누기를 사용하세요.
dutchpay = total_price/2

# 결과 확인을 위해서 지난 시간에 배운 출력방법을 떠올려 두개의 아래 출력문을 완성해 보아요.
# totalprice를 출력해 보아요
print('총 금액은 ',total_price, '원 입니다.')
# dutchpay를 출력해 보아요
print('각자 내야할 금액은 ', dutchpay, '원 입니다.')
'''

# ===========더치페이 계산 프로그램 ============
'''
# 실행을 해보세요. 에러가 발생합니다.
# 아래 주석과 코드를 읽어보면서 미완성인 코드를 완성해 보아요.
pork = 9000 # 삼겹살 1인분에 9천원
fried_rice = 4000 # 볶음밥 1인분에 4천원

# 입력 부분 (그대로 두세요)
pork_count = int(input('삼겹살은 몇인분 드셨나요?:')) #삼겹살 먹은 양을 입력 받기
fried_rice_count = int(input('볶음밥은 몇인분 드셨나요?:')) #볶음밥 먹은 양을 입력 받기
number_of_people = int(input('몇명이 드셨나요?:')) #함께먹은 사람수 입력 받기

# 여기서부터 수정하세요.
# pork, pork_count, fried_rice, fried_rice_count를 사용하여 전체 금액을 계산해 보세요.
# print(fried_rice)
# print(pork)
# print(pork_count)
# print(fried_rice_count)
# print(number_of_people)

total_price = pork_count*pork + fried_rice_count*fried_rice
# print(total_price)

# number_of_people를 사용하여 더치페이해야할 금액을 계산해 보세요.
dutchpay = total_price/number_of_people

# 결과 확인을 위해서 지난 시간에 배운 출력방법을 떠올려 아래 출력문을 완성해 보아요.

# 삼겹살 먹은양, 볶음밥 먹은양, 함께 먹은 사람수를 출력해 보아요
# pork_count, fried_rice_count, number_of_people를 사용하세요.
print('삼겹살 ', pork_count,'인분, 볶음밥 ', fried_rice_count,'인분을 ', number_of_people,'명이 드셨네요.')

# total_price를 출력해 보아요
print('총 금액은 ', total_price, '원 입니다.')

# dutchpay를 출력해 보아요
print('각자 내야할 금액은 ', int(dutchpay), '원 입니다.')
'''

#===============나이 질문하기 ========================
'''
age = input('너의 나이는? ')
print(type(age))


########## 출력값 ###########
# 너의 나이는? 12
# <class 'str'>
'''


# =============나이 출력하기 ========================
# input() 함수는 '문자열(string)' 으로 저장됨 -> 그래서 숫자형으로 바꿔주는 작업이 필요
'''
age = int(input('너의 나이는? '))

print('정말? ', age - 5, '살 인줄 알았어~~~~~')
'''



# ===============나이 채팅 프로그램============================
'''
# 나이를 입력 받습니다.
age = int(input('너의 나이는? '))

# 나이의 10% 적게 말하되, 정수로 출력합니다.


# 사용자가 진심이라고 느낄 수 있도록 적절한 표현을 사용합니다.
print('왜이렇게 어려보여?', age*0.9, '인줄알았어')
'''



### 2017.05.15 - 5강






# 5강 1부 : 복습
'''
#구구단을 외우자
for i in range(2,10):
    for j in range(1,10):
        print (i, 'X', j, '=', i*j, end='\t')
    print()   #print(end='\n')


# i j
# 2 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t \n
# 3 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t \n
# 4 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t \n
# 5 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t \n
# 6 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t \n
# 7 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t \n
# 8 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t \n
# 9 1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t \n
'''

# 하얀토끼의 채점
'''
score = [85, 0, 35, 43, 50, 95, 84, 4, 6, 88, 61, 71, 73, 0, 15, 68, 53, 17, 83, 84, 0, 81, 38, 96, 47, 99, 49, 34, 46, 26, 23, 36, 9, 37, 93, 81, 67, 51, 90, 51, 0, 31, 43, 5, 85, 77, 0, 38, 27, 8, 66, 78, 56, 64, 70, 30, 100, 0, 62, 99, 97, 79, 51, 12, 28, 72, 22, 0, 41, 78, 27, 0, 17, 14, 0, 6, 87, 42, 85, 90, 71, 62, 0, 63, 25, 63, 2, 55, 46, 92, 87, 25, 0, 9, 67, 15, 13, 33, 60, 25]

#100명의 점수 

result = [0, 0, 0]


###아래 score에 저장된 점수를 확인해서 result에 미응시자, 합격자, 불합격자 수를 차례로 저장하는 코드를 작성해 보세요
# 복습
# # score 의 갯수 -> len
# print(len(score)) # -> 100

# # 리스트 내 특정 index 출력
# print(score[99]) # -> 60

# #슬라이싱 #2~5번째 (1:5)
# print(score[1:5]) # 2번째는 1,  0 1 2 3 4 -> [ 0, 35, 43, 50)]
# print(score[-2]) # -> 60 

# print(score[-2:]) # 뒤에서 2번째에서  끝까지 -> [60, 25]
# print(score[:-2]) # 맨앞에서 뒤에서 2번쨰-1까지



#count_non = 0
#count_pass = 0
#count_fail = 0
for i in range(0, len(score)): #for i in score
    if score[i] == 0: # 미응시자
#        count_non += 1 # result 1을 증가시킨다.
        result[0] += 1#count_non
    elif score[i] >= 80:
#        count_pass += 1
        result[1] +=1 #count_pass
    elif score[i] < 80:
#        count_fail += 1
        result[2] += 1 #count_fail

print(result) # -> [11, 21, 68]
'''



# ===========5강 1부 가위바위보 1==============
'''
# random.randrange() 함수를 이용하기 위해 random 모듈 불러오기
import random

# 숫자를 입력 받습니다. 여기서 문자 데이터 타입을 int()를 이용하여 숫자로 바꿉니다.
user = int(input("가위 - 0, 바위 - 1, 보- 2 를 선택해주세요: "))
if user == 0:
    print("당신은 가위를 냈습니다")
elif user == 1:
    print("당신은 바위를 냈습니다")
elif user == 2:
    print("당신은 보를 냈습니다")

# 랜덤 숫자를 저장합니다.
rabbit = random.randrange(0,3) #0,1,2 출력
if rabbit == 0:
    print("토끼는 가위를 냈습니다")
elif rabbit == 1:
    print("토끼는 바위를 냈습니다")
else:
    print("토끼는  보를 냈습니다")
    
# 조건문을 사용하여 이겼는지 졌는지 비겼는지 출력합니다.
if user == rabbit: #
    print("비겼습니다!")
elif user == 0: #가위 (0)
    if (rabbit == 1): # 바위(1)
        print("졌습니다!")
    elif(rabbit == 2):   # 보(2)
        print("이겼습니다!") 
elif user == 1: #바위 (1)
    if (rabbit == 0): # 가위(0)
        print("이겼습니다!")
    elif(rabbit == 2):   # 보(2)
        print("졌습니다!")
elif user == 2: #보 (2)
    if (rabbit == 0): # 가위(0)
        print("졌습니다!")
    elif(rabbit == 1):   # 바위(1)
        print("이겼습니다!")     


# TA님
if user == rabbit:
    print("비겼습니다!")
else:
    if (user == 0 and rabbit ==2) or (user == 1 and rabbit 0) or (user == 2 and rabbit == 1):
        print("이겼습니다")
    else:
        print("졌습니다!")


# 김현진님
if user == rabbit:
    print("비겼습니다!")
elif user - rabbit == 1 or user - rabbit == -2:
    print("이겼습니다!")
else:
    print("졌습니다!")
'''

#=================== 가위바위보 2 ===================
'''
# random.randrange() 함수를 이용하기 위해 random 모듈 불러오기
import random

while True:
# 가위, 바위, 보 중에 하나를 입력 받습니다.
    user = input("가위, 바위, 보 를 선택해주세요: ")
    print("user:", user)
# 잘못된 입력에 에러를 출력합니다.
    if(user == "가위" or user == "바위" or user == "보"):
        break
    else:
        print("잘못된 입력입니다! 가위, 바위, 보 중에 선택해주세요.")

# 랜덤 숫자를 저장합니다.
rock_paper_scissors = ["가위", "바위", "보"]
rabbit = random.choice(rock_paper_scissors)
print("rabbit:", rabbit)

# 조건문을 사용하여 이겼는지 졌는지 비겼는지 출력합니다.
if user == rabbit:
    print("비겼습니다!")
else:
    if(user == '가위'and rabbit == '보') or (user == '바위' and rabbit == '가위') or (user == '보' and rabbit == '바위'):
        print("이겼습니다!") 
    else:
        print("졌습니다!")
'''


# =================== 가위바위보 3 ===================
# random.randrange() 함수를 이용하기 위해 random 모듈 불러오기
import random

# 몇 번 이겼는지 win에 저장하고, 몇 번 졌는지 lose에 저장합니다.
win = 0
lose = 0

# 숫자를 입력 받습니다. 여기서 문자 데이터 타입을 int()를 이용하여 숫자로 바꿉니다.
user = int(input("가위 - 0, 바위 - 1, 보- 2 를 선택해주세요: "))

# 랜덤 숫자를 저장합니다.
rabbit = random.randrange(0,3)

# 조건문을 사용하여 이겼는지 졌는지 비겼는지 출력합니다.
if user == rabbit:
    print("비겼습니다!")
else:
    print("이겼습니다!")
    print("졌습니다!")

# 삼세판 후 이겼는지 졌는지 비겼는지 출력합니다.
print("삼세판 후 최종 우승!")
print("삼세판 후 탈락!")
print("삼세판 후에도 비김!")


# ==================== 5강 2부 ====================
# ====== 목표 읽어오기 1 ====
'''note.txt
8 주차 목표를 세워 보아요!
1. 라이브 강의 빠지지 않기
2. 강의 10분 전/후 예습 및 복습
3. 파이썬의 문법과 이론 깔끔한 이해 (파이썬 문서를 쉽고 정확하게 읽을 수 있을 정도)
4. 프로그래밍 구현 가능
5. 천천히 깊게 생각하며 전진하기
'''

'''main.py
# 파일을 불러옵니다.
f = open('note.txt')

# 파일을 읽습니다.
goal = f.read()

# 파일을 출력합니다.
print(goal)
'''


# ======= 목표 읽어오기 2 =======
'''
# 파일을 불러옵니다.
f = open('note.txt')

# 파일을 읽습니다.
goals = f.readlines() #줄바꿈 형태로 리스트로 가져옴

# 파일을 출력합니다.
for goal in goals:
    if goal != '\n':
        print("[ ]", goal, end='')
    # print(goal)
    else:
        print(goal, end = '')


# s = open('note.txt').read() #  한번에
'''



# ====CSV 읽어오기====
''' main.py
import csv

#csv module 안의 reader라는 함수를 호출
data = csv.reader(open('example.csv')) 

for row in data:
    print(row)
'''

''' example.csv
2017-05-01,test1,1
2017-05-02,test2,2
2017-05-03,test3,3
2017-05-04,test4,4
2017-05-05,test5,5
2017-05-06,test6,6
2017-05-07,test7,7
2017-05-08,test8,8
2017-05-09,test9,9
'''


'''
import csv

#csv module 안의 reader라는 함수를 호출
data = csv.reader(open('example.csv')) 

for row in data:
    print(row[0])

2017-05-01
2017-05-02
2017-05-03
2017-05-04
2017-05-05
2017-05-06
2017-05-07
2017-05-08
2017-05-09
'''

'''
row[2] 합치기
import csv

#csv module 안의 reader라는 함수를 호출
data = csv.reader(open('example.csv')) 
total = 0

for row in data:
    total += int(row[2])
    print(row[2])
print(total) # -> 45
'''



# ==== CSV 읽어오기 2 ====
'''
import csv

data = csv.reader(open('SNAP.csv'), delimiter = '\t', quotechar = '|') # delimeter : 열 구분

# spamReader = csv.reader(open('eggs.csv'), delimiter=' ', quotechar='|')

count = 0
total = 0
for row in data:
    if row[-2] != 'Adj Close':
        print(row[-2])
        total += float(row[-2])
        count += 1

price = total/count
print(price)

#open : 마켓 시작 가격
# adj-close : 평균가격
'''