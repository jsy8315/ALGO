import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();

        int A100 = A / 100; //100으로 나눈 몫 -> 100의 자리수
        int A100NA = A % 100; //100으로 나눈 나머지, 즉 10의 자리 숫자들
        int A10 = A100NA / 10; //10의 자리수
        int A10NA = A100NA % 10; //1의 자리수

        int rA = A10NA * 100 + A10 * 10 + A100;

        int B100 = B / 100; //100으로 나눈 몫 -> 100의 자리수
        int B100NA = B % 100; //100으로 나눈 나머지, 즉 10의 자리 숫자들
        int B10 = B100NA / 10; //10의 자리수
        int B10NA = B100NA % 10; //1의 자리수

        int rB = B10NA * 100 + B10 * 10 + B100;

        if (rA > rB) {
            System.out.println(rA);
        } else {
            System.out.println(rB);
        }
    }
}