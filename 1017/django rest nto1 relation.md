# Django REST framework - N:1 Relation
## GET
0. `CommentSerializer` 생성
![image](https://user-images.githubusercontent.com/109324637/196172480-6143cf8d-914f-4f28-bd37-b9b424d6453e.png)  

### GET-List
1. urls, views 작성
   ![image](https://user-images.githubusercontent.com/109324637/196172740-8eeed8c8-af79-4ee0-9997-f13f13039dc8.png)
   ![image](https://user-images.githubusercontent.com/109324637/196172997-9f250fe1-f9fd-4307-a49e-42fccfdd6720.png)
2. 응답 확인
   ![image](https://user-images.githubusercontent.com/109324637/196173142-a0b049e1-8f55-4be2-9d52-3ed999fbbdbb.png)
---
### GET-Detail
1. urls, views 작성
   ![image](https://user-images.githubusercontent.com/109324637/196173589-9125ffa6-9c87-4493-9f51-7e9847c3c41f.png)
   ![image](https://user-images.githubusercontent.com/109324637/196173680-d3289f9c-1c15-4e3d-9d72-a8b698468bfb.png)
2. 응답 확인
   ![image](https://user-images.githubusercontent.com/109324637/196173854-225f096b-4af0-451c-bfaa-904e6d653adc.png)

## POST
1. urls, views 작성
   ![image](https://user-images.githubusercontent.com/109324637/196174633-46f6c1bf-1d83-4164-bf5d-8d5bbf4d2eb0.png)
   ![image](https://user-images.githubusercontent.com/109324637/196174945-b091e896-142a-46d5-bb38-8ef6cf245346.png)  

### `.save()`의 인자값
✔ `save()` 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있다.  
✔ `CommentSerializer`를 통해 serialize되는 과정에서 인자로 넘어온 `aricle_pk`에 해당하는 article 객체를 추가적인 데이터로 넘겨서 저장  
✔ 이전의 ModelForm의 `commit=False`와 유사  

2. 응답 확인, 그러나...
   ![image](https://user-images.githubusercontent.com/109324637/196176475-3483a8d0-868e-4475-8d40-b465fd064bd7.png)  
   ✔ 에러 발생

### 읽기 전용 필드 설정
✔ **`read_only_fields`**를 사용해 외래 키 필드를 '**읽기 전용 필드**'로 설정  
✔ 데이터를 전송하는 시점에 '**해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에 출력**'하도록 한다.  
![image](https://user-images.githubusercontent.com/109324637/196177136-153b72a8-ef2d-4e87-8801-2db3439c5bde.png)

3. 다시 응답 확인해보기
![image](https://user-images.githubusercontent.com/109324637/196177207-7e02b721-1535-4492-8a45-4d4d62068933.png)

## DELETE & PUT
1. view 함수 작성
   ![image](https://user-images.githubusercontent.com/109324637/196177500-28ce0dae-9ee6-4017-b4b0-d4d8552e0137.png)
2. delete 응답 확인
   ![image](https://user-images.githubusercontent.com/109324637/196177614-c134d9d0-7a35-410a-b06b-1910ffee3146.png)
3. put 응답 확인
   ![image](https://user-images.githubusercontent.com/109324637/196177852-995ac073-dc40-4db3-92e8-1eb91dbed3c5.png)  

## N:1 역참조 데이터 조회
1. 특정 게시글에 작성된 **댓글 목록 출력**하기
   - 기존 필드 override
2. 특정 게시글에 작성된 **댓글의 개수 출력**하기
   - 새로운 필드 추가  
  
### 특정 게시글에 작성된 댓글 목록 출력하기
1. `PrimaryKeyRelatedField()`
   ![image](https://user-images.githubusercontent.com/109324637/196180014-ba8b4109-7b39-4523-941c-82ce491865ee.png)
   ![image](https://user-images.githubusercontent.com/109324637/196180406-ee30b41d-ea87-4b32-87a0-f2f11543b416.png)  
2. Nested relationships(새로운 필드 생성)
   ![image](https://user-images.githubusercontent.com/109324637/196180661-94467dab-4716-400f-af9e-ab60d8b03e9e.png)
   ![image](https://user-images.githubusercontent.com/109324637/196180786-2e0eb731-c967-4e70-bede-d6d655972b97.png)  
   ✔ comment의 상세한 내용까지 확인할 수 있다.  

### 특정 게시글에 작성된 댓글의 개수 출력하기
1. 새로운 필드 추가 `Article Detail`
   ![image](https://user-images.githubusercontent.com/109324637/196181224-bdb9524f-c375-4acc-b345-9cebf6c7d1f4.png)
2. 응답 확인
   ![image](https://user-images.githubusercontent.com/109324637/196181615-0812eff7-48e3-4cd2-b9d2-3fae1d5dff73.png)  

### [주의] 읽기 전용 필드 지정
✔ 특정 필드를 override 혹은 추가한 경우 `read_only_fields`가 작동하지 않는다.  
![image](https://user-images.githubusercontent.com/109324637/196182202-80ff0756-9905-49b8-ab8f-221f11e235b6.png)

## Django shortcuts functions
### `get_object_or_404()`
![image](https://user-images.githubusercontent.com/109324637/196182891-6680dfd2-1f86-42a6-98c5-73ac2d58f4bd.png)  
✔ managers objects에서 `get()`을 호출하지만, 해당 객체가 없을 때 HTTP404를 일으킨다.  
### `get_list_or_404()`
![image](https://user-images.githubusercontent.com/109324637/196183361-25751ed0-9f87-4447-b0db-27b3ec233795.png)  
✔ managers objects에서 `filter()`을 호출하지만, 해당 객체가 없을 때 HTTP404를 일으킨다.  
### 왜 사용해야 될까?
✔ 클라이언트 입장에서 '서버에 오류가 발생하여 요청을 수행할 수 없다(500)'라는 원인이 정확하지 않은 에러를 마주하기보다는, 서버가 적절한 예외처리를 하고 올바른 에러를 전달하는 것 또한 중요!