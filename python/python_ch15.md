# Ch15 클래스

## 1)클래스

- 클래스
  - 관련 정보와 정보의 조작 함수(메서드)를 묶어서 관리



- 클래스 정의
  - class 키워드로 정의
    - 사용하기 위해서는 인스턴스를 생성한 후 사용



- 생성자

  - ㅡㅡinitㅡㅡ(self)
    - 클래스의 인스터스를 생성할 때 자동으로 호출
    - 멤버 변수 정의 및 초기화 역할

  class 이름:

  ​	def ㅡㅡinitㅡㅡ(self,초기값):

  ​		멤버 초기화

  ​	메서드 정의

객체 = 객체명(인수)

![image-20210111220345998](python_ch15.assets/image-20210111220345998.png)



- 상속
  - 기존 클래스 정의를 그대로 자신의 것으로 취하는 방법

Class 자식클래스명(부모클래스명):

 ![image-20210125000049560](python_ch15.assets/image-20210125000049560.png)

- 액세스

  - 파이썬은 기본적으로 정보 은폐 기능 지원하지 않음

  - getter/setter로 정보(프로퍼티)를 보호

    - @property

      -함수명이 프로퍼티명이 되며 getter 함수로 동적

    - @프로퍼티명.setter

      -프로퍼티의 setter() 함수 정의