import java.util.Scanner;

public class boj_2525 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int A = input.nextInt();
        int B = input.nextInt();

        int C = input.nextInt();

        input.close();

        A += C / 60;
        B += C % 60;

        if (B >= 60) {
            A += 1;
            B -= 60;
        }
        if (A >= 24) {
            A -= 24;
        }

        System.out.printf("%d %d", A, B);
    }
}
