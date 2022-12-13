import java.util.Scanner;

public class boj_2739 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int num = input.nextInt();

        input.close();

        for (int i = 1; i < 10; i++) {
            System.out.printf("%d * %d = %d\n", num, i, num*i);
        }
    }
}
