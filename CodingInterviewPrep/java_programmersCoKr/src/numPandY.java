/**문자열 내 p와 y의 개수
 * 문제 설명
 * 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True,
 * 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
 * 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
 * 예를들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.
 *
 * 제한사항
 * 문자열 s의 길이 : 50 이하의 자연수
 * 문자열 s는 알파벳으로만 이루어져 있습니다.
 *
 * 입출력 예
 * s	    answer
 * pPoooyY	true
 * Pyy	    false
 *
 * 입출력 예 설명
 * 입출력 예 #1
 * 'p'의 개수 3개, 'y'의 개수 3개로 같으므로 true를 return 합니다.
 *
 * 입출력 예 #2
 * 'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.
 *
 * https://programmers.co.kr/learn/courses/30/lessons/12916
 */


import java.util.Arrays;

public class numPandY {
    public static boolean numPandY(String s) {
        boolean answer = false;
        int pCount = 0;
        int yCount = 0;
        for (int i = 0; i < s.length(); i++){
            if ((s.toLowerCase()).charAt(i) == 'p'){
                pCount++;
            }
            if ((s.toLowerCase()).charAt(i) == 'y'){
                yCount++;
            }
        }
        if (pCount == yCount){
            answer = true;
        }
        return answer;
    }

    public static boolean numPandY1(String s) {
        s = s.toUpperCase();

        return s.chars().filter( e -> 'P'== e).count() == s.chars().filter( e -> 'Y'== e).count();
    }

    public static boolean numPandY2(String s) {
        long pCnt = Arrays.asList(s.split("")).stream().map(str->str.toUpperCase()).filter(str->str.equals("P")).count();
        long yCnt = Arrays.asList(s.split("")).stream().map(str->str.toUpperCase()).filter(str->str.equals("Y")).count();

        return (pCnt==yCnt)?true:false;
    }

    public static boolean numPandY3(String s) {
        s = s.toUpperCase();
        long pCnt = Arrays.stream(s.split("")).filter(str->str.equals("P")).count();
        long yCnt = Arrays.stream(s.split("")).filter(str->str.equals("Y")).count();

        return (pCnt==yCnt)?true:false;
    }

    public static void main(String[] args) {
        String test1 = "pPoooyY";
        String test2 = "Pyy";

        numPandY npy = new numPandY();
        System.out.println(npy.numPandY(test1));
        System.out.println(npy.numPandY(test2));
        System.out.println(npy.numPandY1(test1));
        System.out.println(npy.numPandY1(test2));
        System.out.println(npy.numPandY2(test1));
        System.out.println(npy.numPandY2(test2));
        System.out.println(npy.numPandY3(test1));
        System.out.println(npy.numPandY3(test2));
    }

}
