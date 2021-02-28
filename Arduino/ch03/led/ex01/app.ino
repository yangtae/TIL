//led 풀업/풀다운 연결핀
const int pu_led_pin = 10; //풀업
const int pd_led_pin = 6;  //풀다운

void setup()
{
	pinMode(pu_led_pin,OUTPUT);
    pinMode(pd_led_pin,OUTPUT);
}

void loop()
{
	digitalWrite(pu_led_pin,LOW);
    digitalWrite(pd_led_pin,HIGH);
}
