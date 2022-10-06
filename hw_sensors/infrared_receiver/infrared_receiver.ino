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

void setup() {
  Serial.begin(115200);
  IrReceiver.begin(IR_RECEIVE_PIN/*, ENABLE_LED_FEEDBACK*/);
//  Serial.print("Ready to receive IR signals of protocols: ");
//  printActiveIRProtocols(&Serial);
//  Serial.print("at pin ");
//  Serial.println(IR_RECEIVE_PIN);
  pinMode(INDICATOR_LED_PIN, OUTPUT);
  digitalWrite(INDICATOR_LED_PIN, LOW);
}

void loop() {
    if (IrReceiver.decode()) {
//        IrReceiver.printIRResultShort(&Serial); // Print a short summary of received data
//        if (IrReceiver.decodedIRData.protocol == UNKNOWN) {
//            Serial.println("Received noise or an unknown (or not yet enabled) protocol");
//            // We have an unknown protocol here, print more info
//            IrReceiver.printIRResultRawFormatted(&Serial, true);
//        }

        if (IrReceiver.decodedIRData.address == RECEIVE_ADDRESS && IrReceiver.decodedIRData.command == RECEIVE_COMMAND) {
//          Serial.println("Command received");

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
//          delay(100);
        }
//        Serial.println();

        IrReceiver.resume(); // Enable receiving of the next value
    }
}
