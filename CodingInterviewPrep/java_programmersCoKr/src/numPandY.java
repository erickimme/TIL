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
