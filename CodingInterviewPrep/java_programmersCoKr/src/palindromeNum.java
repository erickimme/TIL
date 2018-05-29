/**
 * 앞뒤를 뒤집어도 똑같은 문자열을 팰린드롬(palindrome)이라고 합니다.
 * 문자열 s가 주어질 때, s의 부분문자열(Substring)중 가장 긴 팰린드롬의 길이를 return 하는 solution 함수를 완성해 주세요.
 *
 * 예를 들면, 문자열 s가 abcdcba이면 7을 return하고 abacde이면 3을 return합니다.
 *
 * 제한사항
 * 문자열 s의 길이 : 2500 이하의 자연수
 * 문자열 s는 알파벳 소문자로만 구성
 *
 * 입출력 예
 * s	    answer
 * abcdcba	7
 * abacde	3
 *
 * 입출력 예 설명
 * 입출력 예 #1
 * 4번째자리 'd'를 기준으로 문자열 s 전체가 팰린드롬이 되므로 7을 return합니다.
 *
 * 입출력 예 #2
 * 2번째자리 'b'를 기준으로 aba가 팰린드롬이 되므로 3을 return합니다.
 *
 * https://programmers.co.kr/learn/courses/30/lessons/12904?language=java
 *
 */


public class palindromeNum {
    public static int palindromNum(String s)
    {
        int answer = 0;
        int biggest = 0;

        String newS = "";
        int j = s.length()-1;

        // getting substrings :
        // a -> ab -> abc -> abcd -> abcd -> abcdc -> abcdcb -> abcdcba -> b -> bc -> bcd ~
        for (int i = 0; i < s.length(); i++) { //
            for (int k = i; k < s.length(); k++) {
                newS = s.substring(i,k+1);
                answer = palNum(newS);
//                System.out.println("substring: " + newS + "  |  num: " + answer);
                if (answer > biggest){
                    biggest = answer;
                }
            }
        }
//        System.out.println(biggest);
        return biggest;
    }
    public static int palNum(String s){
        int answer = 0;
        int j = s.length()-1;
        for (int i = 0; i < s.length(); i++) {
            char front = s.charAt(i);
            char back = s.charAt(j);
            if (front == back){
                answer += 1;
            }
            j--;
        }
        return answer;
    }

    public static String reverseStr(String s){
        StringBuilder sb = new StringBuilder(s);
        return sb.reverse().toString();

    }

    public static int palindromNum1(String s){
        if (s.equals(reverseStr(s))){
            return s.length();
        }
        else {
            int a = palindromNum1(s.substring(0, s.length()-1));
            int b = palindromNum1(s.substring(1, s.length()));
            return Math.max(a,b);
        }
    }


    public static void main(String[] args) {
        String test1 = "abcdcba"; //7 abc d cba
        String test2 = "abacde"; //3 aba
        palindromNum(test1);
        palindromNum(test2);
        palindromNum1(test1);
        palindromNum1(test2);
    }
}


