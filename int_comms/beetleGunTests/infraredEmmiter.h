#include <Arduino.h>
#include <JC_Button.h> // https://github.com/JChristensen/JC_Button

#define PLAYER_NUM 1   // change depending on whether gun is for player 1 or 2

#define PUSHBUTTON_PIN 2
#define IR_SEND_PIN 3
#define LED_PIN 4

// values to transmit to receiver
#define PLAYER_1_SEND_ADDRESS 0xA906
#define PLAYER_2_SEND_ADDRESS 0x6509
#define SEND_COMMAND 0x0E
#define SEND_NUMBER_OF_REPEATS 0

#include <IRremote.hpp> // https://github.com/Arduino-IRremote/Arduino-IRremote

#define MAX_BULLETS 6

Button myButton(PUSHBUTTON_PIN); // create button object

volatile uint8_t numberOfBullets = MAX_BULLETS;

void initEmmiter()
{
  myButton.begin(); // initialize the button object
  IrSender.begin(); // Start with IR_SEND_PIN as send pin and if NO_LED_FEEDBACK_CODE is NOT defined, enable feedback LED at default feedback LED pin
  pinMode(LED_PIN, OUTPUT);
}

boolean senseEmmiter()
{
  boolean isDetected = false;
  myButton.read();
  if (myButton.wasPressed())
  {
    isDetected = true;
    // Only send IR signal if player has bullets
    if (numberOfBullets > 0)
    {
      if (PLAYER_NUM == 1) {
      IrSender.sendNEC(PLAYER_1_SEND_ADDRESS, SEND_COMMAND, SEND_NUMBER_OF_REPEATS);
      } 
      else if (PLAYER_NUM == 2) {
      IrSender.sendNEC(PLAYER_2_SEND_ADDRESS, SEND_COMMAND, SEND_NUMBER_OF_REPEATS);
      } 
      numberOfBullets--;
      // light LED
      digitalWrite(LED_PIN, HIGH);
      delay(100);
      digitalWrite(LED_PIN, LOW);
    }
    else
    {
      // flash LED
      digitalWrite(LED_PIN, HIGH);
      delay(100);
      digitalWrite(LED_PIN, LOW);
      delay(100);
      digitalWrite(LED_PIN, HIGH);
      delay(100);
      digitalWrite(LED_PIN, LOW);
    }
  }
  return isDetected;
}

void reloadGun()
{
  numberOfBullets = MAX_BULLETS;
}
