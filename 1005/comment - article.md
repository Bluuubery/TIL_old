# Django Relationship fields (N:1) (Comments - Article)
## Django Relationship fields 종류
1. OneToOneField() - 1:1  
2. ForeignKey() - N:1
3. ManyToManyField() - N:N

## ForeignKey(to, on_delete, **options)
✔ N:1 relationship을 담당하는 Django의 모델 필드 클래스  
✔ Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당  
✔ 2개의 필수 위치 인자
  1. 참조하는 **model class**
  2. **on_delete**옵션 
### on_delete
✔ 외래 키가 참조하는 객체가 사라졌을 때 외래 키를 가진 객체를 어떻게 처리할 지를 정의  
✔ 데이터 무결성을 위해서 중요한 설정!  
✔ 옵션 값
- **CASCADE**: 부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제  
- PROTECT, SET_NULL, SET_DEFAULT ...등 여러 옵션 존재  

## Comment 모델
### Comment Model 정의
![image](https://user-images.githubusercontent.com/109324637/193960205-fffe769e-9177-448d-9937-5ebb7bcc19b1.png)  
✔ 외래 키 필드는 ForeignKey 클래스 작성 위치와 관계 없이 필드 마지막에 작성된다.  
✔ 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)로 작성 권장  
### Migration 과정 진행
![image](https://user-images.githubusercontent.com/109324637/193960885-653c1536-77a9-44c9-8e64-9922242cee4d.png)  
![image](https://user-images.githubusercontent.com/109324637/193961084-2e998ad7-5b55-4226-9e66-6b310b8b1ff6.png)
✔ 변동 사항이 발생했으므로 다시 migration 진행  
✔ makemigrations -> migrate  
![image](https://user-images.githubusercontent.com/109324637/193986688-0460a4d8-2daa-4960-903d-c2bf0e948b0a.png)  
✔ '**[설정한 인스턴스 이름]_id**'로 외래키가 들어가있는 것을 확인할 수 있다  
## 댓글 생성해보기
### 0. shell_plus 실행  
![image](https://user-images.githubusercontent.com/109324637/193987126-aa5b9226-3371-4633-aab8-9f7301683efe.png)  
### 1. 그냥 생성하게 된다면...
![image](https://user-images.githubusercontent.com/109324637/193987429-22889857-2884-424e-a7d5-1ce0d8c8f83f.png)  
![image](https://user-images.githubusercontent.com/109324637/193987519-00cc91c9-d910-4c0b-a527-4d20ba0d8d35.png)  
✔ 참조하는 외래키 값이 없어서 에러 발생 (댓글을 단독으로 쓸 수 없음)   
### 2. Article을 먼저 생성하고 해당 Article에 댓글을 생성!
![image](https://user-images.githubusercontent.com/109324637/193987800-8931f583-1535-4e3c-91f3-cd04f3960f9f.png)
![image](https://user-images.githubusercontent.com/109324637/193988014-e5e3dde9-6176-407c-8704-f1e86fac2153.png)  
✔ 정상적으로 댓글이 생성된 것을 확인할 수 있다

### (참고) 바로 값을 지정해주면..?
![image](https://user-images.githubusercontent.com/109324637/193988293-ec0eca3f-1543-4c5b-89c7-3bc6eef09bc7.png)  
✔ 가능은 하나 객체 지향의 관점에서 바람직한 표기법은 아님
### 댓글 속성 확인하기
![image](https://user-images.githubusercontent.com/109324637/193988491-030e75e5-7820-47c0-872d-defe04bcf70b.png)  
### 두번째 댓글 생성하기
![image](https://user-images.githubusercontent.com/109324637/193988649-9129330e-e40e-49a9-adbe-7db3d6b7c0e9.png)  
## 관계 모델 참조
### Related manager
✔ N:1 혹은 M:N관계에서 사용 가능한 문맥  
✔ Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 **역참조**할 때 사용할 수 있는 manager 생성
### 역참조
✔ 나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것  
✔ 본인이 외래 키로 참조 중인 다른 테이블에 접근하는 것  
✔ N:1 관계에서는 1이 N을 참조하는 상황
### Django의 관계 모델 참조
![image](https://user-images.githubusercontent.com/109324637/193989168-fc54c520-4e54-4275-a580-9bd496e439e2.png)
✔ article.comment 형식으로는 댓글 객체를 참조할 수 없다.(Article 클래스 자체에는 어떠한 관계도 작성되어 있지 않음)   
✔ Django가 역참조할 수 있는 **comment_set** manager를 자동으로 생성해 article.comment_set 형태로 댓글 객체를 참조할 수 있다.  
✔ 단순 참조(comment -> article)에서는 comment.article 형태로 바로 작성 가능
### 예시
![image](https://user-images.githubusercontent.com/109324637/193989718-a4edbb0f-bfe8-40fd-8dc1-c3be4c4550bf.png)  
✔ article 1 에 생성된 모든 댓글 조회  
![image](https://user-images.githubusercontent.com/109324637/193989939-b9e63b6b-ef0d-4db8-ab37-9bc3af2526a7.png)  
✔ 위와 같이 모든 댓글들을 comment 변수에 담고 content를 하나씩 출력할 수도 있다
### admin site 등록
![image](https://user-images.githubusercontent.com/109324637/193990581-cc5e064b-3164-4a1d-ad5a-b7b60b045363.png)  
✔ admin site에서 댓글을 확인/관리하기 위해서는 마찬가지로 등록을 해줘야 한다.
## Comment 구현
### Create
#### 1. comment 입력을 위한 CommentForm 작성  
![image](https://user-images.githubusercontent.com/109324637/193991090-cf2bab66-ed39-475a-a925-3a340e26bc8c.png)  
#### 2. detail 페이지에 comment 추가해주기  
![image](https://user-images.githubusercontent.com/109324637/193991492-259e5e8b-56be-487e-8a69-3e9802e1751e.png)
![image](https://user-images.githubusercontent.com/109324637/193991577-7e1550c0-6be9-4f2b-9fd8-fccddedafdcf.png)
#### 3. 그러나...
![image](https://user-images.githubusercontent.com/109324637/193992096-ec2ab475-e10a-4bbc-adca-23f73110b7af.png)
✔ 해당 게시글에 댓글이 바로 작성되도록 하기 위해서는 **외래 키 필드를 사용자의 입력이 아니라 view 함수 내에서 받아 별도로 처리되어 저장되도록 해야 한다.**  
#### 4. 외래 키 필드 출력에서 제외하기
![image](https://user-images.githubusercontent.com/109324637/193992404-baa4c0c1-c0c8-4b93-9b2d-f6b5748656c0.png)
#### 5. 출력에서 제외된 **외래 키 받아오기 (variable routing)**  
![image](https://user-images.githubusercontent.com/109324637/193992892-ee4dfa7b-2b8e-4cc3-957b-d33bcd045f47.png)
![image](https://user-images.githubusercontent.com/109324637/193993117-04c9b44c-6d28-48f3-83e8-e0850b1cdee0.png)
![image](https://user-images.githubusercontent.com/109324637/193993692-656afb85-e271-4546-85bf-392ddbd7b3a8.png)
#### 6. 그러나...
![image](https://user-images.githubusercontent.com/109324637/193993741-af6483cc-1cc5-48cf-a079-c85e84d31fbc.png)  
✔ NOT NULL 에러 발생
#### 7. save 메서드의 commit 옵션을 사용해 DB에 저장되기 전 article 객체 저장
![image](https://user-images.githubusercontent.com/109324637/193994276-12719193-ce5b-4964-824d-1feb1be30e69.png)

### Read
#### 1. 특정 article에 있는 모든 댓글을 가져온 후 context에 추가  
![image](https://user-images.githubusercontent.com/109324637/193995650-8d56be6d-459e-4834-aaf8-bc4e277ca772.png)
#### 2. 템플릿에서 댓글 목록 출력하기
![image](https://user-images.githubusercontent.com/109324637/193995905-cafecbea-531a-41f7-93e5-e7474218fe43.png)
#### 3. 정상적으로 댓글이 달린 것을 확인할 수 있다.
![image](https://user-images.githubusercontent.com/109324637/193995993-9fd81a30-5610-49c4-9397-ab53a91e944f.png)

### Delete
#### 1. url 추가해주기
![image](https://user-images.githubusercontent.com/109324637/193996350-9232d1da-d89e-40be-a6f4-3dfd4658b969.png)
#### 2. view 함수 추가해주기
![image](https://user-images.githubusercontent.com/109324637/193996675-55b7e467-62af-4ba6-82f8-5f76c1f56de9.png)  
✔ 삭제 이후 redirect하기 위해서 article_pk 필요!  
#### 3. 삭제 버튼 만들어주기
   ![image](https://user-images.githubusercontent.com/109324637/193997243-80505faf-da5c-4c9f-bb59-623ca31c6d46.png)

### 댓글 수정은...?
✔ 페이지의 **일부 내용만 업데이트 하는 것은 JavaScript의 영역**이기 때문에 이후에 다시 진행...!!
## Comment 관련 추가 사항
### 1. 댓글 개수 출력하기  
   1. DTL filter - length 사용
  ![image](https://user-images.githubusercontent.com/109324637/193997954-61e80754-b28a-4a91-ac6a-1420e8b05c21.png)

   2. Queryset API - count() 사용
    ![image](https://user-images.githubusercontent.com/109324637/193998073-494c1b25-0f3e-4e73-ad07-ba5b197971c6.png)

### 2. 댓글이 없는 경우 대체 컨텐츠 출력하기
   ![image](https://user-images.githubusercontent.com/109324637/193998410-f05660ea-b3e4-40a1-9933-65ffd1daf1da.png)