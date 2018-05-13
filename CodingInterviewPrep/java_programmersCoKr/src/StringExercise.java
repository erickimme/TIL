/*
getMiddle메소드는 하나의 단어를 입력 받습니다.
단어를 입력 받아서 가운데 글자를 반환하도록 getMiddle메소드를 만들어 보세요.
단어의 길이가 짝수일경우 가운데 두글자를 반환하면 됩니다.
예를들어 입력받은 단어가 power이라면 w를 반환하면 되고, 입력받은 단어가 test라면 es를 반환하면 됩니다.

https://programmers.co.kr/learn/challenge_codes/82
 */
public class StringExercise{
    String getMiddle(String word){
        int len = word.length();

        if (len % 2 == 0){
            String e_word_front = String.valueOf(word.charAt((len/2) - 1));
            String e_word_back = String.valueOf(word.charAt(len/2));
            String full_word = e_word_front + e_word_back;
            // System.out.println(full_word);
            return full_word;
        }
        else if (len % 2 != 0){
            String o_word = String.valueOf(word.charAt(len/2));
            // System.out.println(o_word);
            return o_word;
        }
        return null;
    }

    // best answer
    /*
    class StringExercise{
        String getMiddle(String word){

            return word.substring((word.length()-1)/2, word.length()/2 + 1);
        }
        // 아래는 테스트로 출력해 보기 위한 코드입니다.
        public static void  main(String[] args){
            StringExercise se = new StringExercise();
            System.out.println(se.getMiddle("power"));
        }
    }
    */


    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void  main(String[] args){
        StringExercise se = new StringExercise();
        System.out.println(se.getMiddle("power"));
    }
}