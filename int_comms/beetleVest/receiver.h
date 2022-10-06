#include <Arduino.h>
#define IR_RECEIVE_PIN 2
#define BUZZER_PIN 3
#define INDICATOR_LED_PIN 4
#define DECODE_NEC
#define IR_USE_AVR_TIMER1 //to avoid conflict with buzzer using timer 2
#include <IRremote.hpp> //https://github.com/Arduino-IRremote/Arduino-IRremote

//values expected from sender
#define RECEIVE_ADDRESS 0xA906 
#define RECEIVE_COMMAND 0x0E 

void initReceiver() {
  IrReceiver.begin(IR_RECEIVE_PIN/*, ENABLE_LED_FEEDBACK*/);
  pinMode(INDICATOR_LED_PIN, OUTPUT);
  digitalWrite(INDICATOR_LED_PIN, LOW);
}

boolean senseReceiver() {
    boolean isDetected = false;
    if (IrReceiver.decode()) {

        if (IrReceiver.decodedIRData.address == RECEIVE_ADDRESS && IrReceiver.decodedIRData.command == RECEIVE_COMMAND) {
          isDetected = true;
          //flash the LED & sound the buzzer
          digitalWrite(INDICATOR_LED_PIN, HIGH);
          tone(BUZZER_PIN, 4000);
          delay(100);
          digitalWrite(INDICATOR_LED_PIN, LOW);
          noTone(BUZZER_PIN);
          delay(100);
          digitalWrite(INDICATOR_LED_PIN, HIGH);
          tone(BUZZER_PIN, 4000);
          delay(100);
          digitalWrite(INDICATOR_LED_PIN, LOW);
          noTone(BUZZER_PIN);
        }

        IrReceiver.resume(); // Enable receiving of the next value
    }
    return isDetected;
}
