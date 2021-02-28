#include<Led.h>

Led led(8);
int sw = 4;

void setup(){
    pinMode(sw,INPUT_PULLUP);
}

void loop(){
    bool o_sw, n_sw//old ,new 약자
}