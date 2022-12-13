import java.util.Scanner;

public class boj_25304 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int total = input.nextInt();
        int cnt = input.nextInt();

        int buy = 0;

        for (int i = 0; i < cnt; i++) {
            int p = input.nextInt();
            int q = input.nextInt();

            buy += p*q;
        }

        if (buy == total) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}
