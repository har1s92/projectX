//TEENSY IED DETECTION CODE

// declare analog input pin
const int analogInPin = A0;

// declare digital output pin
const int digitalOutputPin = 0;

// declare the number of loops before adjusting potentiometer
const int saturationLoops = 10;

int saturationCount=0;

void setup() {
  // initialize pin mode
  pinMode(digitalOutputPin, OUTPUT);
}

void loop() {
  // read the analog value on the analogInPin (value from 0 to 1023)
  int analogInput = analogRead(analogInPin);

  if (isSaturated(analogInput)) {
    saturationCount+=1;
  }
  else {
    saturationCount=0;
  }

  if (saturationCount>=saturationLoops) {
    adjustPotentiometer();
  }
  
  // calculate the voltage on the analogInPin (3.22 mV per unit)
  int voltageInput = analogInput * 0.00322;
  
  // write the output of the threshold to the output pin
  digitalWrite(digitalOutputPin, isAboveVoltageThreshold(analogInput));
}

int isAboveVoltageThreshold(int analogReading) {
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

bool isSaturated(int analogReading) {
  int lowThreshold = 5;
  int highThreshold = 1020;
  if (analogReading<lowThreshold || analogReading>highThreshold) {
    return true;
  }
  else {
    return false;
  }
}

void adjustPotentiometer() {
  //need to fill this in with code to get better analog readings
}
