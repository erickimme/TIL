#Alternating Subarrays
'''
There's an array A consisting of N non-zero integers A1..N. A subarray of A is called alternating if any two adjacent elements in it have different signs (i.e. one of them should be negative and the other should be positive).

For each x from 1 to N, compute the length of the longest alternating subarray that starts at x - that is, a subarray Ax..y for the maximum possible y ≥ x. The length of such a subarray is y-x+1.

Input Format

The first line contains N(number of elements).
The following line contains N space-separated integers A1..N.
Constraints

1 ≤ N ≤ 4*105
-109 ≤ Ai ≤ 109
Output Format

Output one line with N space-separated integers - the lengths of the longest alternating subarray starting at x, for each x from 1 to N.

Sample Input 0

4
1 -5 1 -5
Sample Output 0

4 3 2 1
Sample Input 1

6
-5 -1 -1 2 -2 -3

Sample Output 1
1 1 3 2 1 1
'''
def isOppSign(array):
    cnt_list = []
    for a in range(0, len(array)):
        cnt = 1
        # print("")
        # print("new start")
        # print("checking position: array[" + str(a) + "]")
        # print("starting count: ", cnt)
        # for i,j in zip(array[a:], array[a+1:]):
        for i in range(len(array)-a-1):
            if ((array[a+i]) * (array[a+i+1]) < 0 ):
                # print(str(array[i]) + " " + str(array[i+1]) + " are opposite signs" )
                cnt += 1
                # print("cnt: ", cnt)
            else:
                break
        cnt_list.append(cnt)
    # print(cnt_list)
    # print("cnt_list: " + str(cnt_list))

    # printing in format
    # return ' '.join(map(str, cnt_list))
    for e in cnt_list:
        print(e, end=" ")

def main():
    n = input().strip() #str
    array = [int(x) for x in input().split()]  # str
    # print("n: " + str(n))
    # print("array: " + str(array))

    ''' w/o list comprehension
    input_array = input().split()
    array = []
    for a in input_array:
        array.append(int(a))
    print(array)
    '''

    isOppSign(array)

main()

