import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_1110 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        
        int originalN = N;
        int cnt = 0;

        while (true) {
            N = ((N % 10) * 10 + ((N / 10) + (N % 10)) % 10);
            cnt ++;

            if (N == originalN) {
                System.out.println(cnt);
                break;
            }
        }

    }
}
