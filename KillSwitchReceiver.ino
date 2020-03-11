// RF LINK RECEIVER CODE
#include <VirtualWire.h>

//Define Pins
const int ledPin = 8; //Need to define for power pin

const int rxPin = 11;
int cnt = 0;

//Define States
signed int xval;
int yval;
int zbut;
int cbut;

void setup()
{
  Serial.begin(9600);	// Debugging only
  Serial.println("Initialize RF Link Rx Code");

  //Initialize the IO and ISR
  vw_set_ptt_inverted(true); // Required for DR3100
  vw_setup(2000);	    // Bits per sec
  vw_set_rx_pin(rxPin);         //Pin 2 is connected to "Digital Output" of receiver
  vw_rx_start();           // Start the receiver PLL running

}

void loop()
{
  //Set buffer array based on max message length
  uint8_t buf[VW_MAX_MESSAGE_LEN];

  //Set variable to indicate buffer length
  uint8_t buflen = VW_MAX_MESSAGE_LEN;

  if (vw_get_message(buf, &buflen)) // Non-blocking
  {
    cnt++;
    // Flash status LED to show received data
    digitalWrite(13, true); 
    xval = (buf[1]<<8)+buf[0];;
    yval = (buf[3]<<8)+buf[2];
    zbut = (buf[5]<<8)+buf[4];;
    cbut = (buf[7]<<8)+buf[6];;
    
    if (cnt%50 == 0) {
      Serial.print("The x value is: ");
      Serial.print(xval);
      Serial.println("");
      Serial.print("The y value is: ");
      Serial.print(yval);
      Serial.println("");
      Serial.print("The z button is: ");
      Serial.print(zbut);
      Serial.println("");
      Serial.print("The c button is: ");
      Serial.print(cbut);
      Serial.println("");
    }
  }
}
