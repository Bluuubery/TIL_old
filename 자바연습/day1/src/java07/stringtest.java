package java07;

import java.util.Arrays;

public class stringtest {
    public static void main(String[] args) {
        // String a = "hello";
        // String b = "world";
        // String c = "hello";
        // String d  = new String("hello");

        // System.out.println(a.equals(b));
        // System.out.println(a.equals(c));
        // System.out.println(a.equals(d));

        // System.out.println(a == c);
        // System.out.println(a == d);

        // String a = "Hello World";
        // System.out.println(a.indexOf("r"));
        // System.out.println(a.indexOf("x"));
        
        // String a = "Hello World";
        
        // System.out.println(a.contains("Hello"));
        // System.out.println(a.contains("good"));

        // String a = "Hello World";
        // System.out.println(a.charAt(8));
        // System.out.println(a.charAt(100));

        // System.out.println(a.replaceAll("World", "Java"));

        // System.out.println(a.substring(0, 5));

        // System.out.println(a.toUpperCase());
        // System.out.println(a.toLowerCase());

        String a = "a-b-c-d";
        String[] result = a.split("-");
        System.out.println(Arrays.toString(result));

        System.out.println(String.format("%.4f", 3.141592));
    }
}
