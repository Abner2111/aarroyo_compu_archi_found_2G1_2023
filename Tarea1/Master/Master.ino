#include <SPI.h>

const int slaveSelectPin = 10;
const byte handshakeMessage = 0xAA;
long timeStamp;
bool handshakeDone;

byte sentMessage;


void setup() {
  // Set the slave select pin as an output:
  pinMode(slaveSelectPin, OUTPUT);
  // Initialize SPI:
  SPI.begin();
  handshakeDone = false;
}

void loop() {

  if(!handshakeDone){
    digitalWrite(slaveSelectPin, LOW); //enable slave select
    SPI.transfer(handshakeMessage); //send handshake
    digitalWrite(slaveSelectPin, HIGH); //disable slave select
    // Wait for a response:
    byte response = SPI.transfer(0x00);

    // Check if the response is the expected handshake message:
    if (response == handshakeMessage) {
      // Handshake successful
      Serial.println("Handshake successful!");
      handshakeDone = true;
    } 
  } else {
    
  }
  

  

  
}