import java.util.Scanner;

public class boj_8393 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n = input.nextInt();

        input.close();
        
        int ans = 0;

        for (int i = 1; i <= n; i++) {
            ans += i;
        }

        System.out.println(ans);
    }
}
