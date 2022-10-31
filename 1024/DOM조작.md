# DOM 조작

## 개요

✔ DOM 조작 순서

1. 선택(select)
2. 조작(maipulation)

## 선택 관련 메서드

1. `document.querySelector(selector)`  
   ✔ 제공한 선택자와 일치하는 element 한 개 선택  
   ✔ 제공한 CSS selector를 만족하는 첫 번째 element 객체 반환(없다면 null 반환)
2. `document.querySelectorAll(selector)`  
   ✔ 제공한 선택자와 일치하는 여러 element를 선택  
   ✔ 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자로 받는다.  
   ✔ 제공한 CSS selector를 만족하는 NodeList 반환

### 선택 관련 메서드 실습

```JavaScript
   <script>
     console.log(document.querySelector("#title"));
     console.log(document.querySelectorAll(".text"));

     console.log(document.querySelector(".text"));
     console.log(document.querySelectorAll("body > ul > li"));

     liTags = document.querySelectorAll("body > ul > li");
     liTags.forEach((element) => {
       console.log(element);
     });
   </script>
```

![image](https://user-images.githubusercontent.com/109324637/198923327-18308474-e715-4b5c-83e1-b2dc33d8730f.png)

### NodeList

✔ index로만 각 항목에 접근 가능  
✔ 배열의 `forEach` 메서드 및 다양한 배열 메서드 사용 가능  
✔ querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지는 않는다. (기본적으로 동적이지만 querySelectorAll()에 의해 반환될 때는 정적!)

## 조작 관련 메서드

### 생성: `document.createElement(tagName)`

✔ 작성한 tagName의 HTML 요소를 생성하여 반환

### 입력: `Node.innerText`

✔ Node 객체와 그 자손의 텍스트 컨텐츠(DOMstring)을 표현

### 추가: `Node.appendChild()`

✔ 한 Node를 특정 부모 Node의 자식 NodeList중 마지막 자식으로 삽입  
✔ 한번에 오직 하나의 Node만 추가 가능  
✔ 추가한 Node 객체를 반환  
✔ 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동

### 삭제: `Noede.removeChild()`

✔ DOM 에서 노드 제거

### 조작 관련 메서드 실습

```JavaScript
  <script>
    // 태그 생성
    const h1Tag = document.createElement('h1')

    // 태그안에 컨텐츠를 작성하고
    h1Tag.innerText = 'DOM 조작'

    // 부모 div 태그를 가져와서
    const div = document.querySelector('div')

    // div 태그의 자식 요소로 추가
    div.appendChild(h1Tag)

    // div의 h1 요소 삭제
    div.removeChild(h1Tag)
  </script>
```

```JavaScript
  <script>
    // a 태그 생성
    const aTag = document.createElement('a')

    // a 태그 속성 추가
    aTag.setAttribute('href', 'https://google.com')

    // a 태그 컨텐츠 추가
    aTag.innerText = '구글'

    // div 태그 선택 후 자식 태그로 a 태그 추가
    const divTag = document.querySelector('div')
    divTag.appendChild(aTag)

    // hi 태그 선택 후 클래스 값 조정
    const h1Tag = document.querySelector('h1')
    h1Tag.classList.toggle('blue')
  </script>
```

### 조작관련 메서드(속성 조회 및 설정)

✔ `Element.getAttrivbute(attributeName)`

- 해당 요소의 지정된 값(문자열)을 반환
- 인자(attributeName)는 값을 얻고자 하는 속성의 이름

✔ `Element.setAttribute(name, value)`

- 지정된 요소의 값을 설정
- **속성이 이미 존재하면 값을 갱신**, 존재하지 않으면 이름과 값을 새 속성을 추가

### 속성 조회 및 설정 실습

![image](https://user-images.githubusercontent.com/109324637/197463088-0548eca7-919d-40c2-b6ec-9cb4c4d51c70.png)

![image](https://user-images.githubusercontent.com/109324637/197463153-4deca564-33c5-472c-bc26-c7c96a4a8b81.png)
