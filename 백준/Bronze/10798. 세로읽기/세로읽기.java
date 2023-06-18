//입력
//총 다섯줄의 입력이 주어진다. 각 줄에는 최소 1개, 최대 15개의 글자들이 빈칸 없이 연속으로 주어진다. 주어지는 글자는 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’ 중 하나이다. 각 줄의 시작과 마지막에 빈칸은 없다.
//
//출력
//영석이가 세로로 읽은 순서대로 글자들을 출력한다. 이때, 글자들을 공백 없이 연속해서 출력한다.


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //단어 하나씩 하나씩 입력받기

        String word1 = sc.nextLine();
        String word2 = sc.nextLine();
        String word3 = sc.nextLine();
        String word4 = sc.nextLine();
        String word5 = sc.nextLine();

        String[][] words = new String[5][15];

        for(int i = 0; i < 15; i++) {
            if(i < word1.length() ) {
                words[0][i] = String.valueOf(word1.charAt(i));
            } else {
                words[0][i] = "";
            }
        }
        for(int i = 0; i < 15; i++) {
            if(i < word2.length() ) {
                words[1][i] = String.valueOf(word2.charAt(i));
            } else {
                words[1][i] = "";
            }
        }
        for(int i = 0; i < 15; i++) {
            if(i < word3.length() ) {
                words[2][i] = String.valueOf(word3.charAt(i));
            } else {
                words[2][i] = "";
            }
        }
        for(int i = 0; i < 15; i++) {
            if(i < word4.length() ) {
                words[3][i] = String.valueOf(word4.charAt(i));
            } else {
                words[3][i] = "";
            }
        }
        for(int i = 0; i < 15; i++) {
            if(i < word5.length() ) {
                words[4][i] = String.valueOf(word5.charAt(i));
            } else {
                words[4][i] = "";
            }
        }

        for(int j = 0;j < 15; j++) {
            for (int i = 0; i < 5; i++) {
                System.out.print(words[i][j] + "");
            }
        }
    }
}
