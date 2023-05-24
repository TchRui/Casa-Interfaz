#include <Servo.h>
const int led1 = 13;
Servo servo1;

void setup() {
  // put your setup code here, to run once:
  pinMode(led1, OUTPUT);
  servo1.attach(3); 
  serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    char data = Serial.read();
    if (data == 'H') {
      digitalWrite(led1, HIGH);
    } else if (data == 'L') {
      digitalWrite(led1, LOW);
    }
  }
}
