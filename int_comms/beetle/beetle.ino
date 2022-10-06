#define START_STATE_ID 1
#define SLEEP_STATE_ID 2
#define HANDSHAKE_STATE_ID 3
#define DATA_STATE_ID 4

#define TIMEOUT_ACK 25  
#define TIMEOUT_DATA 55 
#define PACKET_SIZE 20

volatile int currentID = 1;
volatile int nextID = 2;

// Packet Definitions (20 bytes each)
struct AckPacket
{
  byte packetType = 'A';
  byte padding[18];
  byte checkSum = 'A'; 
} ackPacket;

struct DataPacket
{ 
  byte packetType = 'D';
  float mean; // 4 bytes
  float median;
  float stdDev; //standard deviation
  float range;
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
//  dummyPacket.mean = 10;
//  dummyPacket.median = 20;
//  dummyPacket.stdDev = 30;
//  dummyPacket.range = 40;
  dummyPacket.mean = random(1, 500) / 100.0;
  dummyPacket.median = random(1, 500) / 100.0;
  dummyPacket.stdDev = random(1, 500) / 100.0;
  dummyPacket.range = random(1, 500) / 100.0;
  dummyPacket.isGunShot = false;
  dummyPacket.isHit = false;
  dummyPacket.checkSum = calculateChecksum((uint8_t *)&dummyPacket);

  Serial.write((byte *)&dummyPacket, sizeof(dummyPacket));
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
    sendDummyData();
  }

  void run() override
  {
    while (true) {
      delay(TIMEOUT_DATA);
      if (Serial.read() == 'A') {
//        Serial.println("got ack in data state");
        break;
      } else if (Serial.read() == 'H') {
//        nextState = &Handshake_State;
          nextID = HANDSHAKE_STATE_ID;
        break;
      }
      sendDummyData();
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
//    nextState = &Data_State;
    while (true) {
      delay(TIMEOUT_ACK);
      if (Serial.read() == 'A') {
//        nextState = &Data_State;
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
//        nextState = &Handshake_State;
          nextID = HANDSHAKE_STATE_ID;
      }
    }
} Sleep_State;

class StartState : public State
{
public:
  StartState() : State(START_STATE_ID) {}

  void init() override
  {
//    nextState = &Sleep_State;
    nextID = SLEEP_STATE_ID;
  }
} Start_State;

// Main Program Loop
void setup()
{
  Serial.begin(115200);
  currState = &Start_State;
  nextID = SLEEP_STATE_ID;
}

void loop()
{
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
