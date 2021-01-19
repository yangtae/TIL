

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







  

  

  

  