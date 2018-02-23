int potPin = 2;    // select the input pin for the potentiometer
int val=0,dval = 341;     //val from potentiometer,3 posible direction manipulation
int dir=0; //to get direction of handle

void setup() {
  pinMode(ledPin, OUTPUT);  // declare the ledPin as an OUTPUT
}

int getPVal() {
  val = analogRead(potPin);    // read the value from the sensor
  val/=dval,val--;//val can have 3 values -1,0,1 from 0-340,342-681,682-1023 levels
  retun val;
}
