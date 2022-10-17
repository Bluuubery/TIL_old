# HTTP
## 개요
✔ HyperText Transfer Protocol  
✔ HTML 문서와 같은 resource들을 가져올 수 있도록 하는 프로토콜  
✔ 웹에서 이루어지는 모든 데이터 교환의 기초  
✔ '클라이언트 - 서버 프로토콜'이라고도 부름  
✔ 클라이언트와 서버는 다음과 같은 개별적인 메시지 교환에 의해 통신  
- 요청(request)
  - 클라이언트에 의해 전송되는 메시지
- 응답(response)
  - 서버에서 응답으로 처리되는 메시지  
## HTTP 특징
### Stateless(무상태)
✔ 동일한 연결(connection)에서 연속적으로 수행되는 두 요청 사이에 링크가 없음  
✔ 즉, 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않는다.  
✔ 이는 특정 페이지와 일관되게 상호작용하려는 사용자에게 문제가 될 수 있음  
✔ 쿠키와 세션이용
### HTTP Request Methods
✔ GET
- 서버에 리로스의 표현을 요청
- GET을 사용하는 요청은 데이터만 검색해야 한다.  

✔ POST
- 데이터를 지정된 리소스에 제출
- 서버의 상태를 변경

✔ PUT
- 요청한 주소의 리소스를 수정

✔ DELETE
- 지정된 리소스를 삭제
### HTTP response status code
✔ 특정 요청이 성공적으로 완료되었는지 여부
1. Informational responses(100 - 199)
2. Successful responses(200 - 299)
3. Redirection messages(300 - 399)
4. Client error responses(400 - 499)
5. Server error responses(500 - 599)

## Identifying Resources on the Web
### URI
✔ Uniform Resources Identifier(통합 자원 식별자)  
✔ URL을 URI의 하나(웹 주소)!  
✔ URN: 특정 이름 공간에서 이름으로 리소스를 식별하는 URI
### URL
✔ Uniform Resource Locator (통합 자원 위치)  
✔ 웹에서 주어진 리소소의 주소  
✔ HTML, CSS, 이미지, JS...
### URL의 구조
![image](https://user-images.githubusercontent.com/109324637/196075425-d0cfec23-3137-4c1b-b5c1-fb0e4b7f76e5.png)   
1. Scheme (Protocol)  
   ✔ 브라우저가 리소르를 요청하는데 사용하는 트로토콜   
   ✔ 브라우저가 사용하는 규약을 나타낸다.  
2. Authority  
   ✔ Shceme 다음에 `://` 문자 패턴으로    
   ✔ Domain과 Port를 모두 포함하며 :(콜론)으로 구분됨  
   1. Domain Name  
   ✔ 요청 중인 웹 서버  
   ✔ 직접 IP 주소를 사용하는 것도 가능하지만, 외우기 어렵기 때문에 주로 Domain Name으로 사용
   2. Port  
   ✔ 웹 서버의 리소스에 접근하는데 사용되는 기술적인 Gate  
   ✔ HTTP의 표준 포트 (HTTP - 80, HTTPS - 443)은 생략 가능  
   ✔ Django: 8000  
3. Path  
   ✔ 웹 서버의 리소스 경로  
   ✔ 초기에는 실제 파일의 물리적 위치를 나타냈지만, 오늘은 추상화된 형태의 구조 표현  
4. Parameters  
   ✔ 웹 서버에 제공하는 추가적인 데이터  
   ✔ `&`기호로 구분되는 Keu-Value 쌍 목록  
   ✔ 리소스를 응답하기 전에 파라미터를 사용하여 추가 작업 수행 가능  
5. Anchor  
   ✔ 리소스의 다른 부분에 대한 앵커  
   ✔ 리소스 내부 일종의 '북마크'를 나타내며 브라우저에 해당 북마크 지점에 있는 콘텐츠를 표시  
   ✔ Fragment identifier(부분 식별자) `#`이후 부분은 서버에 전송되지 않고 브라우저가 해당 지점으로 이동 될 수 있도록 한다.  
   

