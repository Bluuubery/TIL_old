import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class boj_8958 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(br.readLine());

    String[] arr = new String[T];

    for (int i = 0; i < arr.length; i++) {
      arr[i] = br.readLine();
    }

    for (int i = 0; i < arr.length; i++) {
      int sum = 0;
      int score = 0;

      for (int j = 0; j < arr[i].length(); j++) {
        if (arr[i].charAt(j) == 'O') {
          sum++;
        } else {
          sum = 0;
        }
        score += sum;
      }
      System.out.println(score);
    }
  }
}
