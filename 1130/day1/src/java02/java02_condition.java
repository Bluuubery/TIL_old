package java02;

public class java02_condition {
    public static void main(String[] args) {
        int month = 6;

        switch (month) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                System.out.println("31일");
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                System.out.println("30일");
                break;
            default:
                System.out.println("없어");
                break;
        }
    }
}
