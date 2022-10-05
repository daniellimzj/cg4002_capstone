#include <Arduino.h>
#include <IRremote.hpp>

// Communications Definitions
#define START_STATE_ID 1
#define SLEEP_STATE_ID 2
#define HANDSHAKE_STATE_ID 3
#define DATA_STATE_ID 4

#define TIMEOUT_ACK 50  
#define TIMEOUT_DATA 50 
#define PACKET_SIZE 20

// Hardware Definitions
#define IR_RECEIVE_PIN 2
#define BUZZER_PIN 3
#define INDICATOR_LED_PIN 4
#define DECODE_NEC
#define IR_USE_AVR_TIMER1 //to avoid conflict with buzzer using timer 2

#define RECEIVE_ADDRESS 0xA906 
#define RECEIVE_COMMAND 0x0E 

volatile int nextID = SLEEP_STATE_ID;
volatile boolean handshakeDone = false;
volatile boolean isDetected = false;
volatile long counter = 0;

// Packet Definitions (20 bytes each)
struct AckPacket
{
  byte packetType = 'A';
  byte padding[18];
  byte checkSum = 'A'; 
} ackPacket;

struct DataPacket
{ 
  byte packetType = 'V';
  float mean; // 4 bytes
  float range;
  float variance;
  float median;
  boolean isGunShot;
  boolean isHit;
  byte checkSum;
};

// Helper Functions
uint8_t calculateChecksum(uint8_t *packet)
{ // 1 byte
  uint8_t sum = 0;
  for (int i = 0; i < PACKET_SIZE - 1; ++i)
  {
    sum ^= packet[i];
  }
  return sum;
}

// Packet Sending Functions
void sendDummyData()
{
  DataPacket dummyPacket;
  
  dummyPacket.mean = random(1, 500) / 100.0;
  dummyPacket.median = random(1, 500) / 100.0;
  dummyPacket.range = random(1, 500) / 100.0;
  dummyPacket.variance = random(1, 500) / 100.0;
  dummyPacket.isGunShot = false;
  dummyPacket.isHit = false;
  dummyPacket.checkSum = calculateChecksum((uint8_t *)&dummyPacket);

  Serial.write((byte *)&dummyPacket, sizeof(dummyPacket));
}

void sendVestData()
{
  DataPacket vestPacket;

  vestPacket.mean = 0;
  vestPacket.range = 0;
  vestPacket.variance = 0;
  vestPacket.median = 0;
  vestPacket.isGunShot = false;
  vestPacket.isHit = isDetected;
  vestPacket.checkSum = calculateChecksum((uint8_t *)&vestPacket);

  Serial.write((byte *)&vestPacket, sizeof(vestPacket));
}

void sendAck()
{
  Serial.write((byte *)&ackPacket, sizeof(ackPacket));
}

// State Definitions
class State
{
private:
  char id;

public:
  State(char id) { this->id = id; }
  char getID() { return id; }

  virtual void init() {}
  virtual void run() {}
};

State *currState;
State *nextState;

class DataState : public State
{
public:
  DataState() : State(DATA_STATE_ID) {}

  void init() override
  {
//      if (isDetected) {
//        sendVestData();
//      }
//      if (counter >= 39) {
//        sendAck();
//        counter = 0;
//      }
  }

  void run() override
  {
//    while (true) {
      delay(TIMEOUT_DATA);
      if (Serial.read() == 'H') {
        nextID = HANDSHAKE_STATE_ID;
        handshakeDone = false;
//        break;
      } else if (Serial.read() == 'A') {
        isDetected = false;
        nextID = SLEEP_STATE_ID;
//        break;
      }
      if (isDetected) {
        sendVestData();
      }
      if (counter >= 39) {
        sendAck();
        counter = 0;
      }
//    }
  }
} Data_State;

class HandshakeState : public State
{
public:
  HandshakeState() : State(HANDSHAKE_STATE_ID) {}

  void init() override
  {
    sendAck();
  }

  void run() override
  {
    while (true) {
      delay(TIMEOUT_ACK);
      if (Serial.read() == 'A') {
        handshakeDone = true;
        nextID = DATA_STATE_ID;
        break;
      }
      sendAck();
    }
  }
} Handshake_State;

class SleepState : public State
{
  public:
    SleepState() : State(SLEEP_STATE_ID) {}

    void run() override
    {
      if (Serial.read() == 'H') {
          nextID = HANDSHAKE_STATE_ID;
      } else if (handshakeDone) {
        nextID = DATA_STATE_ID;
      }
    }
} Sleep_State;

class StartState : public State
{
public:
  StartState() : State(START_STATE_ID) {}

  void init() override
  {
    nextID = SLEEP_STATE_ID;
  }
} Start_State;

// Hardware Codes
void initReceiver() {
  IrReceiver.begin(IR_RECEIVE_PIN/*, ENABLE_LED_FEEDBACK*/);
  pinMode(INDICATOR_LED_PIN, OUTPUT);
  digitalWrite(INDICATOR_LED_PIN, LOW);
}


void senseReceiver() {
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
        IrReceiver.resume();
        IrReceiver.resume();
        IrReceiver.resume();
        IrReceiver.resume();
    }
}

// Main Program Loop
void setup()
{
  Serial.begin(115200);
  currState = &Start_State;
  nextID = SLEEP_STATE_ID;
  initReceiver();
}

void loop()
{
  counter += 1;
//  Serial.println(counter);
  senseReceiver();
  
  switch (nextID) {
    case START_STATE_ID:
      nextState = &Start_State;
      break;
    case SLEEP_STATE_ID:
      nextState = &Sleep_State;
      break;
    case HANDSHAKE_STATE_ID:
      nextState = &Handshake_State;
      break;
    case DATA_STATE_ID:
      nextState = &Data_State;
      break;
  }
  if (currState->getID() != nextState->getID())
  {
    currState = nextState;
    currState->init();
  }
  currState->run();
}
