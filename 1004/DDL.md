# DDL
## DDL이란?
✔ 'Data Definition'  
✔ DDL은 테이블 구조를 관리: CREATE, ALTER, DROP
## CREATE TABLE statement
![image](https://user-images.githubusercontent.com/109324637/193830734-ef67cb07-9443-4988-abd0-86759e92a3d6.png)

## Data Type 종류
1. Null: 정보가 없거나 알 수 없음
2. Integer: 정수
3. Real: 실수
4. Text: 문자
5. BLOB(Binary Large Object): 입력된 그대로 저장된 데이터 덩어리 (대용 타입 없음)

### Boolean Type...?
✔ SQLite에는 별도의 boolean 타입 없음  
✔ 0(False), 1(True)로 저장
### Date & Time ...?
✔ SQLite에는 날짜 및 시간을 저장하기 위한 별도의 타입 x  
✔ 대신 builtin 'Date And Time Functions'로 TEXT, REAL, 또는 INTEGER값으로 저장
### Binary DATA
✔ 데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로 인코딩된 파일  
## SQLite의 Data Type
✔ 값에 둘러싸는 따옴표와 소수점 또는 지수 x -> **INTEGER**  
✔ 값이 작은 따옴표나 큰 따옴표로 묶이면 -> **TEXT**  
✔ 값에 따옴표나 소수점, 지수가 없으면 -> **REAL**  
✔ 값이 따옴표 없이 NULL이면 -> **NULL**  
### SQLite datatypes의 특징
✔ SQLite는 다른 데이터베이스 엔진의 정적이고 엄격한 타입이 아닌 "**동적 타입 시스템(dynamic type system)**"을 사용  
✔ **컬럼에 저장된 값**에 따라 데이터 타입이 결정됨  
✔ 따라서 테이블을 생성할 떄 컬럼에 대해 특정 데이터 타입을 선언하지 않아도 됨  
✔ 그러나 다른 데이터베이스와의 **호환성 문제가 있기 때문에 데이터 타입 지정권장**  
✔ 데이터 타입을 지정하면 SQlite는 입력된 데이터의 타입을 지정된 에이터 타입으로 변환  
### (참고) 자동 형변환
![image](https://user-images.githubusercontent.com/109324637/193751810-4a7414d8-8f63-4469-b6dc-df475193f019.png)  
## SQLite Data Type Affinity
![image](https://user-images.githubusercontent.com/109324637/193752140-b0b473de-4bd4-4914-a7a9-2860ab756c36.png)   
✔ **다른 데이터베이스 엔진 간의 호환성**을 최대화  
## Contraints 
✔ '**데이터 무결성**'을 유지하기 위해 테이블의 컬럼에 설정하는 제약  
### 데이터 무결성
✔ 데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 정확성을 보증하는 것  
### 1. NOT NULL
✔ 컬럼이 NULL 값을 허용하지 않도록 지정  
### 2. UNIQUE
✔ 컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함  
### 3. PRIMARY KEY
✔ 테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼  
✔ 암시적으로 NOT NULL 제약 조건이 포함되어 있음  
✔ 따로 명시 안 하면 'row id' 자동 생성
### 4. AUTOINCREMENT
✔ 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지  
✔ INTEGER PRIMARY KEY 다음에 작성하면 해당 rowid를 재사용하지 못하도록 함  
✔ Django에서 테이블 생성 시 id컬럼에 기본적으로 사용하는 제약 조건  
### row id의 특징  
✔ 테이블을 생성할 때마다 **rowid라는 암시적 자동 증가 컬럼**이 자동으로 생성됨  
✔ 테이블의 행을 고유하게 식별하는 64비트 부호의 정수 값  
✔ 테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당 (start = 1)
✔ 만약 INTEGER PRiMARY KEY 키워드를 가진 컬럼을 직점 만들면 이 컬럼은 rowid 컬럼의 별칭(alias)가 된다.
## Alter Table
✔ 기존 테이블의 구조를 수정(변경)  
1. Rename a table
2. Rename a column  
3. Add a new column to a table  
4. Delete a column  

### 예시
![image](https://user-images.githubusercontent.com/109324637/193831042-c575abd5-4b4b-4d51-94bc-ce960c377973.png)
## DROP TABLE
✔ 데이터 베이스에서 테이블을 제거  
### DROP TABLE의 특징
✔ 한 번에 하나의 테이블만 삭제 -> 여러 테이블을 제거하려면 여러 DROP TABLE 문 실행  
✔ **실행 취소 or 복구 불가!**
### 예시
![image](https://user-images.githubusercontent.com/109324637/193831145-d106e057-9160-43e5-b648-b76766e90786.png)