// RF LINK TRANSMITTER CODE
#include <VirtualWire.h>

const int buttonPin = 8;
const int ledPin = 5;
const int txPin = 2;

void setup()
{
  Serial.begin(9600);	  // Debugging only
  Serial.println("Initialize RF Link Tx Code");

  // Initialise the IO and ISR
  vw_set_ptt_inverted(true); // Required for DR3100
  vw_setup(2000);	    // Bits per sec
  vw_set_tx_pin(txPin);         //Pin 3 is connected to "Digital Output" of transmitter

  //Set pins as input for buttons
  pinMode(buttonPin, INPUT);

  //Set pin for LED as status indicator
  pinMode(ledPin, OUTPUT); 
}

void loop()
{
  char senseMsg[4];
  int senseData = 255;
  itoa(senseData,senseMsg,10);
  signed int msg[4] = {-125,256,1,0};

  if(digitalRead(buttonPin) == HIGH) {
    digitalWrite(ledPin, true);  //Flash status LED to show transmitting
    tx_debug(msg); //output message to serial monitor for debugging.
    vw_send((uint8_t *)msg, 8);//send message
    vw_wait_tx(); // Wait until the whole message is gone
    digitalWrite(ledPin, false); //Turn off status LED
  }
}

void tx_debug(int *temp_num){
  //output to serial monitor to indicate which button pressed
  Serial.print("Button was pressed, sending msg = ");
  uint8_t *temp_msg = (uint8_t *)temp_num;
  for (int i=0; i<4; i++) {
    Serial.print(temp_msg[i]);
  }
}

