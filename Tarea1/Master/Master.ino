#include <SPI.h>
const int inputPin = A0;
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
  timeStamp = millis();
  Serial.begin(9600);
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
      timeStamp = millis();
    } 
  } else {
    byte response = SPI.transfer(0x00);
    if (response!=sentMessage){
      digitalWrite(slaveSelectPin, LOW); //enable slave select
      SPI.transfer(message); //send message
      digitalWrite(slaveSelectPin, HIGH); //disable slave select
    }
    else{
      byte message = AnalogRead(inputPin)/128;
      digitalWrite(slaveSelectPin, LOW); //enable slave select
      SPI.transfer(message); //send message
      digitalWrite(slaveSelectPin, HIGH); //disable slave select
      sentMessage = message;
      timeStamp = millis();
    }

    if  ((millis-timeStamp)>=3000){
      handshakeDone = false; //response took longer than 3 seconds
      Serial.println("No response");
    }
  }
  

  

  
}