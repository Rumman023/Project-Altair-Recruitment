#include <Encoder.h>  //Accessing header files of encoder

const int encoderChannel1 = 2; //Defining encoder channel A to arduino pin 2
const int encoderChannel2 = 3; //Defining encoder channel B to digital pin 3
const int outputPin1 = 5; //Defining output pin 1 to arduino pin 5
const int outputPin2 = 6; //Defining output pin 1 to arduino pin 6

Encoder encoder(encoderChannel1, encoderChannel2); //Initialising the encoder

//Encoder related variables
int encoderPosition = 0;
int encoderRotations = 0;

void setup()
{
  Serial.begin(9600); //Initializing serial line
  pinMode(outputPin1, OUTPUT); //Settting outputPin1 to the output of arduino
  pinMode(outputPin2, OUTPUT); //Settting outputPin1 to the output of arduino
}


//RPM calculating function
int calculateRPM(int rotations, unsigned long timeMillis)
{
  float time = (float)timeMillis / 1000.0; //Converting milisecond into second
  float rpm = (float)rotations / time * 60.0; //RPM calculation
  return (int)rpm; //returning the calculated RPM value in integer form
}

void loop()
{
  analogWrite(outputPin1, 30); //30 Hz PWM signal applied to output pin 5
  analogWrite(outputPin2, 0); //0 Hz PWM signal applied to output pin 6

  //Encoder position and rotation calculation
  encoderPosition = encoder.read() / 10;
  encoderRotations = abs(encoderPosition) / 10;

  //Simulation run time calculation
  unsigned long runTime = millis();

  //Calculating RPM in every second
  if (runTime >= 1000)
  { 
    delay(1000); //printing RPM on serial monitor after 1 sec delay
    
    //Printing on the serial monitor
    Serial.print("RPM: ");
    Serial.println(calculateRPM(encoderRotations, runTime));
    //Resetting runtime and encoder rotation for next second
    runTime = 0;
    encoderRotations = 0;
  }
}
