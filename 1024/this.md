# This

## 개요

✔ 어떠한 object를 가리키는 키워드  
✔ JavaScript의 함수는 **호출될 때 this를 암묵적으로 전달 받음**  
✔ JavaScript에서의 this는 일반적인 프로그래밍 언어와 다르게 동작  
✔ JavaScript는 해당 **함수의 호출 방식**에 따라 this에 바인딩 되는 객체가 달라진다.  
✔ 즉 함수를 선언할 때 결정되는 것이 아니라, 함수를 호출할 때 **함수가 어떻게 호출되었는지에 따라 동적으로 결정**

## this INDEX

1. 전역 문맥에서의 this
2. **함수 문맥에서의 this**

- 단순 호출
- Method(객체의 메서드로서)
- Nested

### 전역 문맥에서의 this

✔ 브라우저의 전역 객체인 window를 가리킨다.

- 전역 객체는 모든 객체의 유일한 최상위 객체를 의미

```JavaScript
console.log(this) // window
```

### 함수 문맥에서의 this

1. 단순 호출

- 전역 객체를 가리킨다.
- 전역은 브라우저에서는 window, Node.js는 global을 의미함

  ```JavaScript
  const myFunc = function() {
    console.log(this)
  }

  // 브라우저
  myFunc() // window

  // Node.js
  myFunc() // global
  ```

2. Method (Function in Object, 객체의 메서드로서)

- 메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩

  ```JavaScript
  const myObj = {
    data: 1,
    myFunc() {
      console.log(this) // myobj
      console.log(this.data) // 1
    }
  }

  myObj.myFunc() // myObj
  ```

3. Nested(Function 키워드)

- forEach의 콜백 함수에서의 this가 메서드의 객체를 카리키지 못하고 **전역 객체 window를 가리킴**
- 메서드가 아닌 **단순 호출**로 사용되었기 때문
- 이를 해결하기 위해 등장한 것이 **화살표 함수**
  ```JavaScript
  const myObj = {
    numbers: [1],
    myFunc() {
      console.log(this) //myObj
      this.numbers.forEach(function (number) {
      console.log(number) // 1
      console.log(this) // window)
    })
    }
  }
  ```

3. Nested (화살표 함수)

- 이전에 일반 function 키워드와 달리 메서드의 객체를 잘 가리킴
- 화살표 함수에서 this는 **자신을 감싼 정적 범위**
- 자동으로 한 단계 상위의 scope의 context를 바인딩
  ```JavaScript
  const myObj = {
    numbers: [1],
    myFunc() {
      console.log(this) //myObj
      this.numbers.forEach((number) => {
      console.log(number) // 1
      console.log(this) // myObj)
    })
    }
  }
  ```

## 화살표 함수

✔ 화살표 함수는 **호출의 위치와 상관 없이 상위 스코프를 가리킴**

✔ Lexical scope

- 함수를 어디서 호출하는지가 아니라 **어디에 선언**하였는지에 따라 결정
- static scope라고도 하며 대부분 프로그래밍 언어에서 따르는 방식
- 함수 내부에 함수는 화살표 함수를 쓰는 것 권장

### this와 `addEventListener`

✔ However...

- `addEventListner`에서의 콜백 함수는 특별하게 function 키워드의 경우 `addEventListner`를 호출한 대상(event.tartet)를 나타냄
- 반면 화살표 함수의 경우 상위 스코프를 지정하기 때문에 window 객체가 바인딩 된다.

✔ **`addEventListener`의 콜백 함수는 function 키워드를 사용!**

## 정리

✔ this는 호출되는 순간에 결정된다  
✔ 장점

- 함수(메서드)를 하나만 만들어서 여러 객체에서 재사용 할 수 있다.

✔ 단점

- 실수로 이어지기 쉽다

✔ 좋고 나쁘고를 판단하기보다는 어떻게 활용할 수 있을까를 생각하자!!
