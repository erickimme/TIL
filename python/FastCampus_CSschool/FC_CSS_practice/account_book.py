import datetime

def adder(u_input):
    splited_u_input = u_input.split(',')
    purchased = splited_u_input[0]
    amount = splited_u_input[1]
    total = 0
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # text file
    # 1. write in text file
    # 1.1 first line (header)
    first_line = "| 일자 | 품목 | 가격 | 총액 |"
    text = "\n| {0} | {1} | {2} | {3}\n".format(now_time, purchased, amount, total)

    f_txt = open("/Users/kimeric/GitHubProjects/TIL/python/FastCampus_CSschool/FC_CSS_practice/dataset/accountBook.txt", 'a')
    f_txt.write(first_line)
    f_txt.write(text)
    f_txt.close

# 2. read text file

if __name__ == "__main__":
    u_input = input("소비내역을 입력하세요 (품목, 가격) : ")
    adder(u_input)

# TODO : 1) txt.file defaulting 2) sum of

# 추가하고 싶은 기능 : 함수의 호출 횟수
