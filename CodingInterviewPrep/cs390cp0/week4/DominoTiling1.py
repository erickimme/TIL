# Domino Tiling 1
'''
In how many ways can you tile a 3 x n rectangle with 2 x 1 dominoes? Here is a sample tiling of a 3 x 12 rectangle.

image

Input Format

Input consists of several test cases followed by a line containing -1. Each test case is a line containing an integer.

Constraints

0 <= n <= 30

Output Format

For each test case, output one integer number giving the number of possible tilings.

Sample Input 0

2
8
12
-1
Sample Output 0

3
153
2131
'''


def calcWay(n):
    if n < 1:
        return 1
    if n == 2:
        return 3

    return (4*calcWay(n-2) - calcWay(n-4))


if __name__ == '__main__':
    while True:
        n = int(input().strip()) # str -> int
        if (n == -1):
            break
        elif (n % 2 == 0): #even
            print(calcWay(n))
        else:
            print(0)

