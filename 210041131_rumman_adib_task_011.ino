#include <Wire.h>

#define SLAVE_ADDRESS 8 // Defining the slave address

char message[] = "Project Altair."; //This message will be transmitted

void setup() {
  Wire.begin();        // Initializing the Master Arduino
  Serial.begin(9600); // Start serial communication
}

void loop() {
  Wire.beginTransmission(SLAVE_ADDRESS); // Starting the communication to the slave addressd Arduino
  Wire.write(message); // Transmitting the message
  Wire.endTransmission();  // Ending the transmission

  delay(1000); // 1 second delay before sending another message
}
