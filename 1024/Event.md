# Event

## 개요

✔ **Event**란 프로그래밍하고 있는 시스템에서 일어나는 사건(action) 혹은 발생(occurence)인데, 우리가 원한다면 그것들에 어떠한 방식으로 응답할 수 있도록 시스템이 말해주는 것  
✔ ex: 클립, 키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등등...

## Event object

✔ 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 존재  
✔ DOM 요소는 Event를 **'수신'**  
✔ 받은 Event **'처리'**

- Event 처리는 주로 `addEventListner()`라는 Event 처리기를 다양한 html 요소에 **'부착'** 해서 사용

## Event handler - `addEventListner()`

✔ **대상**에 **특정 event**가 발생하면, **할 일**을 등록한다

```JavaScript
EventTarget.addEventListner(type, listner)
```

✔ 지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정  
✔ Event를 지원하는 모든 객체(Element, Document, Window 등)을 대상(EventTarget)으로 지정 가능

✔ `type`

- 반응할 Event 유형을 나타내는 대소문자 구문 문자열
- `input, click, submit...`

✔ `listner`

- 지정된 타입의 Event를 수신할 객체
- JavaScript function 객체(콜백함수)이어야 한다.
- 콜백 함수는 발생한 Event 데이터를 가진 Event 객체를 유일한 매개변수로 받는다.

### Event 실습

1. 버튼 카운트  
   ![image](https://user-images.githubusercontent.com/109324637/197466519-6557ed15-4b06-4fd5-b9c8-185ba956dbd1.png)

2. input 입력값 실시간으로 출력하기  
   ![image](https://user-images.githubusercontent.com/109324637/197467466-a07b1ebf-c570-4a5a-a6d1-681a5ca8e588.png)

3. 입력값 실시간 출력 + button 클릭 시 출력  
   ![image](https://user-images.githubusercontent.com/109324637/197468430-dfe6db85-8479-4147-949e-7da013aa93b3.png)

## Event 취소

### `event.preventDefault()`

✔ 현재 Event의 기본 동작 중단  
✔ HTML 요소의 기본 동작을 작동하지 않게 막음  
✔ HTMl 요소의 기본 동작 예시

- a 태그: 클릭 시 특정 주소로 이동
- form 태그: form 데이터 전송

### 실습

1. 복사 방지  
   ![image](https://user-images.githubusercontent.com/109324637/197469347-c571697c-391f-44aa-aafc-f5f052f3507e.png)

## Event 종합 실습

### [참고] lodash 라이브러리

✔ 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리  
✔ array, object 등 자료 구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수 제공  
✔ ex: reverse, sortBy, range, random...

### 실습 진행

1. 버튼 클릭 시 랜덤 로또 번호 6개 출력  
   ![image](https://user-images.githubusercontent.com/109324637/197471549-250c7a02-8370-42ad-8224-4fcc7b52752d.png)

2. CREATE, READ 기능이 있는 todo app 만들기  
   ![image](https://user-images.githubusercontent.com/109324637/197472646-e5086188-159d-402d-a697-1d7cce0ddd45.png)  
   ✔ 콜백 함수가 길어질 경우 이후 유지보수를 위해 함수를 밖으로 빼서 호출할 수 있다.
