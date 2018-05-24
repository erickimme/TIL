/**
 * 최대값과 최소값 Level 1
 * getMinMaxString 메소드는 String형 변수 str을 매개변수로 입력받습니다.
 * str에는 공백으로 구분된 숫자들이 저장되어 있습니다.
 * str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 (최소값) (최대값)형태의 String을 반환하는 메소드를 완성하세요.
 * 예를들어 str이 1 2 3 4라면 1 4를 리턴하고, -1 -2 -3 -4라면 -4 -1을 리턴하면 됩니다.
 *
 *
 * https://programmers.co.kr/learn/challenge_codes/125
 */

import java.util.Arrays;

public class GetMinMaxString {
    public String getMinMaxString(String str) {
        String [] minMax = str.split(" ");;
        int max = Integer.parseInt(minMax[0]);
        int min = Integer.parseInt(minMax[0]);

        for (int i = 1; i < minMax.length; i++) {
            if ( Integer.parseInt(minMax[i]) > max){
                max = Integer.parseInt(minMax[i]);
            }
            if (Integer.parseInt(minMax[i]) < min){
                min= Integer.parseInt(minMax[i]);
            }
        }
//        return String.format("%d %d", min, max);
        return min + " " + max;
    }

    public String getMinMaxString0(String str) {
        String[] tmp = str.split(" ");
        int min, max, n;
        min = max = Integer.parseInt(tmp[0]);
        for (int i = 1; i < tmp.length; i++) {
            n = Integer.parseInt(tmp[i]);
            if(min > n) min = n;
            if(max < n) max = n;
        }

        return min + " " + max;

    }

    public String getMinMaxString1(String str) {
        int arr[];
        int leng = str.split(" ").length;
        arr = new int[leng];

        for(int i=0; i<leng; i++){
            arr[i] = (Integer.parseInt(str.split(" ")[i]));
        }

        return Arrays.stream(arr).min().orElse(0) + " " + Arrays.stream(arr).max().orElse(0);
    }



    public static void main(String[] args) {
        String str = "1 2 3 4";
        GetMinMaxString minMax = new GetMinMaxString();
        //아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println("최대값과 최소값은?" + minMax.getMinMaxString(str));
        System.out.println("최대값과 최소값은?" + minMax.getMinMaxString0(str));
        System.out.println("최대값과 최소값은?" + minMax.getMinMaxString1(str));
    }
}