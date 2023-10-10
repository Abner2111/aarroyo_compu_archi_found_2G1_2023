#include <SPI.h>


void setup() {
  Serial.begin(115200);
  digitalWrite(SS, HIGH); //disable slave select
  SPI.begin();
  SPI.setCloclDivider(SPI_CLOCK_DIV0); //divide the clock by 0
}

void loop() {
  // put your main code here, to run repeatedly:
  char c;
  digitalWrite(SS, LOW); //enable Slave Select
  for (const char * p = "Hello World!\r"; c = *p; p++){
    SPI.transfer(c);
    Serial.print(c);
  }

  digitalWrite(SS, HIGH); // disable Slave Select
  delay(2000);
}
