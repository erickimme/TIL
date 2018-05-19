import com.sun.deploy.util.ArrayUtil;
import com.sun.tools.javac.util.ArrayUtils;

import java.util.ArrayList;
import java.util.Arrays;

class Divisible {
    public int[] divisible(int[] array, int divisor) {
        //ret에 array에 포함된 정수중, divisor로 나누어 떨어지는 숫자를 순서대로 넣으세요.
        int count = 0;

        for (int i: array) {
            if (i % divisor == 0){
                count++;
            }
        }

        int idx = 0;
        int[] ret = new int[count];
        for (int i = 0; i < array.length; i++) {
            if (array[i] % divisor == 0){
                ret[idx] = array[i];
                idx++;
            }
        }
        return ret;
    }

    // arraylist
    public int[] divisible1(int[] array, int divisor) {
        //ret에 array에 포함된 정수중, divisor로 나누어 떨어지는 숫자를 순서대로 넣으세요.
        ArrayList<Integer> al = new ArrayList<Integer>();
        for (int i : array) {
            if(i % divisor == 0) {
                al.add(i);
            }
        }

        int[] ret = new int[al.size()];
        for (int i = 0; i < al.size(); i++) {
            ret[i] = al.get(i);
        }
        return ret;
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        Divisible div = new Divisible();
        int[] array = {5, 9, 7, 10};
        System.out.println( Arrays.toString( div.divisible(array, 5) ));
        System.out.println( Arrays.toString( div.divisible1(array, 5) ));
    }
}