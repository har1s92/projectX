// KILL SWITCH TRANSMITTER CODE
#include <VirtualWire.h>

const int buttonPin = 11;
const int txPin = 12;

void setup() {
  
  // Initialise the IO and ISR
  vw_set_ptt_inverted(true); // Required for DR3100
  vw_setup(2000);	    // Bits per sec
  vw_set_tx_pin(txPin);         //Pin 3 is connected to "Digital Output" of transmitter

  //Set pins as input for buttons
  pinMode(buttonPin, INPUT);
}

void loop() {
  
  char killCommand[4] = {'k', '!', 'l', 'l'};

  if (digitalRead(buttonPin) == HIGH) {
    vw_send((uint8_t *)killCommand, 8);//send message
    vw_wait_tx(); // Wait until the whole message is gone
  }
}
