package java06;

public class PersonTest {
    public static void main(String[] args) {
        Person p1 = new Person();

        p1.name = "kim";
        p1.age = 24;
        p1.hobby = "Gym";

        Person p2 = new Person();
        
        p2.name = "Lee";
        p2.age = 25;
        p2.hobby = "Netflix";

        System.out.println(Person.personCount);
        // System.out.println(p1.personCount); // 인스턴스로 접근할 수는 있으나 권장은 되지 않는다!
        
    }
}