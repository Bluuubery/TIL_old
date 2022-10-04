# RDB
✔ Relational Database  
✔ 데이터를 테이블, 행, 열 등으로 나누어 구조화  
✔ 자료를 여러 테이블로 나누어서 관리하고, 이 테이블 간 관계를 설정해 여러 데이터를 쉽게 조작 가능  
## 테이블간 관계 설정
![image](https://user-images.githubusercontent.com/109324637/193744738-5a91350c-ae8f-42ce-b267-0c482847b491.png)  
✔ 다른 테이블에 있는 데이터를 어떻게 가져올 것인가...  
✔ **참조하는 데이터 테이블의 id를 추가적인 column으로 관리!**
## RDB의 기본 구조
### 1. 스키마
![image](https://user-images.githubusercontent.com/109324637/193745023-eb9e927f-b801-4131-a2ad-686c6fd7a32c.png)  
✔ 테이블의 구조  
✔ 데이터베이스에서 자료의 구조, 표현 방법, 관계 등 전반적인 명세를 기술한 것   
### 2. 테이블  
![image](https://user-images.githubusercontent.com/109324637/193745100-1853b553-ee9a-4844-87c2-b6d9193583d1.png)  
✔ 필드와 레코드를 사용해 조직된 데이터 요소들의 집합  
✔ 관계(Relation)이라고도 부름  
✔ 필드(Field): 속성, column  
✔ 레코드(Record): 튜플, row  
### PK (Primary Key)
✔ 기본 키  
✔ 기술적으로 다른 항목과 절대로 중복될 수 없는 **단일 값(Unique)**  
## RDBMS
✔ Relational Database Management System (관계형 데이터베이스 관리 시스템)  
ex: **SQLite**, MySQL, Ocacle DB...
## SQLite
✔ 응용 프로그램에 파일 형식으로 넣어 사용하는 비교적 가벼운 데이터 베이스
### Why SQLite?
✔ 어떤 환경에서나 실행 가능한 호환성  
✔ 데이터 타입이 비교적 적고 강하지 않기 때문에 유연한 학습 환경 제공  
✔ **Django Framework의 기본 데이터베이스**
### 단점
✔ 대규모 동시 처리 작업에 부적합  
