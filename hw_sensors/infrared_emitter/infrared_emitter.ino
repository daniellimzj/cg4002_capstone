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

void setup() {
//  Serial.begin(115200);
  myButton.begin(); // initialize the button object
  IrSender.begin(); // Start with IR_SEND_PIN as send pin and if NO_LED_FEEDBACK_CODE is NOT defined, enable feedback LED at default feedback LED pin

//  Serial.print("Ready to send IR signals at pin ");
//  Serial.println(IR_SEND_PIN);
}

void loop() {
  // If button pressed, send the code
  myButton.read();
  if (myButton.wasPressed()) {
//    Serial.println("Sending data");
//    Serial.flush();

    IrSender.sendNEC(SEND_ADDRESS, SEND_COMMAND, SEND_NUMBER_OF_REPEATS);

    // light LED
    digitalWrite(LED_PIN, HIGH);
    delay(100);
    digitalWrite(LED_PIN, LOW);
  }
//  delay(250);  // delay must be greater than 5 ms (RECORD_GAP_MICROS), otherwise the receiver sees it as one long signal
}
