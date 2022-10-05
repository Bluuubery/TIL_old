# Django Relationship fields (N:1) (Article - User)
## User 모델 참조
### Django 에서 User 모델을 참조하는 방법
1. settings.AUTH_USER_MODEL
2. get_user_model()

### 1. settings.AUTH_USER_MODEL
✔ 반환값: 'accounts.User' (문자열)  
✔ User 모델에 대한 외래 키 또는 M:N 관계를 정의할 떄 사용  
✔ **models.py의 모델 필드에서 User 모델을 참조할 때 사용**
### 2. get_user_model()
✔ 반환값: User Object(객체)  
✔ 현재 활성화된 User 모델 반환  
✔ **models.py 가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용**  
## 모델 관계 설정
![image](https://user-images.githubusercontent.com/109324637/194046646-e71a98fb-ae9a-4649-843c-770824109fb9.png)
### 1. model.py
![image](https://user-images.githubusercontent.com/109324637/194003283-0c82c368-f51c-46df-8c24-5d815a8283d2.png)
### 2. makemigrations
![image](https://user-images.githubusercontent.com/109324637/194003704-f0e778d3-83eb-4ba1-a16a-a8b6527c2f29.png)  
✔ 1 번 (기본값 직접 추가)  
### 3. 기본값 추가해주기
![image](https://user-images.githubusercontent.com/109324637/194003907-fb5f55af-1451-4c85-b221-e4302bb732aa.png)  
✔ (임의의)기본값 추가해주기  
### 4. migrate 적용해주기
![image](https://user-images.githubusercontent.com/109324637/194004112-5c57b277-f597-4106-8922-6b9d1b8b049c.png)  

## Create
### 1. 이전과 유사하게 불필요한 user field가 출력되는 상황
![image](https://user-images.githubusercontent.com/109324637/194004770-1892ac86-3cf3-49f0-b1f9-3131c85cf20e.png)
### 2. ArticleForm의 출력 필드 수정
![image](https://user-images.githubusercontent.com/109324637/194004958-46340f3e-f092-4b79-95ca-2a228f78b98f.png)
### 3. save의 commit 옵션 활용해서 게시글 작성자 정보 저장
![image](https://user-images.githubusercontent.com/109324637/194005368-4aaf6ac0-f116-4928-a856-3f7dc2d0cc65.png)

## Delete
![image](https://user-images.githubusercontent.com/109324637/194005932-fe230434-4268-4391-b3f6-e6c380093db5.png)  
✔ 현재 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제 할 수 있도록 함

## Update
### 1. 수정도 마찬가지로 수정을 요청하려는 사람과 게시글즐 작성한 사람을 비교하여 본인의 게시글만 수정
![image](https://user-images.githubusercontent.com/109324637/194017811-61005afd-f109-4b57-a5fa-da41fa902b3d.png)
### 2. 추가로 해당 글의 작성자가 아니라면, 수정/삭제 버튼 출력하지 않기
![image](https://user-images.githubusercontent.com/109324637/194018121-dd4c35a2-5df8-4c55-a2d5-1bbe0a59c4c3.png)

## Read
### 작성자 출력하기 (index, detail)
![image](https://user-images.githubusercontent.com/109324637/194018573-2cf7bded-ffe9-4f92-ba8c-3d99c5d5071a.png)
✔ user.username이 아니라 user만 출력해도 작성자를 반환하도록 되어있음  
