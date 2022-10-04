#include <Arduino.h>
#include <JC_Button.h> // https://github.com/JChristensen/JC_Button

#define PUSHBUTTON_PIN 2
#define IR_SEND_PIN 3
#define LED_PIN 4

//values to transmit to receiver
#define SEND_ADDRESS 0xA906 
#define SEND_COMMAND 0x0E
#define SEND_NUMBER_OF_REPEATS 0

#include <IRremote.hpp>

Button myButton(PUSHBUTTON_PIN); //create button object

void initEmmiter() {
  myButton.begin(); // initialize the button object
  IrSender.begin(); // Start with IR_SEND_PIN as send pin and if NO_LED_FEEDBACK_CODE is NOT defined, enable feedback LED at default feedback LED pin
}

void senseEmmiter(boolean isDetected) {
  // If button pressed, send the code
  myButton.read();
  if (myButton.wasPressed()) {
    IrSender.sendNEC(SEND_ADDRESS, SEND_COMMAND, SEND_NUMBER_OF_REPEATS);
    isDetected = true;

    // light LED
    digitalWrite(LED_PIN, HIGH);
    delay(100);
    digitalWrite(LED_PIN, LOW);
  }
}
