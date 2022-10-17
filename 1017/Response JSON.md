# Response JSON
## 개요  
✔ 서버는 페이지(html)뿐만 아니라 다양한 데이터 타입을 응답할 수 있다.  
✔ JSON 데이터를 응답하는 서버로의 변환  
✔ 화면은 다른 Front-end Framework가 구성  
## 사전 준비
1. migrate 진행 (사진 생략)
2. 준비된 파일 load해서 초기 데이터 입력
   ![image](https://user-images.githubusercontent.com/109324637/196099611-f4ae0c00-6bc9-4c7a-a22b-f32ebae1a112.png)  
3. url 살펴보기
   ![image](https://user-images.githubusercontent.com/109324637/196099901-c54bb1e5-40b2-4c0a-9d0f-77c5b4946601.png)  
   ![image](https://user-images.githubusercontent.com/109324637/196099945-2655d4e1-fe40-42e3-82cc-1a2eb63d8926.png)  

## Response
1. HTML 응답
2. `JsonResponse()`을 사용한 JSON 응답
3. Django Serializer를 사용한 JSON 응답
4. **Djano REST framework**를 사용한 JSON 응답

### 1. HTML 응답

![image](https://user-images.githubusercontent.com/109324637/196100540-46514975-aab8-454d-964a-e0416ef1cd14.png)
![image](https://user-images.githubusercontent.com/109324637/196100387-033a72f3-12cc-43fe-bdb4-38d17e9212fe.png)
![image](https://user-images.githubusercontent.com/109324637/196100747-03d4acc7-ac9b-4590-a0e0-b166f3ca05b2.png)  
✔ 기존에 하던 방식

### 2. `JsonResponse()`를 사용한 JSON 응답
![image](https://user-images.githubusercontent.com/109324637/196101232-8b8e9ab5-639b-4f1e-8a19-64c23518ecb3.png)
![image](https://user-images.githubusercontent.com/109324637/196101356-f15f53cf-65d7-4ca7-b708-0e1261a269d7.png)
![image](https://user-images.githubusercontent.com/109324637/196101424-1c9fd8d7-9240-4ea4-bb28-432b6c2d8821.png)    
✔ JSON 형태로 반환한다.

### 3. Django Serializer를 사용한 JSON 응답
![image](https://user-images.githubusercontent.com/109324637/196101823-e7bb28f8-b724-4894-a1b2-f0d6193ef28c.png)
![image](https://user-images.githubusercontent.com/109324637/196102092-7d36ec3e-7f5b-467b-ae2a-b2bfe77c4fc1.png)  
✔ 모델 구조를 기반으로 djang가 알아서 JSON 형태로 반환한다.
#### Serialization
- 데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고, **나중에 재구성할 수 있는 포맷으로 변환**하는 과정  
- **"나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정"**  
- Django의 `serialize()`는 Queryset 및 Model Instance를 JSON 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어 준다.  

### **4. Django REST framework를 사용한 JSON 응답**
✔ **Django REST framework**  
  - Django에서 Restfrul API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
  
![image](https://user-images.githubusercontent.com/109324637/196103167-ea0b74ad-4db4-4691-9dbc-afd71e2868f8.png)  
✔ DRF 설치  
![image](https://user-images.githubusercontent.com/109324637/196103366-f74e04d4-602d-4acf-a72f-ccaf60f1f769.png)
✔ ModelForm과 구조가 유사하다  
![image](https://user-images.githubusercontent.com/109324637/196103659-a9552465-8e78-439f-aeb8-45ac6a915d2f.png)  
![image](https://user-images.githubusercontent.com/109324637/196103751-dab2e187-5524-458f-ac26-55062bba6705.png)  
✔ DRF 템플릿 기반으로 JSON 파일이 출력되는 문서를 제공해준다.  
![image](https://user-images.githubusercontent.com/109324637/196103949-f6af0dd3-7bc5-4cb1-aeb7-dd41ad212300.png)  
✔ 브라우저상에는 JSON을 문서(Text)로 출력해주지만 실제 코드상으론 JSON이 제공된다.  
### request 라이브러리를 이용하여 JSON 응답 받기
![image](https://user-images.githubusercontent.com/109324637/196104345-77823a1b-2448-4d1d-9dc9-f3f487734441.png) 
![image](https://user-images.githubusercontent.com/109324637/196104566-d10f6d5f-9851-4722-bedc-92505c470ff8.png)  
✔ 위와 같이 `requests`를 이용하여 JSON으로부터 필요한 데이터를 받을 수 있다.  