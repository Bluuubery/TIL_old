# Django Relationship fields (N:1) (Comment - User)
## 모델 관계 설정
![image](https://user-images.githubusercontent.com/109324637/194046766-824cc4ec-f2fb-4d1c-bb50-5fe3f0018911.png)
![image](https://user-images.githubusercontent.com/109324637/194040874-798b7fba-9560-403d-aca5-a4398194b418.png)  
✔ models.py에 외래 키 추가해주고 migrations해주기!  
## Create
### 1. 이전과 마찬가지로 불필요한 유저 선택창 출력
![image](https://user-images.githubusercontent.com/109324637/194041421-3401e77e-a2fa-46b9-8d6d-0d7ce675b86b.png)
### 2. Form에서 출력 필드 수정
![image](https://user-images.githubusercontent.com/109324637/194041534-f1b36af6-c1b6-4a27-b432-c7eceb34dc9a.png)
### 3. 누락된 외래키 추가해주기
![image](https://user-images.githubusercontent.com/109324637/194041980-2572ef53-9f82-4fd8-a80e-6b1c60a954ae.png)
## Read
### Detail 템플릿에서 작성자 출력되도록 변경
![image](https://user-images.githubusercontent.com/109324637/194042423-dfa5af50-95a2-447b-9f28-2ce1855a7e80.png)
## Delete
### 1. 댓글 작성자 확인해서 본인 댓글만 삭제할 수 있도록 하기
![image](https://user-images.githubusercontent.com/109324637/194042860-895c55e8-0d29-4371-8b6e-6cb18890a1c4.png)
### 2. 댓글 작성자 외에 댓글 삭제 버튼 숨기기
![image](https://user-images.githubusercontent.com/109324637/194043112-897cebe9-98b7-4f0d-9523-3383819b0887.png)
## 인증된 사용자에 대한 접근 제한하기
### 인증된 사용자인 경우만 댓글 작성하기
![image](https://user-images.githubusercontent.com/109324637/194043590-77083570-d227-47ff-82ad-6818eb258817.png)
![image](https://user-images.githubusercontent.com/109324637/194044518-ef0704fe-7257-4dc5-b869-c65c3009aef5.png)
![image](https://user-images.githubusercontent.com/109324637/194044615-c455592a-49eb-4dc7-a682-0a260d2aec53.png)
### 인증된 사용자인 경우만 댓글 삭제하기
![image](https://user-images.githubusercontent.com/109324637/194044925-10ebb889-f613-4c5e-bf30-3cbeb39d10fe.png)
### 데코레이터 추가해주기
![image](https://user-images.githubusercontent.com/109324637/194045151-23298a88-0c30-4b82-8183-f5d6424e3521.png)  
✔ 한번에 다 추가할려고 하지말고 처음엔 구조를 생각하면서 하나씩 설계하기