//문제
//알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

//입력
//첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

//출력
//각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.

//만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는
//문제
//        문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
//
//        QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
//
//        입력
//        첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다.
//
//        출력
//        각 테스트 케이스에 대해 P를 출력한다.
//문제
//        9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
//
//        예를 들어, 서로 다른 9개의 자연수
//
//        3, 29, 38, 12, 57, 74, 40, 85, 61
//
//        이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
//
//        입력
//        첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
//
//        출력
//        첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String[] words = str.split("");
        int result = 0;
        int t = words.length;

        if (words[0].equals(" ")) {
            if (words[t-1].equals(" ")) {
                for (int i = 0; i < words.length; i++) {
                    if (words[i].equals(" ")) {
                        result += 1;
                    }
                }
                System.out.println(result - 1);
            } else {
                for (int i = 0; i < words.length; i++) {
                    if (words[i].equals(" ")) {
                        result += 1;
                    }
                }
                System.out.println(result);
            }
        } else {
            if (words[t-1].equals(" ")) {
                for (int i = 0; i < words.length; i++) {
                    if (words[i].equals(" ")) {
                        result += 1;
                    }
                }
                System.out.println(result);
            } else {
                for (int i = 0; i < words.length; i++) {
                    if (words[i].equals(" ")) {
                        result += 1;
                    }
                }
                System.out.println(result + 1);
            }
        }
    }
}