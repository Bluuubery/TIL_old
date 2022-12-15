import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class boj_1546 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());

    double[] arr = new double[N];
    double maxScore = 0;

    StringTokenizer st = new StringTokenizer(br.readLine());

    for (int i = 0; i < arr.length; i++) {
      double score = Double.parseDouble(st.nextToken());
      arr[i] = score;

      if (score > maxScore) {
        maxScore = score;
      }
    }

    double sum = 0;

    for (int i = 0; i < arr.length; i++) {
      sum += (arr[i] / maxScore) * 100;
    }

    System.out.println(sum / N);
  }
}
