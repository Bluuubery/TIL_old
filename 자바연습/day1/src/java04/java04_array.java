package java04;

import java.util.Arrays;

public class java04_array {
    public static void main(String[] args) {
        // int[] score1;
        // int score2[];

        int[] score2 = new int[5];

        score2[0] = 11;
        score2[2] = 12;
        score2[3] = 13;
        score2[4] = 14;

        // for (int i = 0; i < score2.length; i++) {
        //     System.out.println(score2[i]);
        // }

        int [] arr = {1, 3, 5, 7, 9};
        
        for (int i : arr) {
            i *= 2;
            System.out.println(i);
        };

        System.out.println(Arrays.toString(arr));

    }
}
