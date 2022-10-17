# Django REST framework - Single Model
✔ 단일 모델의 data를 Serialization 하여 JSON 데이터를 응답하는 Django 서버 구축
## 사전 준비
1. postman 설치
2. models migrate
3. json 더미데이터 load하기
4. `djangorestframework` 설치하기  

## ModelSerializer
### Model Serializer  
✔ 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut제공
1. Model 정보에 맞춰 자동으로 필드 생성  
2. serializer에 대한 유효성 검사기를 자동으로 생성
3. `.create() 및 .update()`의 간단한 기본 현 포함    
---
1. Model Serializer 작성하기  
   ![image](https://user-images.githubusercontent.com/109324637/196107232-f7487326-7c15-4f98-aa19-a21d7feb2258.png)  
2. shell_plus 실행 및 ArticeListSerializer import
   ![image](https://user-images.githubusercontent.com/109324637/196110949-d5df7ff3-dda5-4632-b5f8-69a96f6880a8.png)  
3. 인스턴스 구조 확인하기
   ![image](https://user-images.githubusercontent.com/109324637/196111077-4643dd0d-29d2-4ec3-abd3-5ea624a522df.png)  
4. Model instance 객체 serialize
   ![image](https://user-images.githubusercontent.com/109324637/196111354-0e2d541a-559b-4b7e-a3ce-7d11b81e641f.png)  
5. QuerySet 객체 serialize
   ![image](https://user-images.githubusercontent.com/109324637/196111870-a87e9bf1-139b-43f5-a48d-b775611b2dee.png)  
   ✔ QuerySet 객체는 에러가 발생한다...!  
6. `Many = True` 옵션 설정
   ![image](https://user-images.githubusercontent.com/109324637/196112155-888c0b34-0e4e-4b36-9131-79d38b40dba2.png)  
   ✔ 정상적으로 출력이 된다.
## RESTful API - Article
### GET - List
1. url 및 view 함수 작성
   ![image](https://user-images.githubusercontent.com/109324637/196113115-4bbda654-b77d-43d0-b168-9333c82eaa01.png)
   ![image](https://user-images.githubusercontent.com/109324637/196113015-764ea3a7-9dd4-4233-b1a3-ccee1c8580c3.png)  
   ✔ 게시글 데이터 목록 조회하기  
   ✔ DRF에서 **`api_view` 데코레이터 작성은 필수**
2. 응답 확인
   ![image](https://user-images.githubusercontent.com/109324637/196113447-db660d2b-46bb-4436-a519-ee67f678811d.png)
   ![image](https://user-images.githubusercontent.com/109324637/196113800-eab22aad-2472-4d2c-a69d-ae57b8bff263.png)  
   ✔ Postman으로 확인 할 수 있음  

### `api_view` decorator  
✔ DRF **view 함수가 응답해야 하는 HTTP 메서드 목록**을 받음  
✔ **기본적으로 GET 메서드만 허용되며 허용되지 않은 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답**  

---
### GET - Detail
1. `ArticleSerializer` 정의
   ![image](https://user-images.githubusercontent.com/109324637/196115110-e26b4fa2-5ff1-4957-af56-6f4a6797f579.png)  
2. url 및 view 함수 정의
   ![image](https://user-images.githubusercontent.com/109324637/196115256-43ca231c-c81d-43ee-8ea4-08197f02db6a.png)
   ![image](https://user-images.githubusercontent.com/109324637/196115481-c91dbd8b-e0c7-4a60-aaf5-6e2bcf5cf59f.png)
3. 응답 확인
   ![image](https://user-images.githubusercontent.com/109324637/196115745-6a2328a6-4267-494e-96ca-16ee45f63bbc.png)  

---
### POST
✔ 요청에 대한 **데이터 생성이 성공했을 때는 201 Created 상태 코드**를, **실패 했을 경우에는 400 Bad request**를 응답
1. view 함수 작성
   ![image](https://user-images.githubusercontent.com/109324637/196116822-78a6a458-7a82-4275-ac8d-1d35666c684b.png)  
   ✔ method 기준으로 구분하기 때문에 새로운 view함수를 작성하는 게 아니라 밑에 추가해준다.  
2. 응답 확인
   ![image](https://user-images.githubusercontent.com/109324637/196117550-6dc8b228-310b-4e34-9c3e-fb172d6102b5.png)
3. `raise_exception=True`
   ![image](https://user-images.githubusercontent.com/109324637/196169134-915c96c1-f741-4ee9-acd8-7d7b1e470a58.png)  
   ✔ `raise_exception=True`를 설정해주면 자동으로 예외 처리돼 HTTP400을 반환한다.  
--- 
### DELETE
1. view함수 작성
   ![image](https://user-images.githubusercontent.com/109324637/196169774-195d57e8-7013-4fb9-8bdc-3a99f1075eac.png)  
   ✔ 데이터 삭제에 성공했을 경우 **204 No Content** 반환  
2. 응답 확인
   ![image](https://user-images.githubusercontent.com/109324637/196170557-e116073b-f3a3-4d46-88a3-58ee262ee183.png)  
---
### PUT
1. view함수 작성
   ![image](https://user-images.githubusercontent.com/109324637/196171249-8b6f0428-d56b-4b09-a3ee-7a6cfe1b7de7.png)   
2. 응답 확인
   ![image](https://user-images.githubusercontent.com/109324637/196171498-b134b618-e4b4-4267-967e-19fa4f2222b8.png)  
### 