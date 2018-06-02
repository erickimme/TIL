public class stringToInteger {
    public static int stringToInteger (String s) {
        return Integer.valueOf(s);
    }

    public static void main(String[] args) {
        String str1 = "1234";
        String str2 = "-1234";

        stringToInteger sti = new stringToInteger();
        System.out.println(sti.stringToInteger(str1));
        System.out.println(sti.stringToInteger(str2));
    }
}
