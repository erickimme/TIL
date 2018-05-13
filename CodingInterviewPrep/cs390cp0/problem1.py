#Basic Input Practice
'''
You're given a series of test cases with integers, and you will need to return the sum for each test case.

Input Format

Input begins with an integer n representing the number of test cases following. Each of the n lines after will contain a single integer x followed by x integers. Your output will be n integers, one on each line, indicating the sum of the x integers for that test case.

Constraints

0 < n < 50 0 < x < 10

Output Format

n integers representing sums.

Sample Input 0

2
3 5 2 3
1 1
Sample Output 0

10
1
Explanation 0

x is 2, so we have 2 test cases. First test case has x equal to 3, so we add all 3 numbers following. On the next line we have 1 number to add, so the sum is 1.

Sample Input 1

1
1 2
Sample Output 1

2
Sample Input 2

0

'''

'''C
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */    
    int numCase = 0;
    int numNum = 0;
    scanf("%d", &numCase);
    int i, j;
    for (i=0; i < numCase; i++) {    
        int sum = 0;
        scanf("%d", &numNum);
        for (j=0; j < numNum; j++) {
            int num = 0;
            scanf("%d", &num);
            sum += num;
        }
        
        printf("%d\n", sum);           
    }
    
    return 0;
}
'''


'''python
(
'''
