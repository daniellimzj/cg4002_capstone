#include <Arduino.h>

#define PLAYER_NUM 1   // change depending on whether vest is for player 1 or 2
// 1 means that this beetle will be on the vest of player 1

#define IR_RECEIVE_PIN 2
#define BUZZER_PIN 3
#define INDICATOR_LED_PIN 4
#define DECODE_NEC
#define IR_USE_AVR_TIMER1 //to avoid conflict with buzzer using timer 2

#include <IRremote.hpp> //https://github.com/Arduino-IRremote/Arduino-IRremote

//values expected from sender
#define PLAYER_1_SEND_ADDRESS 0xA906
#define PLAYER_2_SEND_ADDRESS 0x6509
#define RECEIVE_COMMAND 0x0E 

#define LED_FLASH_INTERVAL 100 //time between LED flashes in milliseconds

void initReceiver() {
  IrReceiver.begin(IR_RECEIVE_PIN/*, ENABLE_LED_FEEDBACK*/);
  pinMode(INDICATOR_LED_PIN, OUTPUT);
  digitalWrite(INDICATOR_LED_PIN, LOW);
}

void flashIndicator() {
    digitalWrite(INDICATOR_LED_PIN, HIGH);
    tone(BUZZER_PIN, 4000);
    delay(LED_FLASH_INTERVAL);
    digitalWrite(INDICATOR_LED_PIN, LOW);
    noTone(BUZZER_PIN);
    delay(LED_FLASH_INTERVAL);
    digitalWrite(INDICATOR_LED_PIN, HIGH);
    tone(BUZZER_PIN, 4000);
    delay(LED_FLASH_INTERVAL);
    digitalWrite(INDICATOR_LED_PIN, LOW);
    noTone(BUZZER_PIN);
}

boolean senseReceiver() {
    boolean isDetected = false;
    if (IrReceiver.decode()) {
        if (IrReceiver.decodedIRData.command == RECEIVE_COMMAND) {
            if ((PLAYER_NUM == 1 && IrReceiver.decodedIRData.address == PLAYER_2_SEND_ADDRESS) || 
            (PLAYER_NUM == 2 && IrReceiver.decodedIRData.address == PLAYER_1_SEND_ADDRESS)) {
              isDetected = true;
              flashIndicator();
            }
        }
        IrReceiver.resume(); // Enable receiving of the next value
    }
    return isDetected;
}
