# Many to many relationship
## M:N 관계
✔ Many-to-many relationships  
✔ 한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우  
✔ 양쪽 모두에서 N:1 관계를 가진다.  
## 개요
✔ 병원에 내원하는 환자와 의사의 예약 시스템 구축  
✔ 환자 <-> 의사 관계 데이터 모델링
### 용어 정리
✔ Target model
- 관계 필드를 가지지 않은 모델  
   
✔ Source model
- 관계 필드를 가진 모델  
## N:1 모델의 한계
![image](https://user-images.githubusercontent.com/109324637/195232355-c0012417-54d9-44fd-9d6a-95082b762a67.png)  
✔ 동일한 환자가 다른 의사에게 예약하기 위해서는 객체를 하나 더 만들어서 예약을 진행해야 한다.     
![image](https://user-images.githubusercontent.com/109324637/195232416-68b9415c-0ccf-4439-b89f-c17088a86e0b.png)  
✔ 외래 키 컬럼에 '1, 2' 형태로 참조하기 불가능  
### 중개 모델 작성을 통한 해결
![image](https://user-images.githubusercontent.com/109324637/195232961-fad40963-d8ee-438b-8fe0-a6bd42ffaa3f.png)  
✔ 환자와 의사 둘다에 대해서 N:1 관계를 가지는 별도의 예약 모델을 새로 작성  
![image](https://user-images.githubusercontent.com/109324637/195233197-bfb7c230-a661-42a9-bcad-1723c11b1fd0.png)  
✔ 의사와 환자 생성 후 예약 만들기 (사진은 doctor를 두 번 생성해서 2번 의사로 나옴)   
![image](https://user-images.githubusercontent.com/109324637/195233571-790c08a9-f204-461c-a907-f044e5ed8e68.png)  
✔ 역참조를 통해서 예약 정보 조회 가능  
## Django ManyToManyField
![image](https://user-images.githubusercontent.com/109324637/195233888-d922b5d0-d1f8-44e5-9eec-40611439d0ca.png)  
✔ 환자 모델에 DJango ManyToManyField 작성 (복수형으로 작성하기!)  
![image](https://user-images.githubusercontent.com/109324637/195234574-c4210f74-3814-4e45-b793-4e6424d9a298.png)  
✔ 종속적이지 않은 별도의 스키마(중개 테이블)이 생성된다.  
![image](https://user-images.githubusercontent.com/109324637/195235073-e8981805-0640-4032-bd03-6437fb103297.png)  
✔ 예약 생성 및 조회(환자 -> 의사)  
![image](https://user-images.githubusercontent.com/109324637/195235264-a5d8db9b-b008-42a0-b807-883f1f52c1dd.png)  
✔ 의사 -> 환자  
![image](https://user-images.githubusercontent.com/109324637/195235894-76eb0b45-9687-4858-bdbc-762ab94862c0.png)  
✔ 예약 취소 (의사 -> 환자)   
![image](https://user-images.githubusercontent.com/109324637/195236059-84efdc25-3892-4b89-b81a-178f02bdedee.png)  
✔ 예약 취소 (환자 -> 의사)  
### `related_name` argument
✔ target model이 source model을 참조할 떄 사용할 이름  
![image](https://user-images.githubusercontent.com/109324637/195236315-e5b740df-fc9b-4f31-942f-db74c02d730d.png)  
![image](https://user-images.githubusercontent.com/109324637/195236513-b6646cd1-e91a-4d1a-8dab-56837d91bbdf.png)  
✔ 역참조가 아니라 related_name으로 바로 접근할 수 있다    
### `through` argument
✔ 그렇다면 중개 모델을 직접 작성하는 경우는 없을까?
- 중개 테이블을 수동으로 지정할 경우 `through`옵션을 사용할 수 있다.  
   
✔ 가장 일반적인 용도는 중개테이블에 추가 데이터를 사용해 M:N관계와 연결하려는 경우 
![image](https://user-images.githubusercontent.com/109324637/195237266-8420a688-fb62-4fde-8e3b-d4372a44798c.png)  
✔ `through` 설정 및 `Reservation Class` 수정  
![image](https://user-images.githubusercontent.com/109324637/195237833-baf83506-ffca-44d8-bd0a-9e227867a3dc.png)  
✔ 기존 중개 모델에서의 예약 생성 방식을 이용할 수도 있다.  
![image](https://user-images.githubusercontent.com/109324637/195238113-5b64b42a-b1d1-4a0d-a72e-1f3f9c011a2a.png)  
✔ 기존 manytomany field에서 의사나 환자가 예약을 생성하듯이 생성할 수 있다.    
✔ `through_dfaults`값에 딕셔너리 타입으로 입력해준다.
### `symmetrical`
✔ 대칭을 의미  
✔ `ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서 사용  
![image](https://user-images.githubusercontent.com/109324637/195239286-986b379e-56a7-4b28-be2d-6b82e413534a.png)    

✔ True일 경우
- _set 매니저를 추가하지 않음
- source 모델의 인스턴스가 target모델의 인스턴스를 참조하면 자동으로 target모델 인스턴스도 source 모델 인스턴스를 자동으로 참조하도록 한다.(대칭)
- 즉, 내가 당신의 친구라면 당신도 내 친구가 되는 관계  
  
✔ 대칭을 원하지 않는 경우 False로 설정

## 정리
✔ M:N 관계로 맺어진 두 테이블에는 변화가 없음  
✔ Django의 `ManyToManyField`은 중개 테이블을 자동으로 생성한다.  
✔ Django의 `ManyToManyField`는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관 없으나, 필드 작성 위치에 따라 참조와 역참조 방향을 주의해야 한다.  
✔ N:1은 완전한 종속 관계 였지만, M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 두 가지 형태로 모두 표현 가능  
