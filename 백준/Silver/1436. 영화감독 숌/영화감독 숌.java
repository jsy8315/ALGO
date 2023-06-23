import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //입력값
        int N = sc.nextInt();

        int count = 0;
        int i = 1;

        while (count < N + 1) {
            String s = Integer.toString(i);

            if(s.contains("666")) {
                count++;
            }

            if (count == N) {
                System.out.println(i);
                break;
            }
            i++;
        }
    }
}
