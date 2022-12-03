package java06;

public class Person {
    static int personCount;

    String name;
    int age;
    String hobby;

    public void info() {
        System.out.println("내 이름은" + name + "입니다");
        System.out.println("나이는" + age + ", 취미는" + hobby + "입니다.");
    }

}
