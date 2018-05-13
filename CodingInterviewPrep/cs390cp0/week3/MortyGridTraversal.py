#!/usr/bin/env python3
final=[]
def srch(arr,orig_s,x,y,pos,copy,temp):
    n=len(arr)
    if pos == n:
        f_call(temp)
        return True
    c=orig_s[pos]
    if(x+1 < n):
        if arr[x+1][y]==c:
            copy+=c
            temp.append(converter_2d1d(x+1,y,n))
            if srch(arr,orig_s,x+1,y,pos+1,copy,temp):
                return True
    if (x - 1 >=0):
        if arr[x - 1][y] == c:
            copy += c
            temp.append(converter_2d1d(x-1 , y, n))
            if srch(arr, orig_s, x - 1, y, pos + 1, copy,temp):
                return True
    if (y + 1 < n):
        if arr[x][y+1] == c:
            copy += c
            temp.append(converter_2d1d(x, y+1, n))
            if srch(arr, orig_s, x , y+1, pos + 1, copy,temp):
                return True
    if (y - 1 >= 0):
        if arr[x][y-1] == c:
            copy += c
            temp.append(converter_2d1d(x, y-1, n))
            if srch(arr, orig_s, x , y-1, pos + 1, copy,temp):
                return True
    if len(temp)==0:
        return False
    temp.pop()
    return False


def converter_2d1d(x,y,l):
    return x*l+y


def f_call(temp):
    global final
    final=[]
    for i in temp:
        final.append(i)
    #print(final)

def check_dim(i,j,k,n,temp):
    for z in temp:
        y = z % n
        x = (z - y) / n
        if i==x and j==y:
            return True
    return False
def print_func(n,k,arr,temp,str):
    for i in range(n):
        for j in range(n):
            if k == n:
                k=k-1
            if check_dim(i, j, k, n, temp):
                print(arr[i][j], end='')
                k += 1
            else:
                print('.', end='')


        print()





def main():
    str_1=input()
    # print(str_1)
    n = len(str_1)
    # print("n: " + str(n))
    array =[]
    value = []
    for j in range(n * n):
        value.append(0)
    # print("val" + str(value))
    temp = []
    k = 0
    trial = True

    for i in range(n):
          array.append([j for j in input()])
    # print("array: " + str(array))

    for i in range(n):
        if trial == False:
            break
        for j in range(n):
            if array[i][j] == str_1[0]:
                temp.append(converter_2d1d(i,j,n))
                if srch(array, str_1, i, j, 1, str_1[0],temp):
                    print_func(n,k,array,temp,str_1)
                    trial=False
                else:
                    temp = []
            if trial ==False:
                break

    if trial is True:
        print("NO PATH EXISTS")




# main()
'''if len(final)==n:
                 for i in range(n):
                     for j in range(n):
                         if dim_check(i,j,k,n):
                             print(arr[i][j],end='')
                             k+=1
                         else:
                             print('.',end='')
                         if k==n:
                             k=k-1
                 break
             else:
                 temp=[]'''

'''
PORTAL
POTOLP
LRLRRR
PTARPO
TAPRRO
LPOPOR
PLRLRL
'''

'''
PORTAL
POTOLP
LRPRRR
PTARPO
TAPRRO
LPOPOR
PLRLRL
'''
