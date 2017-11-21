int pin=13;
int inp=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(pin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0)
  {
    inp=Serial.read();
    if(inp=='H')
      digitalWrite(pin,HIGH);
    else if (inp=='L')
      digitalWrite(pin,LOW);
  }
}
