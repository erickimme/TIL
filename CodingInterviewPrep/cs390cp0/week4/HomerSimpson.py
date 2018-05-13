# '''
# Homer Simpson likes eating Krusty-burgers.
# It takes Homer m minutes to eat a Krusty-burger.
# However, there’s a new type of burger in Apu’s Kwik-e-Mart.
# Homer likes those too. It takes him n minutes to eat one of these burgers.
# Given t minutes, you have to find out the maximum number of burgers Homer can eat without wasting any time.
# If he must waste time, he can have beer.
#
# Input Format
# Input consists of several test cases. Each test case consists of three integers m, n, t.
#
# Constraints
# 0 < m, n, t < 10000
#
# Output Format
# For each test case, print in a single line the maximum number of burgers Homer can eat without having beer.
# If homer must have beer, then also print the time he gets for drinking, separated by a single space.
# It is preferable that Homer drinks as little beer as possible.
#
# Sample Input 0
#
# 3 5 54
# 3 5 55
#
# Sample Output 0
# 18
# 17
#
# Sample Input 1
# 17 18 99
# 435 159 4568
# 1 1 1
# 10 87 555
# 34 657 189
# 999 99 6544
# 10 100 1000
# 1000 10 1
# 54 65 98
# 6 4 21
# 3 7 1000
# 103 103 465
# 485 173 6548
# 6465 555 1551
# 34 7878 8484
# 321 456 9877
#
# Sample Output 1
# 5 9
# 20 8
# 1
# 17
# 5 19
# 57 1
# 100
# 0 1
# 1 33
# 5 1
# 332
# 4 53
# 18 2
# 2 441
# 249 18
# 24 13
# '''
#
# '''
# def calMaxDonutMinBeerTime(m, n, t):
#     max_bur_time = max(m, n) # 18 #5
#     min_bur_time = min(m, n) # 17 #3
#     print("max_bur_time: " + str(max_bur_time))
#     print("min_bur_time: " + str(min_bur_time))
#
#     max_bur_num = int(t/min_bur_time) # 99 / 18 = 5, remainder = 9 | # 54 = 10*5 + 4 => 10
#     min_bur_num = int(t/max_bur_time) # 99 / 17 = 5, remainder = 14 | # 54 = 18*3 + 0 => 18
#     print("max_bur_num: " + str(max_bur_num))
#     print("min_bur_num: " + str(min_bur_num))
#
#     # formula
#     # 0 < rangeBurNum_from_minBurtime < 18
#     # 0 < rangeBurNum_from_maxBurtiem < 10
#
#     # totalTimeEatDonut
#     # BeerTime = t-TotalTimeEatDonut
#     # Min_beerTime
#     # Max_totalBurger
#     list_bt = []
#     list_tb = []
#     for i in range(min_bur_num+1): # 10
#         # print("")
#         for j in range(max_bur_num+1): # 18
#             totalTimeEatDonut = i*min_bur_time + j*max_bur_time
#             beerTime = t - totalTimeEatDonut
#             totalBurger = i+j
#
#             if beerTime >= 0:
#                 list_bt.append(beerTime)
#                 list_tb.append(totalBurger)
#             print("list_bt: " + str(list_bt))
#             print("list_tb: " + str(list_tb))
#             print(len(list_bt), len(list_tb))
#
#             # print("i: " + str(i) + " j: " + str(j) + " totalTimeEatDonuts: " + str(
#             #     totalTimeEatDonut) + " beerTime: " + str(
#             #     beerTime) + " min_beerTime: " + str(min_beerTime) + " totalBurger: " + str(totalBurger))
#             #
#             # if (beerTime <0):
#             #     # print("i: " + str(i) + " j: " + str(j) + " totalTimeEatDonuts: " + str(
#             #     # totalTimeEatDonut) + " beerTime: " + str(
#             #     # beerTime) + " min_beerTime: " + str(min_beerTime) + " totalBurger: " + str(totalBurger))
#             # else:
#             #     if beerTime < min_beerTime:
#             #         min_beerTime = beerTime
#             #         list_min_bt.append(beerTime)
#             #         # print("i: " + str(i) + " j: " + str(j) + " totalTimeEatDonuts: " + str(
#             #         #     totalTimeEatDonut) + " beerTime: " + str(
#             #         #     beerTime) + " min_beerTime: " + str(min_beerTime) + " totalBurger: " + str(totalBurger))
#
#             # if beerTime < min_beerTime:
#             #     min_beerTime = beerTime
#             # if beerTime < 0 and min_beerTime > 0:
#             #     min_beerTime = beerTime
#             #     print("totalburger: " + str(i+j) + " min_beertime: " + str(min_beerTime)+"\n")
#             #
#             # elif beerTime >= 0 and beerTime < min_beerTime:
#             #     min_beerTime = beerTime
#             #     if min_beerTime == 0:
#             #         print("max_bur_num: " + str(i+j)) # max bur number
#
#     min_beerTime = min(list_bt)
#         # print("min_beerTime: " + str(min_beerTime)) # 9
#         # print("index_min_bt: " + str(list_bt.index(min_beerTime))) # 5
#     max_totalBurger = list_tb[list_bt.index(min_beerTime)]
#         # print("max_totalburger: " + str(max_totalBurger))
#     print(max_totalBurger, min_beerTime)
#
#
# def main():
#     n = ' '
#     array = []
#     # while n != "":
#     #     n = input().strip()
#     #     print("n: " + str(n))
#     #     n.split()
#
#         # for x in n.split():
#         #     array.append(x)
#         #     print(array)
#         # array = [int(x) for x in input().split()]  # str
#         # print("array: " + str(array))
#
#     m = 435
#     n = 159
#     t = 4568
#     calMaxDonutMinBeerTime(m, n, t)
#     # ''' w/o list comprehension
#     # input_array = input().split()
#     # array = []
#     # for a in input_array:
#     #     array.append(int(a))
#     # print(array)
#     '''
#
# main()
# '''
#
# ''' C++
# int
# main()
# {
# / * Enter
# your
# code
# here.Read
# input
# from STDIN.Print output
#
# to
# STDOUT * /
#
# int
# m_time, n_time, t_time;
# int
# max_m_num, max_n_num;
#
# while (cin >> m_time) {
# cin >> n_time >> t_time;
#
# max_m_num = t_time / m_time;
# max_n_num = t_time / n_time;
#
# int max_m_n = 0;
# bool hasBeerTime = false;
# for (int i = max_m_num; i >= 0; i—) {
# for (int j = max_n_num; j >= 0; j—) {
# if (i * m_time + j * n_time == t_time) {
# if (max_m_n < i + j) {
# max_m_n = i + j;
# hasBeerTime = true;
# }
# }
# }
# }
#
# if (hasBeerTime == true) {
# cout << max_m_n << endl;
# }
# else {
#
# int min_beer_time = 100000;
# int curr_beer_time = 0;
# int min_beer_m = max_m_num;
# int min_beer_n = max_n_num;
#
# for (int i = max_m_num; i >= 0; i—) {
# for (int j = max_n_num; j >= 0; j—) {
#
# curr_beer_time = t_time - (i * m_time + j * n_time);
#
# if (0 < curr_beer_time & & curr_beer_time <= min_beer_time) {
# if (curr_beer_time == min_beer_time) {
# if (min_beer_m + min_beer_n < i+j) {
# min_beer_time = curr_beer_time;
# min_beer_m = i;
# min_beer_n = j;
# }
# } else {
# min_beer_time = curr_beer_time;
# min_beer_m = i;
# min_beer_n = j;
# }
#
# }
# }
# }
# cout << min_beer_m + min_beer_n << " " << min_beer_time << endl;
# }
# }
#
# return 0;
# }
# '''
#
#
# def calMaxDonutMinBeerTime(m, n, t):
#     higher_v = max(m, n)
#     lower_v = min(m, n)
#     max_burg = int(t / lower_v)
#     min_burg = int(t / higher_v)
#     b_times = []
#     beerTime = t - max_burg * lower_v
#     k = 0
#     lb_temp = 0
#     hb_temp = 0
#     max_b = 0
#     min_t = t
#     for i in range(max_burg, -1, -1):
#         lb_temp = i
#         for j in range(min_burg + 1):
#             hb_temp = j
#             beerTime = t - ((i * lower_v) + (j * higher_v))
#             if beerTime >= 0:
#                 if beerTime < min_t:
#                     min_t = beerTime
#                     max_b = lb_temp + hb_temp
#                 elif beerTime == min_t:
#                     if lb_temp + hb_temp > max_b:
#                         max_b = lb_temp + hb_temp
#             else:
#                 break
#
#     if min_t == 0:
#         print(max_b)
#     else:
#         print(max_b, min_t)
#
#
# def main():
#     while True:
#         str = input()
#         if str == '':
#             break
#         else:
#             inp = [int(x) for x in str.split()]
#             m = inp[0]
#             n = inp[1]
#             t = inp[2]
#             calMaxDonutMinBeerTime(m, n, t)
#
#
# main()
#
