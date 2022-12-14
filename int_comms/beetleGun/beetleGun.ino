#include "infraredEmmiter.h"

#define START_STATE_ID 1
#define IDLE_STATE_ID 2
#define HANDSHAKE_STATE_ID 3
#define DATA_STATE_ID 4

#define TIMEOUT_ACK 50 
#define TIMEOUT_DATA 50 
#define PACKET_SIZE 20

volatile int nextID = IDLE_STATE_ID;
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

struct NotifyPacket
{
  byte packetType = 'N';
  byte padding[18];
  byte checksum = 'N';
} notifyPacket;

struct DataPacket
{ 
  byte packetType = (PLAYER_NUM == 1) ? 'G' : 'J';
  float mean;
  float range;
  float variance;
  float median;
  boolean isGunShot;
  boolean isHit;
  byte checkSum;
};

// Helper Functions
uint8_t calculateChecksum(uint8_t *packet)
{
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

void sendGunData()
{
  DataPacket gunPacket;

  gunPacket.mean = 0;
  gunPacket.range = 0;
  gunPacket.variance = 0;
  gunPacket.median = 0;
  gunPacket.isGunShot = isDetected;
  gunPacket.isHit = false;
  gunPacket.checkSum = calculateChecksum((uint8_t *)&gunPacket);

  Serial.write((byte *)&gunPacket, sizeof(gunPacket));
}

void sendAck()
{
  Serial.write((byte *)&ackPacket, sizeof(ackPacket));
}

void sendNotify()
{
  Serial.write((byte *)&notifyPacket, sizeof(notifyPacket));
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

  void run() override
  {
      delay(TIMEOUT_DATA);
      if (Serial.read() == 'R') {
        reloadGun();
      } else if (Serial.read() == 'A') {
        isDetected = false;
        nextID = IDLE_STATE_ID;
      } else if (Serial.read() == 'H') {
        nextID = HANDSHAKE_STATE_ID;
        handshakeDone = false;
      }
      if (isDetected) {
        sendGunData();
      }
      if (counter >= 30) {
        sendNotify();
        counter = 0;
      }
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

class IdleState : public State
{
  public:
    IdleState() : State(IDLE_STATE_ID) {}

    void run() override
    {
      if (Serial.read() == 'H') {
          nextID = HANDSHAKE_STATE_ID;
      } else if (handshakeDone) {
        nextID = DATA_STATE_ID;
      }
    }
} Idle_State;

class StartState : public State
{
public:
  StartState() : State(START_STATE_ID) {}

  void init() override
  {
    nextID = IDLE_STATE_ID;
  }
} Start_State;

// Main Program Loop
void setup()
{
  Serial.begin(115200);
  currState = &Start_State;
  nextID = IDLE_STATE_ID;
  initEmmiter();
}

void loop()
{
  counter += 1;
  isDetected = senseEmmiter();
  
  switch (nextID) {
    case START_STATE_ID:
      nextState = &Start_State;
      break;
    case IDLE_STATE_ID:
      nextState = &Idle_State;
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
