# Ch11 컬렉션 관리

## 1) 컬렉션 관리 함수

- enumerate
  - enumerate(시퀀스,[, start])
    - 시퀀스의 인덱스와 요소를 튜플 묶어서 순회

![image-20210113221111705](python_ch11.assets/image-20210113221111705.png)



- zip
  - zip(시퀀스1, 시퀀스2) -> [(값1, 값2), .....]
  - 시퀀스의 길이가 다른 경우 가장 짧은 시퀀스의 길이에 맞춤

![image-20210113222148393](python_ch11.assets/image-20210113222148393.png)

![image-20210113222200122](python_ch11.assets/image-20210113222200122.png)



- any(), all()
  - any(시퀀스)
    - 시퀀스 하나라도 True가 있으면 True 리턴
  - all(시퀀스)
    - 시퀀스의 모든 요소가 True이면 True 리턴



## 2) 람다 함수

- filter
  - filter(판정함수, 시퀀스)  => 시퀀스
    - 시퀀스의 각 요소를 판정함수에 전달하여 True를 리턴하는 요소로만 구성된 새로운 시퀀스 리턴

![image-20210113224800965](python_ch11.assets/image-20210113224800965.png)



- map
  - map(적용시킬함수, 시퀀스)

![image-20210113225749486](python_ch11.assets/image-20210113225749486.png)



- 람다함수
  - 한 줄로 정의되는 함수의 축약  표현
  - 함수의 이름이 없음
    - 변수에 대입해서 사용
  - lambda 인수 : 식

![image-20210113225836554](python_ch11.assets/image-20210113225836554.png)



## 3) 컬렉션의 사본

- 리스트의 사본
  - 시퀀스.copy() -> 시퀀스 복사본

![image-20210113230207238](python_ch11.assets/image-20210113230207238.png)



![image-20210113230419072](python_ch11.assets/image-20210113230419072.png)



- is 연산자
  - 두 변수가 같은 객체를 가르키고 있는지 조사

![image-20210113230459750](python_ch11.assets/image-20210113230459750.png)