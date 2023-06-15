import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = N / 4; //몫
        int R = N % 4; //나머지

        if (R != 0) {
            M = M + 1;
        }

        for (int i = 0; i < M; i++) {
            System.out.print("long ");
        }
        System.out.println("int");
    }
}