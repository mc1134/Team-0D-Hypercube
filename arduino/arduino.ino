/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 100;    // variable to store the servo position
const int servoPin = 9;
const int tiltPin = 2;
const int tiltDirPin = 4;

void setup() {
  Serial.begin(9600);
  myservo.attach(servoPin);  // attaches the servo on pin 9 to the servo object
  myservo.write(pos);

  pinMode(tiltPin, INPUT);
  pinMode(tiltDirPin, INPUT);
  //Serial.print(pos);

}

void loop() {
  /*if(digitalRead(2) == HIGH && digitalRead(4) == LOW){
    delay(2000);
    myservo.write(pos + 45);
    delay(2000);
    myservo.write(pos);
  }else if(digitalRead(2) == LOW && digitalRead(4) == LOW){
    delay(2000);
    myservo.write(pos - 45);
    delay(2000);
    myservo.write(pos);
  }else if(digitalRead(2) == HIGH && digitalRead(4) == HIGH){
    delay(2000);
    myservo.write(pos);
  }*/

  if (digitalRead(tiltPin) == HIGH){ //tilting to commence
      if(digitalRead(tiltDirPin) == HIGH){
          myservo.write(pos + 45);
      } else {
          myservo.write(pos - 45);
      }
  } else {
  	myservo.write(pos); 
  }

  /*if(1 && 2){
    delay(2000);
    myservo.write(pos + 45);
    delay(2000);
    myservo.write(pos);
  }else if(digitalRead(2) == LOW && digitalRead(4) == LOW){
    delay(2000);
    myservo.write(pos - 45);
    delay(2000);
    myservo.write(pos);
  }else if(digitalRead(2) == HIGH && digitalRead(4) == HIGH){
    delay(2000);
    myservo.write(pos);
  }*/

  /*for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // goes from 180 degrees to 0 degrees
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }*/
}
