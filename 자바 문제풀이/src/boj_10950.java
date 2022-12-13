import java.util.Scanner;

public class boj_10950 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        int T = input.nextInt();

        for (int i = 0; i < T; i++) {
            int A = input.nextInt();
            int B = input.nextInt();

            System.out.println(A + B);
        }

        input.close();
    }

}
