
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String[] word = s.split("");
        int N = word.length;
        int T = 0;

        //짝수인지 홀수인지 나눠서 계산-> 안해도 됐었을듣ㅅ
        //홀수인 경우
        if ((N % 2) == 1) {
            for(int i = 0; i < (N / 2); i++) {
                if (word[i].equals(word[N - 1 - i])) {
                    continue;
                } else {
                    T += 1;
                }
            }
        //짝수인경우
        } else {
            for(int i = 0; i < (N / 2); i++) {
                if (word[i].equals(word[N - 1 - i])) {
                    continue;
                } else {
                    T += 1;
                }
            }
        }

        if ( T == 0 ) {
            System.out.println("1");
        } else {
            System.out.println("0");
        }
    }
}
