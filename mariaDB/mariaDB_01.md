

# mariaDB

- 테이블 구조와 관련 용어

![image-20210119225900336](mariaDB_01.assets/image-20210119225900336.png)

## 1) SQL 기본

### 1) SELECT문

- 명칭
  - 데이터베이스명.테이블명
    - desc employees.titles;
  - SQL 명령어는 대소문자 구분하지 않음
  - 사용자 정의 명칭은 구분하기도함



- 주석
  - --
    - 한줄 주석문
  - /*    */
    - 여러줄 주석문



- DESC
  - 테이블의 구조를 출력

![image-20210119230656196](mariaDB_01.assets/image-20210119230656196.png)



- 샘플 데이터베이스 구축하기

  - shopDB.sql 파일을 c:\\temp 에 준비

  - 시작 > MariaDB > Command Prompt

    -cd \\temp

    -mysql -u(userid) root -p(password)



​	 MariaDB[sqlDB] > source shopDB.sql



- SELECT

  - 테이블의 내용 출력

    -SELECT 필드목록

    FROM 테이블명

    [WHERE 조건]

    [GROUP BY 컬럼명]

    [HAVING 조건]

    [ORDER BY 컬럼명]

    ![image-20210119231208146](mariaDB_01.assets/image-20210119231208146.png)

  - WHERE 절 - 관계 연산자(AND, OR, NOT)의 사용![image-20210119231431763](mariaDB_01.assets/image-20210119231431763.png)

    

  - WHERE 절 - BETWEEN.... AND, IN() 그리고 LIKE

  ![image-20210119231544688](mariaDB_01.assets/image-20210119231544688.png)

  ![image-20210119232003106](mariaDB_01.assets/image-20210119232003106.png)



- ANY/ALL/SOME 그리고 서브쿼리(SubQuery, 하위쿼리)
  - 서브쿼리
    - FROM/WHERE 절에 SELECT문을 제시
    - 서브 쿼리는 반드시()안에 작성

SELECT Name, height FROM userTBL WHERE height > 177;

-키가 177보다 큰 사람 출력



SELECT Name, height FROM userTBL

​	WHERE height > (SELECT height FROM userTbl WHERE Name = '김경호');

-김경호의 키보다 큰 사람 출력



SELECT Name, height FROM userTBL

​	WHERE height >= (SELECT height FROM userTbl WHERE addr='경남');

-이 경우 모든 경남사람보다 키큰 사람인지 경남 아무 사람키보다 큰것만 하는지 모호하기 때문에 ANY/ALL을 써야한다



SELECT Name, height FROM userTBL 

WHERE name LIKE '김%';

-% : 아무 글자가 와도 상관없음 (개 수에 제한 없음)



SELECT Name, height WHERE name like '_종신';

-_ : 한글자로 아무 글자가 와도 상관없음

  

- 원하는 순서대로 정렬하여 출력
  - 오름차순 : ASC(디폴트, 생략가능)
  - 내림차순 : DESC



SELECT Name, mDate FROM userTBL ORDER BY mDate;

-mDate의 오름 차순으로 정렬



SELECT Name, mDate FROM userTBL ORDER BY mDate DESC;

-mDate의 내림 차순으로 정렬



- 중복된 것은 하나만 남기는 DISTINCT

SELECT DISTINCT addr FROM userTBL



- 출력하는 개수를 제한하는 LIMIT

SELECT emp_no, hire_date FROM employees

ORDER BY hire_date ASC

LIMIT 5;



- 테이블을 복사하는 CREATE TABLE ..SELECT
  - 기존 테이블과 동일한 구조로 테이블 생성
  - KEY 제약조건은 복사되지 않음
    - 필드의 이름, 타입, 길이, NULL여부가 동일
  - 특정 컬럼(SELECT 절 제시) 또는 특정 행만 (WHERE절 제시)복사 가능

형식] CREATE TABLE [새로운 테이블명] (SELECT 복사할 열 FORM 기본테이블명)

  

CREATE TABLE buyTBL2 (SELECT * FROM buyTBL);

SELECT * FROM buyTBL2



- GROUP BY  그리고 집계함수
  - GROUP BY 절
    - 특정 컬럼에 대해 동일한 값을 가지는 행들을 하나의 행으로 처리
    - 통계 작업에 사용

SELECT userID as '사용자 아이디', SUM(amount) as '총 구매 개수'

FROM buyTBL

GROUP BY userID;

![image-20210121230423866](mariaDB_01.assets/image-20210121230423866.png)



- HAVING절
  - GROUP BY 결과에서 필터링

SELECT userID as '사용자', SUM(price*amount) AS '총구매액'

FROM buyTBL

GROUP BY userID

HAVING SUM(price*amount) > 1000;