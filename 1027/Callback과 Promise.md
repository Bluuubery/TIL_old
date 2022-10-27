# Callback과 Promise

## 비동기 처리 방식의 문제점

✔ 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라 작업이 완료되는 순서에 따라 처리된다는 것  
✔ **실행 결과를 예상하면서 코드를 짤 수 없다**

## 콜백함수(Callback Function)

✔ **다른 함수의 인자로 전달되는 함수**  
✔ 시간이 걸리는 **비동기 작업이 왼료된 후 실행할 작업을 명시**하는 데 사용되는 콜백 함수를 비동기 콜백(asynchronous callback)이라 부른다.

### 콜백함수를 사용하는 이유

✔ 명시적인 호출이 아닌 특정한 조건 혹은 행동에 의해 호출되도록 작성할 수 있음  
✔ '요청이 들어오면', '이벤트가 발생하면', '데이터를 받아오면'등의 조건으로 이후 로직을 제어할 수 있음  
✔ **비동기 처리를 순차적으로 동작할 수 있게함**

### 콜백 지옥

![image](https://user-images.githubusercontent.com/109324637/198169329-3945ff70-3d13-4053-ad34-c984f20ccf7c.png)  
✔ 연쇄적으로 발생하는 비동기 작업을 순차적으로 진행할 수 있게함  
✔ 코드가 지나치게 깊어지는 문제가 발생할 수 있다.

## Promise

### 개요

✔ Callback Hell 문제를 해결하기 위해 등장한 **비동기 처리 객체**  
✔ '작업이 끝나면 실행 시켜 줄게' 라는 약속  
✔ **비동기 작업의 완료 또는 실패를 나나태는 객체**
✔ Promise 기반의 클라이언트가 바로 이전에 사용한 **Axios 라이브러리!**

- 성공에 대한 약속 `then()`
- 실패에 대한 약속 `cathch()`

### then & catch

✔ **`then(callback)`**

- 요청한 작업이 성공하면 callback 실행
- callback은 **이전 작업의 성공 결과를 인자로 받음**

✔ **`catch(callback)`**

- `then()`이 하나라도 실패하면 callback 실행
- callback은 이전 작업의 실패 객체를 인자로 전달 받음

✔ then 과 catch 모두 항상 promise 객체를 반환, 즉 계속해서 **`chaining`**을 할 수 있음  
✔ **axios로 처리한 비동기 로직이 항상 promise객체를 반환**, 그래서 계속 then을 이어 나가면서 작성 가능

### Promise가 보장하는 것(vs 비동기 콜백)

1. callback 함수는 JavaScript의 Event Loop가 현재 실행 중이 Call Stack을 완료하기 이전에은 절대 호출되지 않는다.

- Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출된다.

2. 비동기 작업이 성공하거나 실패한 뒤에 `.then()` 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작

3. `.then()`을 여러번 사용하여 여러 개의 callback 함수를 추가할 수 있다.(chaining)

- 각각의 callback은 주어진 순서대로 하나하나 실행된다.
- chaining은 Promise의 가장 뛰어난 장점

4. promise 방식은 비동기 처리를 마치 우리가 일반적으로 위에서 아래로 적는 방식처럼 코드를 작성할 수 있다.
