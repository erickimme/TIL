//문자열 내림차순으로 배치하기 Level 1
//        reverseStr 메소드는 String형 변수 str을 매개변수로 입력받습니다.
//        str에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 String을 리턴해주세요.
//        str는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
//        예를들어 str이 Zbcdefg면 gfedcbZ을 리턴하면 됩니다.

//https://programmers.co.kr/learn/challenge_codes/98
import java.util.Arrays;
import java.util.Collections;

public class ReverseStr {
    public String reverseStr(String str){
        String newStr = "";
        for (int i = str.length()-1; i >= 0; i--) {
            newStr += str.charAt(i);
        }
        return newStr.toString();
    }

    public String reverseStr1(String str){
        StringBuilder sb = new StringBuilder(str);
        return sb.reverse().toString();
    }

    public String reverseStr2(String str){
        String arr[] = str.split("");
        Arrays.sort(arr);
        StringBuffer sb = new StringBuffer();
        for(int i=0; i<arr.length; i++)
            sb.append(arr[i]);
        return sb.reverse().toString();
    }

    public String reverseStr3(String str){
        // charArray
        char[] charArray = new char[str.length()];
        for(int i=0; i<str.length(); i++) {
            charArray[i] = str.charAt(i);
        }
        // Sort
        Arrays.sort(charArray);
        // Reverse
        String result = "";
        for(int i=charArray.length-1; i>=0; i--) {
            result += Character.toString(charArray[i]);
        }

        return result;
    }

    public String reverseStr4(String str) {
            String[] array = str.split("");
            Arrays.sort(array);
            Collections.reverse(Arrays.asList(array));
            return String.join("", array);
    }

    public String reverseStr5(String str) {
            char[] sol = str.toCharArray();
            Arrays.sort(sol);
            return new StringBuilder(new String(sol)).reverse().toString();
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        ReverseStr rs = new ReverseStr();
        System.out.println( rs.reverseStr("Zbcdefg") );
        System.out.println( rs.reverseStr1("Zbcdefg") );
        System.out.println( rs.reverseStr2("Zbcdefg") );
        System.out.println( rs.reverseStr3("Zbcdefg") );
        System.out.println( rs.reverseStr4("Zbcdefg") );
        System.out.println( rs.reverseStr5("Zbcdefg") );
    }
}