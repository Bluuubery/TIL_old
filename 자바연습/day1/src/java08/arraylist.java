package java08;

import java.util.ArrayList;

public class arraylist {
    public static void main(String[] args) {
        ArrayList<Number> arr = new ArrayList<>();

        arr.add(1);
        arr.add(2);
        arr.add(3);
        arr.add(4);

        // System.out.println(arr.get(2));
        // System.out.println(arr.size());
        // System.out.println(arr.contains(3));
        // System.out.println(arr.contains(5));
        System.out.println(arr.remove("3"));
    }
}
