import java.util.Scanner;

public class boj_2884 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int H = input.nextInt();
        int M = input.nextInt();

        input.close();

        if (M < 45) {
            if (H == 0) {
                H = 23;
            } else {
                H -= 1;
            }
            M += 15;
        } else {
            M -= 45;
        }

        System.out.printf("%d %d", H, M);
    }
}
