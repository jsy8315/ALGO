import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
            int N = sc.nextInt();
            //배열 선언
            int[] arr = new int[N];

            //입력받은 값 배열로 저장
            for (int i = 0; i < N; i++) {
                arr[i] = sc.nextInt();
            }
            //최대값, 최소값을 배열 첫 수로 지정
            int max = arr[0];
            int min = arr[0];

            //for문을 돌면서 max, min 갱신
            for (int j = 0; j < N; j++ ) {
                if (max < arr[j]) {
                    max = arr[j];
                }
                if (min > arr[j]) {
                    min = arr[j];
                }
            }
        System.out.println(min + " " + max);
    }
}