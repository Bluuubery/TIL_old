# DOM

## Browser APIs

✔ 웹 브라우저에 내장된 API로 웹 브라우저가 현재 컴퓨터 환경에 관한 데이터를 제공하거나, 오디오를 재생하는 등 여러가지 유용하고 복잡한 일 수행 가능

- DOM
- Geolocation API
- WebGL

## DOM 개요

✔ 문서 객체 모델(Document Object Model)  
✔ 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM구조에 접근할 수 있는 방법을 제공

- 문서 구조, 스타일, 내용 등을 쉽게 변경할 수 있도록 도움
- HTML 컨텐츠를 추가, 제거, 변경하고 동적으로 페이지에 스타일 추가하는 등 HTML/CSS 조작 가능

✔ HTML 문서를 구조화 하여 각 요소를 **객체(object)**로 취급

![dom트리](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/DOM-model.svg/1200px-DOM-model.svg.png)

✔ DOM 은 문서를 논리 트리로 표현
✔ 웹 페이지는 일종의 문서(document)  
✔ DOM은 웹페이지의 객체 지향 표현이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음

## DOM에 접근하기

✔ 모든 웹 브라우저가 이미 DOM 구조를 사용하고 있기 때문에 특별히 해야할 일은 없다.

### DOM의 주요 객체

- **`window`**
- **`document`**
- `navigator, location, history, screen` 등

### `window` object

✔ DOM을 표현하는 창  
✔ 가장 최상위 객체(작성 시 생략 가능)  
✔ 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타낸다.

### `window`의 메서드

```web
<!-- 새 탭 열기 -->
window.open()

<!-- 경고 대화 상자 표시 -->
window.print()

<!-- 인쇄 대화 상자 표시 -->
window.alert()
```

### `document` object

![image](https://user-images.githubusercontent.com/109324637/197458469-acd8bcac-0a3b-49f4-ab15-813804ddd586.png)

✔ 브라우저가 불러온 웹페이지  
✔ 페이지 컨텐츠의 진입점 역할을 하며, `<body>` 등과 같은 수많은 다른 요소들을 포함

### `document`의 속성 예시

![image](https://user-images.githubusercontent.com/109324637/197458659-0fa9b74d-b35d-4439-96f2-e46147e071d5.png)  
✔ 문서의 제목

## [참고] 파싱(Parsing)

✔ 구문 분석, 해석  
✔ 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
