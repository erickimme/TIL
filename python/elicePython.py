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



# 1주차 (4/17) 02 1강 1부 소개, 2부 실습 및 프로젝트: 너의 이름은
# 수업 내용 : 소개, 기본개념, 파이썬 입/출력, 프로젝트 : 자기소개

# 8 주차 목표를 세워 보아요!
#	1. 라이브 강의 빠지지 않기
#	2. 강의 10분 전/후 예습 및 복습
#	3. 파이썬의 문법과 이론 깔끔한 이해 (파이썬 문서를 쉽고 정확하게 읽을 수 있을 정도)
#	4. 프로그래밍 구현 가능
#	5. 천천히 깊게 생각하며 전진하기


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




