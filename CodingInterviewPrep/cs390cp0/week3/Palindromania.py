'''
A palindrome is a word that reads the same backward as forward.
For e.g. "madam" or "noon". For a given string, you need to find the number of substrings that are palindromes.

Input Format
The given input will have one line containing the input string.

Constraints
Length of the string is less than 100.

Output Format
Output the number of distinct palindromic substrings of the input string.

Sample Input 0
abaaa

Sample Output 0
5

Explanation 0
Below are 5 palindrome sub-strings: a, aa, aaa, aba, b
'''


#!/usr/bin/py
# Head ends here
def seperator(a):
    # 1 letter combination
    for i in a:
        print(i)

    # 2 letter combination

    # 3 letter combination
    return


def checkPalindrom(a):
    if len(a) <= 1:
        return True
    else:
        left = 0
        right = len(a) - 1
        # print("left: %d , right: %d" % (left, right))
        while left < right:
            if a[left] == a[right]:
                left += 1
                right -= 1
                return True
            else:
                return False
        return True



# Tail starts here
if __name__ == '__main__':
    # a = input().strip()
    # print("a:", a)

    examples = ["mom", "dad", "abcba", "baddt"]
    for ex in examples:
        if checkPalindrom(ex):
            print(ex)

    # checkPalindrom(a)
    # seperator(a)
    #



