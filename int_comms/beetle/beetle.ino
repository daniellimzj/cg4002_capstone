#define START_STATE_ID 1
#define HANDSHAKE_STATE_ID 2
#define DATA_STATE_ID 3

#define TIMEOUT_ACK 80 //testing
#define TIMEOUT_DATA 50 //testing
#define PACKET_SIZE 20

//Packet Definitions (20 bytes each)
struct AckPacket {
  byte packetType = 'A';
  byte padding[18];
  byte checkSum = 'A'; //unsure about this
} ackPacket;

struct DataPacket { //change to mean, median, ...
  byte packetType = 'D';
  float accelData[3]; //x, y, z data points (6 bytes) TODO: WHAT OTHER DATA NEEDED?
  float gyroData[3]; 
  byte padding[5] = {};
  long timestamp; //TODO: need this? if not change padding (4 bytes)
  byte checkSum;
};

//Helper Functions
uint8_t calculateChecksum(uint8_t* packet) { //1 byte
  uint8_t sum = 0;
  for (int i = 0; i < PACKET_SIZE - 1; ++i) {
    sum ^= packet[i];
  }
  return sum;
}

//Packet Sending Functions
void sendDummyData() {
  DataPacket dummyPacket;
  dummyPacket.accelData[0] = 10;
  dummyPacket.accelData[1] = 20;
  dummyPacket.accelData[2] = 30;
  dummyPacket.timestamp = millis();
  dummyPacket.checkSum = calculateChecksum((uint8_t*)&dummyPacket);

  Serial.write((byte*)&dummyPacket, sizeof(dummyPacket));
}

void sendAck() {
  Serial.write((byte*)&ackPacket, sizeof(ackPacket));
}

//State Definitions
class State {
  private:
    char id;

  public:
    State(char id) {this->id = id;}
    char getID() {return id;}

    virtual void init() {}
    virtual void run() {}
};

State* currState;
State* nextState;

class DataState : public State {
  public:
    DataState() : State(DATA_STATE_ID) {}

    void init() override {
      sendDummyData();
    }

    void run() override {
      while (Serial.read() != 'A') { //No ack from laptop
        delay(TIMEOUT_DATA);
        sendDummyData();
      }
    }
} Data_State;

class HandshakeState : public State {
  public:
    HandshakeState() : State(HANDSHAKE_STATE_ID) {}

    void init() override {
      sendAck();
    }

    void run() override {
      while (Serial.available() && Serial.read() != 'A') { //No ack from laptop
        delay(TIMEOUT_ACK);
        sendAck();
      }
    }
} Handshake_State;

class StartState : public State {
  public:
    StartState() : State(START_STATE_ID) {}

    void init() override {
      nextState = &Handshake_State;
    }
} Start_State;

void startBeetle() {
  if (Serial.read() == 'H') {
    nextState = &Handshake_State;
  } else if (Serial.read() == 'A') {
    Serial.println("Initiating Data State");
    nextState = &Data_State;
  }
}

//Main Program Loop
void loop() {
  if (currState->getID() != nextState->getID()) {
    currState = nextState;
    currState->init();
  }
  currState->run();
}

void setup() {
  Serial.begin(115200);
//  currState = &Data_State;
//  nextState = &Data_State;
  currState = &Handshake_State;
  nextState = &Handshake_State;
//  startBeetle();
}
