package java05;

import java.util.Arrays;

public class java05 {
    public static void main(String[] args) {
        
        int[] arr = {1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6};

        int[] used = new int[10];

        for (int i : arr) {
            used[i]++;
        }

        System.out.println(Arrays.toString(used));
        
    }
}
