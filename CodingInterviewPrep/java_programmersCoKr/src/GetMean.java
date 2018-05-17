//함수를 완성해서 매개변수 array의 평균값을 return하도록 만들어 보세요.
//        어떠한 크기의 array가 와도 평균값을 구할 수 있어야 합니다.
//https://programmers.co.kr/learn/challenge_codes/127

import java.util.Arrays;

public class GetMean {
    public int getMean(int[] array) {
        int len = array.length;
        int sum = 0;
        for (int i = 0; i < len; i++) {
            sum += array[i];
        }
        int mean = sum/len;
        return mean;
    }

    // enhanced for loop
    public int getMean_enhancedForLoop(int[] array) {
        int len = array.length;
        int sum = 0;
        for (int i : array){
            sum += i;
        }
        int mean = sum/len;
        return mean;
    }

    // stream
    // java 8에 새롭게 추가된 API
    // 가독성 간편성을 제공
    // for loop과 Iterator(반복자) 대신 사용하여 코드가 간단해짐
    // 문제 : 스트림은 오직 한 번 만 사용할 수 있음 (재사용 불가)
    // 참고자료 :
    // https://www.mkyong.com/java8/java-how-to-convert-array-to-stream/
    // https://okky.kr/article/329818
    public int getMean_stream(int[] array) {
        int answer = (int) Arrays.stream(array).average().orElse(0);
        return answer;
    }

     // stream (1)
     public int getMean_stream1(int[] array) {
         int answer = java.util.stream.IntStream.of(array).sum()/array.length;
         return answer;
     }


    public static void main(String[] args) {
        int x[] = {5, 4, 3};
        GetMean getMean = new GetMean();
        // 아래는 테스트로 출력해 보기 위한 코드입니다.
        System.out.println("평균값 : " + getMean.getMean(x));
        System.out.println("평균값 : " + getMean.getMean_enhancedForLoop(x));
        System.out.println("평균값 : " + getMean.getMean_stream(x));
        System.out.println("평균값 : " + getMean.getMean_stream1(x));

        // output
//        평균값 : 4
//        평균값 : 4
//        평균값 : 4
//        평균값 : 4
    }
}

