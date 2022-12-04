package java07;

public class stringbuffer {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer();

        sb.append("hello");
        sb.append(" ");
        sb.append("world");

        String result = sb.toString();
        System.out.println(result);
    }
    
}
