#include <SPI.h>
const int inputPin = A0;
const int slaveSelectPin = 10;
const byte handshakeMessage = 0xAA;//8bits
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
  //Serial.println(analogRead(inputPin)/64);
  if(!handshakeDone){
    digitalWrite(slaveSelectPin, LOW); //enable slave select
    SPI.transfer(handshakeMessage); //send handshake
    digitalWrite(slaveSelectPin, HIGH); //disable slave select
    // Wait for a response:
    
    sentMessage = handshakeMessage;
    byte response = SPI.transfer(0x00);
    Serial.println("HS sent");
    Serial.print("Response: ");
    Serial.println(response/2);

    // Check if the response is the expected handshake message:
    if (response == handshakeMessage/2) {
      // Handshake successful
      Serial.println("Handshake successful!");
      handshakeDone = true;
      timeStamp = millis();
    } 
  } else {
    byte response = SPI.transfer(0x00);
    //Serial.print("Respuesta: ");
    //Serial.println(response);
    if (response!=sentMessage/2){
      sentMessage = analogRead(inputPin)/32;
      digitalWrite(slaveSelectPin, LOW); //enable slave select
      SPI.transfer(sentMessage); //send message
      //Serial.print("Mensaje ");
      //Serial.println(sentMessage);
      digitalWrite(slaveSelectPin, HIGH); //disable slave select
    }
    else{
      sentMessage = analogRead(inputPin)/32; //0x00-0x07 message 
      digitalWrite(slaveSelectPin, LOW); //enable slave select
      SPI.transfer(sentMessage); //send message
      //Serial.print("Mensaje ");
      //Serial.println(sentMessage);
      digitalWrite(slaveSelectPin, HIGH); //disable slave select
      timeStamp = millis();
    }

    if  ((millis()-timeStamp)>=3000){
      handshakeDone = false; //response took longer than 3 seconds
      Serial.println("No response");
    }
  }
  

  

  
}