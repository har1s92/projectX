// KILL SWITCH RECEIVER CODE
#include <VirtualWire.h>

//Define Pins
const int ledPin = 8;
const int rxPin = 11;

//Define Kill Switch Code
const char killCommand[4] = "k!ll";

void setup() {
  //Set pin for LED as status indicator
  pinMode(ledPin, OUTPUT);

  //Initialize the IO and ISR
  vw_set_ptt_inverted(true); // Required for DR3100
  vw_setup(2000);	    // Bits per sec
  vw_set_rx_pin(rxPin);         //Pin 2 is connected to "Digital Output" of receiver
  vw_rx_start();           // Start the receiver PLL running

  //Turn on LED
  digitalWrite(ledPin, HIGH);
}

void loop() {
  //Set buffer array based on max message length
  uint8_t buf[VW_MAX_MESSAGE_LEN];

  //Set variable to indicate buffer length
  uint8_t buflen = VW_MAX_MESSAGE_LEN;

  if (vw_get_message(buf, &buflen)) {   
    char message[4] = {buf[0], buf[1], buf[2], buf[3]};
    if (strcmp(message, killCommand)==0) {
      digitalWrite(ledPin, LOW);
    }
  }
}
