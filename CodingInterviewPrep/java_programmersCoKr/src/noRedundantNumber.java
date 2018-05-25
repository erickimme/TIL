/**
 * 문제 설명
 * 배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.
 * 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
 * 배열 arr에서 제거 되고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
 * 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.

 * 예를들면
 * arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
 * arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
 * 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

 * 제한사항
 * 배열 arr의 크기 : 1,000,000 이하의 자연수
 * 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
 * 입출력 예
 * arr	            answer
 * [1,1,3,3,0,1,1]	[1,3,0,1]
 * [4,4,4,3,3]	    [4,3]

 * 입출력 예 설명
 * 입출력 예 #1,2
 * 문제의 예시와 같습니다.
 *
 * https://programmers.co.kr/learn/courses/30/lessons/12906?language=java
 */

import java.util.*;

//public class Solution {
//    public int[] solution(int []arr) {
//        int[] answer = {};
//
//        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
//        System.out.println("Hello Java");
//
//        return answer;
//    }
//}
public class noRedundantNumber {
    
    // array
    public static int[] noRedundantNumber1(int []arr) {
        int len = arr.length;
        int[] answer = new int[len];

        if(len == 0)
            return answer;

        int cnt = 0;
        answer[cnt] = arr[cnt];
        for(int i = 1; i < len; i++)
        {
            if(arr[i] != answer[cnt]){
                cnt++;
                answer[cnt] = arr[i];
            }
        }
        int finalLength = cnt + 1;
        int [] finalAnswer = new int[finalLength];
        for(int i = 0; i < finalLength; i++) {
            finalAnswer[i] = answer[i];
        }
        return finalAnswer;
    }

    // arraylist, array
    public static int[] noRedundantNumber2(int [] arr){
        ArrayList<Integer> list = new ArrayList<>();
        int num = arr[0];
        list.add(arr[0]);
        for (int i = 1; i < arr.length ; i++) {
            if (num == arr[i]) {
                continue;
            } else {
                list.add(arr[i]);
                num = arr[i];
            }
        }

        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size() ; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }

    // arraylist, array
    public static int[] noRedundantNumber3(int [] arr){
        ArrayList<Integer> numlist = new ArrayList<Integer>();
        if (arr.length <= 1000000) {
            int before = arr[0];
            numlist.add(before);
            for (int i : arr) {
                if (before == i){
                    ;
                }
                else{
                    numlist.add(i);
                    before = i;
                }
            }
        }

        int[] answer = new int[numlist.size()];
        for (int i = 0; i < numlist.size(); i++) {
            answer[i] = numlist.get(i);
//            System.out.print(answer[i] + " ");
        }
        return answer;
    }

    // Stringbuilder
    public int[] noRedundantNumber4(int []arr) {
        StringBuilder sb = new StringBuilder();
        int size = arr.length;
        sb.append(arr[0]);
        for(int i=1; i<size; i++){
            if(arr[i-1]!=arr[i]) sb.append(arr[i]);
        }
        String[] array = sb.toString().split("");
        size = array.length;
        int[] answer = new int[size];
        for(int i=0; i<size; i++){
            answer[i] = Integer.parseInt(array[i]);
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] test1 = {1, 1, 3, 3, 0, 1, 1};
        int[] test2 = {4, 4, 4, 3, 3};

        noRedundantNumber1(test1);
        noRedundantNumber1(test2);
        noRedundantNumber2(test1);
        noRedundantNumber2(test2);
        noRedundantNumber3(test1);
        noRedundantNumber3(test2);

    }
}

