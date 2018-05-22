import java.util.ArrayList;

/**
 * 수박수박수박수박수박수? Level 1
 * water_melon함수는 정수 n을 매개변수로 입력받습니다.
 * 길이가 n이고, 수박수박수...와 같은 패턴을 유지하는 문자열을 리턴하도록 함수를 완성하세요.
 * 예를 들어 n이 4이면 '수박수박'을 리턴하고 3이라면 '수박수'를 리턴하면 됩니다.
 *
 * https://programmers.co.kr/learn/challenge_codes/109
 */

public class WaterMelon {
    public String watermelon(int n){
        ArrayList<String> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (i % 2 == 0){
                result.add(i, "수");
            }
            else{
                result.add(i, "박");
            }
        }
        return String.join("", result);
    }

    //
    public String watermelon1(int n){
        return new String(new char [n/2+1]).replace("\0", "수박").substring(0,n);
    }

    // ?
    public String watermelon2(int n){
        String result="";
        for(int i=0; i<n; i++){
            result += i%2==0?"수":"박";
        }

        // same code
//        for(int i = 0; i < n ; i++){
//            if(i%2 ==0)result+="수";
//            else result+="박";
//        }

        return result;
    }

    // stringbuffer
    public String watermelon3(int n){
        StringBuffer sf = new StringBuffer();
        for (int i=1; i<=n; ++i) {
            sf.append(i%2==1?"수":"박");
        }
        return sf.toString();
    }

    // 실행을 위한 테스트코드입니다.
    public static void  main(String[] args){
        WaterMelon wm = new WaterMelon();
        System.out.println("n이 3인 경우: " + wm.watermelon(3));
        System.out.println("n이 4인 경우: " + wm.watermelon(4) + "\n");
        System.out.println("n이 3인 경우: " + wm.watermelon1(3));
        System.out.println("n이 4인 경우: " + wm.watermelon1(4) + "\n");
        System.out.println("n이 3인 경우: " + wm.watermelon2(3));
        System.out.println("n이 4인 경우: " + wm.watermelon2(4) + "\n");
        System.out.println("n이 3인 경우: " + wm.watermelon3(3));
        System.out.println("n이 4인 경우: " + wm.watermelon3(4) + "\n");
    }
}
