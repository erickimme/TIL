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