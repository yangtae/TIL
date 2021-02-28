

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



- 테이블 생성
  - productTBL (CREATE 코드)

CREATE TABLE 'producttbl'(

​	'productName' CHAR(4) NOT NULL COLLATE 'utf8_general_ci',

​	'cost' INT(11) NOT NULL DEFAULT '0',

​	'makeDate' DATE NULL DEFAULT '0000-00-00',

​	'company' CHAR(5) NULL DEFAULT NULL COLLATE 'utf8_general_ci',

​	'amount' INT(11) NULL DEFAULT NULL,

​	PRIMARY KEY('productName') USING BTREE

)

COLLATE = 'utf8_general_ci'

ENGINE=InnoDB;



- 데이터 활용

  - memberTBL > 쿼리탭

    - memberName과 memberAddress만 출력

    -SELECT memberName, memberAddress FROM membertbl;

    - memberName이 '지운이'인 행만 출력

    -SELECT * FROM memberTBL WHERE memberName = '지운이'



- 쿼리로 테이블 생성
  - CREATE TABLE 'my tstTBL' (id INT);
    - 명칭에 공백이 있는 경우 반드시 '명칭'으로 지정
  - 쿼리로 생성한 경우 새로 고침해야 그래픽에 나타남



- 쿼리로 테이블 삭제
  - DROP TABLE 'my tstTBL';





- 

