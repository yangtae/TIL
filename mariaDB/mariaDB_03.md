# SQL 고급 -조인-

## 1. 조인

- 조인
  - 두개 이상의 테이블을 서로 묶어서 하나의 결과 집합으로 만들어 내는 것
  - 관계형 테이블의 가장 큰 특징
  - 테이블 간의 관계
    - 1:1
    - 1:N
    - N:M



- INNER JOIN(내부 조인)
  - 가장 많이 사용되는 조인
  - 공통 컬럼을 기반으로 결합
    - 부모 테이블 : Primary Key
    - 자식 테이블 : Foreign Key(부모 테이블의 PK값 참조)



[형식]

SELECT<열 목록>

FROM <첫 번째 테이블>

​	INNER JOIN <두 번째 테이블>

​	ON <조인될 조건>  -- 공통컬럼

[WHERE 검색 조건]



SELECT *

FROM buyTBL

​	INNER JOIN userTBL

​	ON buyTBL.userID = userTBL.userID

WHERE buyTBL.userID = 'JYP';



# 테이블과 뷰

- SQL로 테이블 만들기(FOREIN KEY)
  - FOREIN KEY
    - 다른 테이블에 대한 참조를 의미
    - 참조되는 필드는 반드시 그 테이블에서 KEY여야 함(유일해야함)
    - FOREIGN KEY(필드명) REFERENCES 참조테이블명(참조테이블_필드명)



CREATE TABLE buyTBL

( num int AUTO_INCREMENT NOT NULL PRIMARY KEY,

​	userid char(8) NOT NULL,

​	prodName char(6) NOT NULL

​	groupName char(4) NULL

​	price int NOT NULL,

​	FOREIGN KEY(userid) REFERENCES userTBL(userID)

)



- 기본키(PRIMARY KEY) 제약 조건
  - 테이블당 1개의 컬럼에만 배정
  - 값은 중복 될 수 없으며, NULL을 가질 수 없음
  - 자동으로 인덱스 객체가 생성됨



- 외래 키(FOREIGN KEY) 제약조건

  - 두 테이블 사이의 관계를 선언함으로써, 데이터의 무결성을 보장

  - 하나의 테이블(자식 테이블)이 다른 테이블(부모 테이블)에 의존하게 됨

  - 자식 테이블에 외래 키가 존재

    - 참조하는  부모 테이블에 반드시 값이 존재해야 함

      -삽입/수정 시 부모 테이블에 값이 없다면 에러

    - 자식 테이블에 참조하는 행이 있다면 해당 부모 테이블의 행은 삭제 불가

      -삭제 시 에러 발생

      -자식 테이블의 해당 값을 NULL로 바꾸거나, 먼저 자식테이블의 행을 삭제

  - 부모 테이블의 행을 수정/삭제할때

    - 그 행을 참조하는 자식 테이블에 대한 처리 옵션 지정

    - ON DELETE CASECADE

      -부모 행이 삭제될 때 자식 테이블의 행도 자동 삭제

    - ON UPDATE CASECADE

      -부모 수정시 자식도 해당 값으로 자동 수정

    - 디폴트

      -ON UPDATE NO ACTION

      -ON DELETE NO ACTION



- UNIQUE 제약조건
  - 중복을 허용하지 않음
  - NULL은 허용



## 2.뷰

- 뷰
  - 테이블과 동일하게 사용되는 개체
  - SELECT쿼리 결과를 하나의 테이블로 간주
    - 여기에 이름을 배정하고 이를 통해 사용



CREATE VIEW 뷰이름

AS SELECT 쿼리



USE tableDB

CREATE VIEW v_userTBL

AS SELECT userid, name, addr FROM userTBL;

SELECT *FROM vuserTBL; -- 뷰를 테이블이라고 생각해도 무방