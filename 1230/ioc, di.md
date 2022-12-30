# 제어의 역전(IoC) & 의존성 주입(DI)

## 제어의 역전

제어의 역전(IoC): **프로그램의 제어 흐름을 직접 제어하는 것이 아니라 외부에서 관리하는 것**

```java
public class OrderServiceImpl implements OrderService {

    // private final DiscountPolicy discountPolicy = new FixDiscountPolicy();
    private final DiscountPolicy discountPolicy = new RateDiscountPolicy();
}

```

기존에는 클라이언트 구현 객체가 스스로 필요한 서버 구현 객체를 생성, 연결 실행했다. -> 구현 객체가 스스로 프로그램의 제어 흐름을 조정함

허나 이렇게 할 경우 1. 할인 정책을 변경할 때 클라이언트 코드를 직접 수정해야하고(OCP 위반), 2. 추상화뿐만이 아니라 구현 객체에도 의존하는 문제가 발생한다.(DIP 위반)

---

```java
// Appconfig.java

public class AppConfig {
 
    public MemberService memberService() {
        return new MemberServiceImpl(memberRepository());
    }
 
    public OrderService orderService() {
        return new OrderServiceImpl(
                memberRepository(),
                discountPolicy());
     }
 
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }
 
    public DiscountPolicy discountPolicy() {
        return new FixDiscountPolicy();
 }
}
```

```java
// OrderServiceImpl.java

public class OrderServiceImpl implements OrderService {
    
    private final MemberRepository memberRepository;
    private final DiscountPolicy discountPolicy;
    
    public OrderServiceImpl(MemberRepository memberRepository, DiscountPolicy
discountPolicy) {
        this.memberRepository = memberRepository;
         this.discountPolicy = discountPolicy;
 }
 ...
}

```

**프로그램의 제어 흐름은 AppConfig(외부)가 가져가고 OrderServiceImpl은 자신의 로직만 실행하게 된다**



애플리케이션의 실제 동작에 필요한 구현 객체는 AppConfig가 생성하고, 생성한 객체 인스턴스의 참조(레퍼런스)를 생성자를 통해서 주입(연결)해준다.

`OrderServiceImpl` ->  `MemoryMemberRepository` , `FixDiscountPolicy`



![](assets/ioc,%20di.md/2022-12-30-22-46-43.png)

`OrderServiceImpl` 입장에서 생성자를 통해 어떤 구현 객체가 들어올지(주입될지)는 알 수 없다.

`OrderServiceImpl` 의 생성자를 통해서 어떤 구현 객체을 주입할지는 오직 외부( AppConfig )에서결정한다.

`OrderServiceImpl` 은 이제부터 실행에만 집중하면 된다.

## 의존성 주입(DI)

### 정적인 클래스 의존관계

![](assets/ioc,%20di.md/2022-12-30-22-52-43.png)

클래스가 사용하는 import 코드만 보고 파악할 수 있다  

### 동적인 객체 인스턴스 의존 관계

![](assets/ioc,%20di.md/2022-12-30-22-53-05.png)

애플리케이션 실행 시점에 실제 생성된 객체 인스턴스의 참조가 연결된 의존 관계

**의존성 주입(DI):** 애플리케이션 실행 시점(런타임)에 외부에서 실제 구현 객체를 생성하고 클라이언트에 전달해서, 클라이언트와 서버의 실제 의존관계가 연결 되는 것

## IoC컨테이너, DI컨테이너

AppConfig처럼 객체를 생성하고 관리하면서 의존관계를 연결해주는 것

최근에는 의존관계 주입에 초점을 맞춰 주로 DI컨테이너라고 한다.