String t;
int pin=13;
void setup() {
  // put your setup code here, to run once:
  pinMode(pin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(Serial.available()) //Capturing letters from the established serial connection
  {
    delay(10);
    char c = Serial.read();
    t += c;//t = t + c; (O, O+P = OP, OP + E = OPE, OPE + N = OPEN),OPEN+CLOSE =OPENCLOSE
  }
  if(t.length()>0)
  {
    if(t=="ON")
    {
      Serial.print("ON");
      digitalWrite(pin,HIGH);
    }
    if(t=="OFF")
    {
      Serial.print("OFF");
      digitalWrite(pin,LOW);
    }
    t="";
  }
  
}
