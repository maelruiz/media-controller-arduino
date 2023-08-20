const int joystickXPin = A0;      // Analog input pin for X-axis
const int joystickYPin = A1;      // Analog input pin for Y-axis
const int joystickButtonPin = 2;  // Digital input pin for button
const int potentiometerPin = A2;

void setup() {
  Serial.begin(9600); // Initialize serial communication with baud rate 9600

  pinMode(joystickButtonPin, INPUT_PULLUP);  // Use internal pull-up resistor
  
}

void loop() {
  int xValue = analogRead(joystickXPin);
  int yValue = analogRead(joystickYPin);
  int buttonState = digitalRead(joystickButtonPin);
  int potValue = analogRead(potentiometerPin);

  // Map the joystick values to the desired range
  int mappedX = map(xValue, 0, 1023, -100, 100);
  int mappedY = map(yValue, 0, 1023, -100, 100);
  
  // Map the potentiometer value to a volume range (0-100)
  int volume = map(potValue, 0, 1023, 0, 100);

  // Play or pause the media
  if (buttonState == LOW) {
    Serial.println("Pause");
    delay(1000);
  }
  
  // Skip to next or previous track

  if (mappedY < -60) {
    Serial.println("Previous");

  } else if (mappedY > 60) {
    Serial.println("Next");

  } else if (mappedX < -60) {
    Serial.println("Down");

  } else if (mappedX > 60) {
    Serial.println("Up");

  } 
  
  else {
    Serial.println("Nothing");

  }
  Serial.println(volume);
  delay(1000);  // Add a small delay to avoid excessive updates
}
