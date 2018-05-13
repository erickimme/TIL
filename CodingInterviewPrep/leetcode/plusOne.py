'''
66. Plus One

Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits) - 1 - i))
        print([int(i) for i in str(num + 1)])
        return [int(i) for i in str(num + 1)]

if __name__ == '__main__':
    li = [1,2,3,4]
    test = Solution()

    test.plusOne(li)




