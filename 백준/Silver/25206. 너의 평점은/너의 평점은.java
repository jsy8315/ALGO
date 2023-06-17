
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //이중배열 선언
        String[][] arr = new String[20][3];

        //for문 돌리면서 입력값 받기
        for (int i = 0; i < 20; i++) {
            for (int j = 0; j < 3; j++) {
                arr[i][j] = sc.next();
            }
        }
        //기본 값 선언
        double score = 0.0;
        //P는 학점계산에서 제외해야되므로 따로 계산 -> 이걸로 나누는게 아니었음ㅅㅂ
        int P = 0;
        double credits = 0.0;

        //for문 돌면서 학점 계산
        for (int i = 0; i < 20; i++) {
            if (arr[i][2].equals("A+")) {
                //학점 숫자로 변환
                double credit = Double.parseDouble(arr[i][1]);
                score += credit * 4.5;
                credits += credit;
            } else if (arr[i][2].equals("A0")) {
                //학점 숫자로 변환
                double credit = Double.parseDouble(arr[i][1]);
                score += credit * 4.0;
                credits += credit;
            } else if (arr[i][2].equals("B+")) {
                //학점 숫자로 변환
                double credit = Double.parseDouble(arr[i][1]);
                score += credit * 3.5;
                credits += credit;
            } else if (arr[i][2].equals("B0")) {
                //학점 숫자로 변환
                double credit = Double.parseDouble(arr[i][1]);
                score += credit * 3.0;
                credits += credit;
            } else if (arr[i][2].equals("C+")) {
                //학점 숫자로 변환
                double credit = Double.parseDouble(arr[i][1]);
                score += credit * 2.5;
                credits += credit;
            } else if (arr[i][2].equals("C0")) {
                //학점 숫자로 변환
                double credit = Double.parseDouble(arr[i][1]);
                score += credit * 2.0;
                credits += credit;
            } else if (arr[i][2].equals("D+")) {
                //학점 숫자로 변환
                double credit = Double.parseDouble(arr[i][1]);
                score += credit * 1.5;
                credits += credit;
            } else if (arr[i][2].equals("D0")) {
                //학점 숫자로 변환
                double credit = Double.parseDouble(arr[i][1]);
                score += credit * 1.0;
                credits += credit;
            } else if (arr[i][2].equals("F")) {
                //학점 숫자로 변환
                double credit = Double.parseDouble(arr[i][1]);
                score += credit * 0.0;
                credits += credit;
            } else {
                continue;
            }
        }
        score = score / credits;
        System.out.println(score);
    }
}
