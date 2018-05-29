import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * level1 : 문자열 다루기 기본
 *  문제 설명
 *  문자열 s의 길이가 4혹은 6이고, 숫자로만 구성되있는지 확인해주는 함수, solution을 완성하세요.
 *  예를들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.
 *
 *  제한 사항
 *  s는 길이 1 이상, 길이 8 이하인 문자열입니다.
 *
 *  입출력 예
 *  s	    return
 *  a234	false
 *  1234    true
 *
 *  https://programmers.co.kr/learn/courses/30/lessons/12918?language=java
 */


public class stringchecker {
    public static boolean stringchecker(String s){
        boolean answer = false;
        if (s.length() == 4 || s.length() == 6){
            if(s.matches("^\\d+$")){
                return true;
            }
        }
        return answer;
    }

    // 가장 일반적인 풀이
    public static boolean stringchecker1(String s) {
        int length = s.length();
        if (length != 4 && length != 6)
            return false;
        for (int i = 0; i < length; ++i) {
            char c = s.charAt(i);
            if (c < '0' || c > '9'){
                return false;
            // 똑같은데 ASCII 값으로 적음
//            if (c < 48 || c > 57) {
//                return false;
//            }
            }
        }
        return true;
    }


    // try, catch로 풀어낸 경우
    public static boolean stringchecker2(String s) {
        if(s.length() == 4 || s.length() == 6){
            try{
                int x = Integer.parseInt(s);
                return true;
            } catch(NumberFormatException e){
                return false;
            }
        }
        return false;
    }

    // isDigit이용
    public static boolean stringchecker3(String s) {
        boolean answer = false;
        if(s.length() == 4 || s.length() == 6 ){
            int i;
            for(i=0;i<s.length();i++){
                if(!Character.isDigit(s.charAt(i))){
                    break;
                }
            }
            if(i==s.length()){
                answer =true;
            }
        }
        return answer;
    }

    // patten, compile로 풀어낸 경우
    public static boolean stringchecker4(String s) {
        boolean answer = true;
        Pattern p = Pattern.compile("^\\d{4}$");
        Matcher m = p.matcher(s);
        answer = m.matches();
        return answer;
    }

    public static void main(String[] args) {
        String str1 = "a234";
        String str2 = "1234";

        stringchecker(str1);
        stringchecker(str2);
        stringchecker1(str1);
        stringchecker1(str2);
        stringchecker2(str1);
        stringchecker2(str2);
        stringchecker3(str1);
        stringchecker3(str2);
    }
}
