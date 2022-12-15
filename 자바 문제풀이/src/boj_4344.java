import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_4344 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int C = Integer.parseInt(br.readLine());

        for (int i = 0; i < C; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int N = Integer.parseInt(st.nextToken());

            int[] arr = new int [N];
            
            int sum = 0;

            for (int j = 0; j < arr.length; j++) {
                int num = Integer.parseInt(st.nextToken());
                arr[j] = num;
                sum += num;
            }
            
            double avg = sum / N;

            double cnt = 0;

            for (int j = 0; j < arr.length; j++) {
                if (arr[j] > avg) {
                    cnt ++;
                }
            }            

            System.out.printf("%.3f%%\n", (cnt/N)*100);
            

        }


    }
}
