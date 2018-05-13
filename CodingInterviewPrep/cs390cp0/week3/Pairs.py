#!/usr/bin/py
# Head ends here
'''
import itertools
def pairs(a,k):
    # a is the list of numbers and k is the difference value
    a.sort()
    print("a:", a)
    answer = 0
    # for a, b in itertools.combinations(a, 2):
    #     if abs(a - b) == k:
    #         answer += 1

    for i in a:
        target = i + k
        print("target: ", target)

        if target in a:
            answer += 1
    return answer

# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    print("a:", a)
    a = list(map(int, a.split(' ')))
    print("a in list:", a)
    _a_size=a[0]
    _k=a[1]
    print("_k:", _k)
    b = input().strip()
    print("b:", b)
    b = list(map(int, b.split(' ')))
    print("b in list:", b)
    print(pairs(b,_k))
'''
# 5 2
# 1 5 3 4 2


def main():
    return
    # a_split = a.split()
    # print(a_split)
    # n = [int(x) for x in input().split()]
    # arr = [int(x) for x in input().split()]
    # diff=n[1]
    # pair=0
    # sarr=set(arr)
    # for e in sarr:
    #     if e-diff in sarr:
    #        pair+=1

    # print(pair)


def pairs(n,k):
    pair_cnt = 0
    print(type(k))
    set_n = set(k)
    print("set_n: " + str(set_n))

    for ele in set_n:
        print("ele: " + str(ele) + str(type(ele)))
        print("ele-diff: " + str(ele - diff))
        if ele - diff in set_n:
            pair_cnt += 1

    print("pair_cnt: " + str(pair_cnt))
    return pair_cnt

# main()
if __name__ == '__main__':
    a = input().strip()  # string type
    print(a)
    a_split = a.split() # list type
    print("a_split:" + str(a_split))

    n = []
    for x in a_split:
        n.append(int(x))
    print("n: " + str(n))
    # n_listComp = [int(x) for x in a_split]
    # print(n_listComp)

    diff = n[1]
    print("diff: " + str(diff))


    b = input().strip()
    b_split = b.split()
    print("b_split:" + str(b_split))

    k = []
    for x in b_split:
        k.append(int(x))
    print("k: " + str(k))
    # k_listComp = [int(x) for x in b_split]
    # print("k_listComp: " + str(k_listComp))
    pairs(n, k)









