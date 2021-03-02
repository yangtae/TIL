#include<Led.h>
#include<Button.h>

Led led(8);
Button btn(4);

void work(){//콜백의 리턴타입과 매개변수가 같아야 한다 함수의 이름은 상관없음
    led.toggle();
}

void setup(){
    btn.setCallback();
}

void loop(){
    btn.check();
}