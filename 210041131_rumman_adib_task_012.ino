#include <Wire.h>

#define SLAVE_ADDRESS 8 // Defining the slave address

void setup() {
  Wire.begin(SLAVE_ADDRESS);     // Initializing the Slave Arduino
  Wire.onReceive(receiveEvent); // Registering receiveEvent function for rthe incoming message
  Serial.begin(9600); // Start serial communication
}

void loop() {
  // The Slave doesn't need to do anything in the loop.
}

void receiveEvent(int byteCount) {
  while (Wire.available()) {
    char receivedChar = Wire.read(); // Reading incoming message by character
    Serial.print(receivedChar);      // Printing the received characters as message
  }
}
