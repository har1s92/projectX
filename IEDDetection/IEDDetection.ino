//TEENSY IED DETECTION CODE

// declare analog input pin
const int analogInPin = A0;

// declare digital output pin
const int digitalOutputPin = 0;

void setup() {
  // initialize pin mode
  pinMode(digitalOutputPin, OUTPUT);
}

void loop() {
  // read the analog value on the analogInPin (value from 0 to 1023)
  int analogInput = analogRead(analogInPin);
  
  // calculate the voltage on the analogInPin (3.22 mV per unit)
  int voltageInput = analogInput * 0.00322;
  
  // write the output of the threshold to the output pin
  digitalWrite(digitalOutputPin, isAboveThreshold(analogInput));
}

int isAboveThreshold(int analogReading) {
  // set the analog thershold value
  int analogThreshold = 0;

  // compare the analog reading to the threshold
  if (analogReading >= analogThreshold) {
    return HIGH;
  }
  else {
    return LOW;
  }
}
