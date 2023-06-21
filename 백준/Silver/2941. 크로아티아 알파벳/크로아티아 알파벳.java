import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        String[] arr = s.split("");
        int len = arr.length;
        int result = 0;

        for(int i = 0; i < arr.length; i++ ) {
            if (arr[i].equals("c")) {
                result += 1;
            } else if(arr[i].equals("d") ) {
                result += 1;
            } else if(arr[i].equals("l")) {
                result += 1;
            } else if(arr[i].equals("n")) {
                result += 1;
            } else if(arr[i].equals("s")) {
                result += 1;
            } else if(arr[i].equals("z")) {
                if (i == 0) {
                    result += 1;
                } else if (i == (len - 1)) {
                    result += 1;
                } else {
                    if (arr[i - 1].equals("d") && arr[i + 1].equals("=")) {
                        continue;
                    } else {
                        result += 1;
                    }
                }
            } else if(arr[i].equals("j")) {
                if (i == 0) {
                    result += 1;
                } else {
                    if (arr[i - 1].equals("l") || arr[i - 1].equals("n")) {
                        continue;
                    } else {
                        result += 1;
                    }
                }
            } else if (arr[i].equals("=") || arr[i].equals("-")) {
                continue;
            } else {
                result += 1;
            }
        }
        System.out.print(result);
    }
}
