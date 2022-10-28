# DML
## DML이란?
✔ Data Manipulation  
✔ DML을 통해 데이터 조작 (CRUD)  
✔ INSERT, SELECT, UPDATE, DELETE  
## Simple query
✔ **SELECT**문을 사용하여 간단하게 단일 테이블에서 데이터 조회하기
### SELECT statement
✔ 'Query data from a table'  
✔ 특정 테이블에서 데이터를 조회하기 위해 사용  
✔ 문법 규칙  
1. SELECT절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정
2. FROM 절(clause)에서 데이터를 가져올 테이블을 지정    

✔ 다양한 절과 함께 사용할 수 있어 매우 복잡
### 예시
![image](https://user-images.githubusercontent.com/109324637/193815166-6b4bba83-a689-4039-b813-125a67b33282.png)

## Sorting rows
✔ **ORDER BY**절을 사용하여 쿼리의 결과를 정렬  
이미지 넣기  
✔ SELECT문에 추가하여 결과를 정렬  
✔ ORDER절 다음에 'ASC' 혹은 'DESC' 키워드 사용  
✔ ASC: 오름차순 (기본 값)  
✔ DESC: 내림차순
### 예시
![image](https://user-images.githubusercontent.com/109324637/193814849-516bdd10-3444-4c3e-a634-24eb095d4816.png)
### (참고) Sorting NULLs
✔ SQLite는 NULL을 가장 작은 값으로 취급  
## Filtering Data
✔ 데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리 제어  
✔ Clause: SELECT DISTINCT, WHERE, LIMIT  
✔ Operator: LIKE, IN, BETWEEN
### SELECT DISTINCT clause
✔ 조회 결과에서 중복된 행을 제거   
✔ DISTINCT 절은 SELECT에서 선택적으로 사용 가능  
✔ 문법 규칙  
1. DISTINCT 절은 SELECT 키워드 바로 뒤에 나타나야함  
2. DISTINCT 키워드 뒤에 컬럼 또는 컬럼 목록을 작성  
#### 예시
![image](https://user-images.githubusercontent.com/109324637/193814463-975ddfbc-ff6d-45d6-a11d-e3b2e69b61aa.png)
#### (참고) NULL with DISTINCT
✔ SQLite 는 NULL 값을 중복으로 간주
### WHERE clause
✔ 조회 시 **특정 검색 조건**을 지정  
✔ WHERE 절은 SELECT 문에서 선택적으로 사용 가능  
✔ SELECT문 외에도 UPDATE 및 DELETE문에서 사용 가능  
#### 예시
![image](https://user-images.githubusercontent.com/109324637/193790394-aa060374-38d2-40cc-98a1-58c374f85ab6.png)
### SQLITE 논리 연산자
✔ 1, 0 또는 NULL 값을 반환 (Boolean 데이터 타입 x)  
✔ ALL, AND, ANY, BETWEEN, IN, LIKE, NOT, OR
### LIKE operator
✔ **패턴 일치**를 기반으로 조회  
✔ 기본적으로 대소문자 구분 x  
✔ 패턴 구성을 위한 두 개의 와일드 카드
1. %(percent): 0개 이상의 문자가 올 수 있음을 의미
2. _(underscore): 단일(1개) 문자가 있음을 의미
#### 예시
![image](https://user-images.githubusercontent.com/109324637/193789609-7e1a32e5-ef49-48be-9f41-848668673403.png)
### IN operator
✔ 값이 값 목록 결과에 있는 값과 일치하는지 확인  
✔ True / False 반환  
✔ 부정: **NOT IN** 연산자 사용
#### 예시
![image](https://user-images.githubusercontent.com/109324637/193816075-a2f5e106-2f1c-453a-9029-90d99c18ffab.png)  
### BETWEEN operator
✔ 값이 값 범위에 있는지 테스트  
✔ 값이 지정된 범위에 있으면 True 반환    
✔ 부정: **NOT BETWEEN** 연산자 사용  
#### 예시
![image](https://user-images.githubusercontent.com/109324637/193816985-2ea8040b-24c1-433c-90a0-802399613d92.png)  
### LIMIT operator
✔ 쿼리에서 반환되는 행 수를 제한  
✔ SELECT문에서 선택적으로 사용 가능  
✔ row_count는 반환되는 행 수를 지정하는 양의 정수 의미  
#### 예시
![image](https://user-images.githubusercontent.com/109324637/193817594-059d02c4-2c9e-4dee-a0ef-ad09dd408896.png)  
### OFFSET operator
✔ LIMIT절과 함께 사용해 특정 지정된 위치에서부터 데이터 조회 가능
#### 예시
![image](https://user-images.githubusercontent.com/109324637/193817974-2eb3843c-35c2-4187-89fa-8f47f7c2b845.png)
## Grouping data
### GROUP BY clause
✔ 특정 그룹으로 묶인 결과를 생성  
✔ 선택된 컬럼 값을 기준으로 데이터(행)들의 공통 값을 묶어서 결과로 나타냄  
✔ SELECT문에서 선택적으로 사용 가능  
✔ SELECT문에서 FROM 절 뒤에 작성 (WHERE절이 포함된 경우 WHERE절 뒤에 작성)  
✔ aggregate function을 적용하여 그룹에 대한 추가적인 정보 제공 가능  
### Aggregate function
✔ 각 집합의 최대값, 최소값, 평균, 합계 및 개수 계산  
✔ 값 집합에 대한 계싼을 수행하고 단일 값을 반환  
✔ AVG(), COUNT(), MAX(), MIN(), SUM()  
✔ 컬럼의 데이어 타입이 숫자(INTEGER)일 때만 사용 가능  
#### 예시
![image](https://user-images.githubusercontent.com/109324637/193820313-5231af00-2475-4a80-8b8e-964b7b92c582.png)
## Changing data
✔ 데이터를 삽입, 수정, 삭제하기  
✔ INSERT, UPDATE, DELETE  
### INSERT statement
![image](https://user-images.githubusercontent.com/109324637/193822133-4c83edb1-ecf5-4387-b144-4d69f9c29dfb.png)  
✔ 새 행을 테이블에 삽입  
✔ 문법 규칙
1. 먼저 INSERT INTO 키워드 뒤에 데이터를 삽입할 테이블의 이름 지정
2. 테이블 이름 뒤에 쉼표로 구분된 목록 추가
3. VALUES 키워드 뒤에 구분된 값 목록 추가(테이블과 순서 동일)
#### 예시
![image](https://user-images.githubusercontent.com/109324637/193822637-c67790ee-467c-4ca0-b710-660fc1539c40.png)
### UPDATE statement
✔ 테이블에 있는 기존 행의 데이터를 업데이트 한다.  
✔ 문법 규칙  
1. UPDATE 절 이후에 업데이트할 테이블 지정
2. SET 절에서 테이블의 각 칼럼에 대해 새 값을 설정
3. WHERE절의 조건을 사용하여 업데이트할 행을 지정(미선택 시 모든 행의 데이터 업데이트)
4. 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 업데이트할 행 수 지정 가능
#### 예시
![image](https://user-images.githubusercontent.com/109324637/193823773-f8fed95d-f147-4cde-96a7-6809eaab0f1a.png)
### DELETE statement
![image](https://user-images.githubusercontent.com/109324637/193824302-50dffdaa-964e-4d90-a8ff-24e22bffe8c8.png)  
✔ 테이블에서 행 제거  
✔ 테이블의 한 행, 여러 행 및 모든 행 삭제 가능
✔ 문법 규칙  
1. DELETE FROM 키워드 뒤에 행을 제거하려는 테이블 이름 지정  
2. WHERE 절에 검색 조건을 추가하여 제거할 행 식별 (생락 시 모든 행 삭제)  
3. 선택적으로 ORDER BY 및 LIMIT 절 사용하여 삭제할 행 수 지정 가능
#### 예시
![image](https://user-images.githubusercontent.com/109324637/193824711-ade908b4-39d2-4d06-bc7b-fec59026fdc1.png)