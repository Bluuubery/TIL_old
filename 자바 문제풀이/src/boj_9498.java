import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_9498 {
    
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        // StringTokenizer st = new StringTokenizer(str, " ");

        int score = Integer.parseInt(str);

        if (score >= 90) {
            System.out.println("A");
        } 
        else if (score >= 80) {
            System.out.println("B");
        }
        else if (score >= 70) {
            System.out.println("C");
        }
        else if (score >= 60) {
            System.out.println("D");
        }
        else {
            System.out.println("F");
        }



    }
}