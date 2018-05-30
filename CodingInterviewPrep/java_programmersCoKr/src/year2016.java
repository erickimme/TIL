import java.util.Calendar;
import java.util.Locale;
import java.time.*;

/**
 * 2016년
 * 문제 설명
 * 2016년 1월 1일은 금요일입니다.
 * 2016년 a월 b일은 무슨 요일일까요? 두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
 * 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT입니다.
 * 예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.
 *
 * 제한 조건
 * 2016년은 윤년입니다.
 * 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
 * 입출력 예
 *  a	b	result
 *  5	24	TUE
 *
 * https://programmers.co.kr/learn/courses/30/lessons/12901?language=java
 *
 */

public class year2016 {
    // using Calendar
    public String year2016(int month, int day) {
        Calendar cal = new Calendar.Builder().setCalendarType("iso8601")
                .setDate(2016, month-1, day)
                .build();
        Locale local = new Locale("ko-KR");
        String answer = cal.getDisplayName(Calendar.DAY_OF_WEEK, Calendar.LONG, local).toUpperCase();
        return answer;
    }


    // calendar with different way of using
    public static String year2016_1(int month, int day) {
        Calendar cal = Calendar.getInstance();
        cal.set(2016 ,month-1 ,day);

        String answer[] = {"SUN","MON","TUE","WED","THU","FRI","SAT"};
        int ab=cal.get(Calendar.DAY_OF_WEEK)-1;
        return answer[ab];
    }

    // best answer, using LocalDate
    public static String year2016_2(int month, int day) {
        LocalDate newDate = LocalDate.of(2016, month, day);
        return newDate.getDayOfWeek().toString().substring(0,3);
    }

    // normal
    public static String year2016_3(int a, int b) {
        String answer = "";
        String[] day = { "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU" };
        int[] date = { 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        int allDate = 0;
        for (int i = 0; i < a - 1; i++) {
            allDate += date[i];
        }
        allDate += (b - 1);
        answer = day[allDate % 7];

        return answer;
    }

    // using case
    public static String year2016_4(int a, int b) {
        String answer = " ";
        int[] monthDay = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        for (int i = 1; i < a; i++) {
            b += monthDay[i - 1];
        }
        switch (b % 7) {
            case 3:
                answer = "SUN";
                break;
            case 4:
                answer = "MON";
                break;
            case 5:
                answer = "TUE";
                break;
            case 6:
                answer = "WED";
                break;
            case 0:
                answer = "THU";
                break;
            case 1:
                answer = "FRI";
                break;
            case 2:
                answer = "SAT";
                break;
        }
        return answer;
    }

    public static void main(String[] args) {
        year2016 y2016 = new year2016();
        int month = 5;
        int day = 24;
        System.out.println(y2016.year2016(month, day));
        System.out.println(y2016.year2016_1(month, day));
        System.out.println(y2016.year2016_2(month, day));
        System.out.println(y2016.year2016_3(month, day));
        System.out.println(y2016.year2016_4(month, day));
    }
}

