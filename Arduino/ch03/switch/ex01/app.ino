#include <Led.h>

Led led1(8);
Led led2(9);

int sw1=3; //풀다운
int sw2=4; //풀업

void setup(){
    pinMode(sw1,INPUT);
    pinMode(sw2,INPUT);
}

int v1,v2;

void loop(){
    
    //풀다운 : 평시에 low 누르면 high
    v1 = digitalRead(sw1);
    led1.setValue(v1);
    
    
    //풀업 : 평시에 high 누르면 low
    v2 = digitalRead(sw2);
    led2.setValue(v2);
}