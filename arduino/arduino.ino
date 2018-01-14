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

int pos = 90;    // variable to store the servo position
const int servoPin = 9;
const int tiltPin = 2;
const int tiltDirPin = 4;
const int tiltAmount = 30; 

void setup() {
  Serial.begin(9600);
  myservo.attach(servoPin);  // attaches the servo on pin 9 to the servo object
  myservo.write(pos);

  pinMode(tiltPin, INPUT);
  pinMode(tiltDirPin, INPUT);
  //Serial.print(pos);

}

void loop() {

  if (digitalRead(tiltPin) == HIGH){ //tilting to commence
      if(digitalRead(tiltDirPin) == HIGH){
          myservo.write(pos + tiltAmount);
      } else {
          myservo.write(pos - tiltAmount);
      }
  } else {
  	myservo.write(pos); 
  }

  
}
