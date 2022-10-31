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

   ```JavaScript
   <body>
   <button id="btn">버튼</button>
   <p id="counter">0</p>

   <script>
     const btn = document.querySelector('#btn')
     let countNum = 0

     // 이벤트 핸들러 작성
     btn.addEventListener('click', function (event) {
       // console.log(event)
       const pTag = document.querySelector('#counter')

       countNum += 1

       pTag.innerText = countNum
     })
   </script>
   ```

2. input 입력값 실시간으로 출력하기

   ```JavaScript
   <body>
     <input type="text" id="text-input" />
     <p></p>
     <script>
       // 1. input 선택
       const inputTag = document.querySelector("#text-input");

       // 2. 이벤트 핸들러 부착
       inputTag.addEventListener("input", function (event) {
         const pTag = document.querySelector("p");
         // 모든 정보는 event에 저장! .target을 통해 접근
         pTag.innerText = event.target.value;
       });
     </script>
   </body>
   ```

3. 입력값 실시간 출력 + button 클릭 시 출력

   ```JavaScript
   <body>
      <h1></h1>
      <button id="btn">클릭</button>
      <input type="text" />

      <script>
         const btn = document.querySelector("#btn");
         // btn이 클릭 되면 함수 실행
         btn.addEventListener("click", function (event) {
           // h1 태그 선택
           const h1Tag = document.querySelector("h1");
           // 클래스 blue 토글
           h1Tag.classList.toggle("blue");
         });

         // input
         const inputTag = document.querySelector("input");

         // input에 값이 입력되면 함수 실행
         inputTag.addEventListener("input", function (event) {
           // h1 태그 실행
           const h1Tag = document.querySelector("h1");
           // input값을 태그의 컨텐츠로 채우기
           h1Tag.innerText = event.target.value;
         });
      </script>
   </body>
   ```

## Event 취소

### `event.preventDefault()`

✔ 현재 Event의 기본 동작 중단
✔ HTML 요소의 기본 동작을 작동하지 않게 막음
✔ HTMl 요소의 기본 동작 예시

- a 태그: 클릭 시 특정 주소로 이동
- form 태그: form 데이터 전송

### 실습

1. 복사 방지

```JavaScript
   <body>
     <div>
       <h1>정말 중요한 내용</h1>
     </div>

     <script>
       // 복사 방지 코드
       const h1Tag = document.querySelector("h1");
       h1Tag.addEventListener("copy", function (event) {
         event.preventDefault();
         // 경고 문구 출력
         alert("복사 할 수 없습니다.");
       });
     </script>
   </body>
```

## Event 종합 실습

### [참고] lodash 라이브러리

✔ 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리  
✔ array, object 등 자료 구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수 제공  
✔ ex: reverse, sortBy, range, random...

### 실습 진행

1. 버튼 클릭 시 랜덤 로또 번호 6개 출력

```JavaScript
   <body>
     <h1>로또 추천 번호</h1>
     <button id="lotto-btn">행운 번호 받기</button>
     <div id="result"></div>

     <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
     <script>
       // 버튼 선택하기
       const button = document.querySelector("#lotto-btn");
       button.addEventListener("click", function () {
         // 컨테이너 만들기
         const ballContainer = document.createElement("div");
         ballContainer.classList.add("ball-container");

         // 랜덤 숫자 6개 만들기
         // lodash 라이브러리 이용
         const numbers = _.sampleSize(_.range(1, 46), 6);

         // 공 만들기
         numbers.forEach((number) => {
           const ball = document.createElement("div");
           ball.classList.add("ball");
           ball.innerText = number;
           ball.style.backgroundColor = "crimson";
           // 공을 컨테이너의 자식으로 추가
           ballContainer.appendChild(ball);
         });
         // 컨테이너를 결과 영역의 자식으로 추가
         const result = document.querySelector("#result");
         result.appendChild(ballContainer);
       });
     </script>
   </body>
```

2. CREATE, READ 기능이 있는 todo app 만들기

```JavaScript
   <body>
     <form action="#">
       <input type="text" class="inputData" />
       <input type="submit" value="Add" />
     </form>
     <ul></ul>

     <script>
       const formTag = document.querySelector("form");

       const addTodo = function (event) {
         // 제출 시 주소 이동을 막기 위해 이벤트 취소
         event.preventDefault();

         // 입력값 가져오기
         const inputTag = document.querySelector(".inputData");
         const data = inputTag.value;

         // .trim() 양쪽 공백 제거 -> 공백을 제거 했을 때 문자값이 있다면
         if (data.trim()) {
           const liTag = document.createElement("li");
           liTag.innerText = data;

           const ulTag = document.querySelector("ul");
           ulTag.appendChild(liTag);
         } else {
           alert("할 일을 입력하세요");
         }
         event.target.reset();
       };

       formTag.addEventListener("submit", addTodo);
     </script>
   </body>
```

✔ 콜백 함수가 길어질 경우 이후 유지보수를 위해 함수를 밖으로 빼서 호출할 수 있다.
