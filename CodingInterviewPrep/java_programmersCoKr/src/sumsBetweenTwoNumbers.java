/**
 * 두 정수 사이의 합
 * 문제 설명
 * 두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
 * 예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.
 *
 * 제한 조건
 * a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
 * a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
 * a와 b의 대소관계는 정해져있지 않습니다.
 *
 * 입출력 예
 * a	b	return
 * 3	5	12
 * 3	3	3
 * 5	3	12
 *
 * https://programmers.co.kr/learn/courses/30/lessons/12912
 */

public class sumsBetweenTwoNumbers {

    public static long sumsBetweenTwoNumbers(int a, int b) {
        long answer = 0;
        if (a == b){
            answer = a;
        }
        else {
            if (a > b){
                answer = summer(b, a);
            }
            else{
                answer = summer(a, b);
            }
        }
        return answer;
    }

    public static int summer(int smaller, int bigger) {
        int sum = 0;
        for (int i = smaller; i <= bigger; i++) {
            sum += i;
        }
        return sum;
    }

    // answer
    public static long sumsBetweenTwoNumbers1(int a, int b) {
        long answer = 0;

        if (a > b){
            int tmp = a;
            a = b;
            b = tmp;
        }
        for(int i = a; i <= b; i++){
            answer += i;
        }
        return answer;
    }

    // others
    public static long sumsBetweenTwoNumbers2(int a, int b){
        long answer = 0;
        if(a!=b){
            for(int i=Math.min(a,b);i<=Math.max(a,b);i++){
                answer+=i;
            }
        }else{
            answer=a;
        }
        return answer;
    }


    public static void main(String[] args) {
        int a = 3;
        int b = 5;
        System.out.println(sumsBetweenTwoNumbers(a,b));
        System.out.println(sumsBetweenTwoNumbers1(a,b));
        System.out.println(sumsBetweenTwoNumbers2(a,b));

    }
}
