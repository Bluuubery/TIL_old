import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class boj_3052 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    HashSet<Integer> hashSet = new HashSet<>();

    for (int i = 0; i < 10; i++) {
      int n = Integer.parseInt(br.readLine());
      hashSet.add(n % 42);
    }

    System.out.println(hashSet.size());
  }
}
