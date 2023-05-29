#include <Servo.h>

const int led1 = 13;
const int led2 = 12;
const int led3 = 11;
const int led4 = 10;
const int led5 = 9;
const int led6 = 8;
const int led7 = 7;


Servo servo1;

void setup() {
  // put your setup code here, to run once:
  pinMode(led1, OUTPUT);
  servo1.attach(3); 
  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
  char data = Serial.read();
  switch (data) {
    case 'A':
      digitalWrite(led1, HIGH);
      break;
    case 'a':
      digitalWrite(led1, LOW);
      break;
    case 'B':
      digitalWrite(led2, HIGH);
      break;
    case 'b':
      digitalWrite(led2, LOW);
      break;
    case 'C':
      digitalWrite(led3, HIGH);
      break;
    case 'c':
      digitalWrite(led3, LOW);
      break;
    case 'D':
      digitalWrite(led4, HIGH);
      break;
    case 'd':
      digitalWrite(led4, LOW);
      break;
    case 'E':
      digitalWrite(led5, HIGH);
      break;
    case 'e':
      digitalWrite(led5, LOW);
      break;
    case 'F':
      digitalWrite(led6, HIGH);
      break;
    case 'f':
      digitalWrite(led6, LOW);
      break;
    case 'G':
      digitalWrite(led7, HIGH);
      break;
    case 'g':
      digitalWrite(led7, LOW);
      break;
    default:
      break;
    }
  }
}
