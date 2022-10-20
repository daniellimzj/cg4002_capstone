#include "sensor.h"

#define PLAYER 1

#define START_STATE_ID 1
#define SLEEP_STATE_ID 2
#define HANDSHAKE_STATE_ID 3
#define DATA_STATE_ID 4

#define TIMEOUT_ACK 25
#define TIMEOUT_DATA 40
#define PACKET_SIZE 20

volatile int nextID = SLEEP_STATE_ID;

volatile boolean handshakeDone = false;
volatile boolean dataReady = false;

// SENSOR
MPU6050 myIMU;

int16_t accX, accY, accZ, gyroX, gyroY, gyroZ;
int16_t filteredAccX, filteredAccY, filteredAccZ, filteredGyroX, filteredGyroY, filteredGyroZ;

unsigned long i = 0;
unsigned long previousMillis = 0;
unsigned long currentMillis;

ExponentialFilter<long> accXFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> accYFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> accZFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> gyroXFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> gyroYFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> gyroZFilter(FILTER_WEIGHT, 0);

// Packet Definitions (16 bytes each)
struct AckPacket
{
  byte packetType = 'A';
  byte padding[18];
  byte checkSum = 'A';
} ackPacket;

struct DataPacket
{
  byte packetType = 'D';
  int16_t accX; // 2 bytes
  int16_t accY;
  int16_t accZ;
  int16_t gyroX;
  int16_t gyroY;
  int16_t gyroZ;
  byte padding[4];
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

// byte getType(uint8_t index) {
//   if (PLAYER == 1) {
//     if (index == ACCEL_X) {
//       return 'a';
//     } else if (index == ACCEL_Y) {
//       return 'b';
//     } else if (index == ACCEL_Z) {
//       return 'c';
//     } else if (index == ROTATE_X) {
//       return 'd';
//     } else if (index == ROTATE_Y) {
//       return 'e';
//     } else if (index == ROTATE_Z) {
//       return 'f';
//     }
//   } else if (PLAYER == 2) {
//     if (index == ACCEL_X) {
//       return 'u';
//     } else if (index == ACCEL_Y) {
//       return 'v';
//     } else if (index == ACCEL_Z) {
//       return 'w';
//     } else if (index == ROTATE_X) {
//       return 'x';
//     } else if (index == ROTATE_Y) {
//       return 'y';
//     } else if (index == ROTATE_Z) {
//       return 'z';
//     }
//   }
// }

void sendArmData()
{
  DataPacket armPacket;

  armPacket.accX = filteredAccX;
  armPacket.accY = filteredAccY;
  armPacket.accZ = filteredAccZ;
  armPacket.gyroX = filteredGyroX;
  armPacket.gyroY = filteredGyroY;
  armPacket.gyroZ = filteredGyroZ;
  armPacket.isGunShot = false;
  armPacket.isHit = false;
  armPacket.checkSum = calculateChecksum((uint8_t *)&armPacket);

  Serial.write((byte *)&armPacket, sizeof(armPacket));
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
    if (dataReady)
    {
      sendArmData();
    }
  }

  void run() override
  {
    //    while (true) {
    //      delay(TIMEOUT_DATA);
    //      if (Serial.read() == 'H') {
    //        nextID = HANDSHAKE_STATE_ID;
    //        handshakeDone = false;
    //        dataReady = false;
    //        break;
    //      } else if (Serial.read() == 'A') {
    //        dataReady = false;
    //        nextID = SLEEP_STATE_ID;
    //        break;
    //      }
    //      sendArmData();
    //    }
    //    delay(TIMEOUT_DATA);
    unsigned long currTime = millis();
    char serialRead = Serial.read();
    while (serialRead != 'H' || serialRead != 'A')
    {
      if (millis() - currTime >= TIMEOUT_DATA)
      {
        break;
      }
      serialRead = Serial.read();
    }
    if (serialRead == 'H')
    {
      nextID = HANDSHAKE_STATE_ID;
      handshakeDone = false;
      dataReady = false;
      //      break;
    }
    else if (serialRead == 'A')
    {
      dataReady = false;
      nextID = SLEEP_STATE_ID;
      //      break;
    }
    sendArmData();
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
    while (true)
    {
      delay(TIMEOUT_ACK);
      if (Serial.read() == 'A')
      {
        nextID = DATA_STATE_ID;
        handshakeDone = true;
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
    if (Serial.read() == 'H')
    {
      nextID = HANDSHAKE_STATE_ID;
    }
    else if (handshakeDone && dataReady)
    {
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

// SENSOR FUNCTIONS
void initSensor()
{
  Serial.begin(115200);

  myIMU.initialize(); // MPU6050 starts in sleep mode, need to wake it up to use it

  myIMU.setDLPFMode(6);

  if (myIMU.getRate() == 0)
  {
    myIMU.setRate((8000 / SAMPLE_RATE) - 1);
  }
  else
  {
    myIMU.setRate((1000 / SAMPLE_RATE) - 1);
  }
  // set initial value for filtered values
  myIMU.getMotion6(&accX, &accY, &accZ, &gyroX, &gyroY, &gyroZ); // take all measurements in same instant
  accXFilter.SetCurrent(accX);
  accYFilter.SetCurrent(accY);
  accZFilter.SetCurrent(accZ);
  gyroXFilter.SetCurrent(gyroX);
  gyroYFilter.SetCurrent(gyroY);
  gyroZFilter.SetCurrent(gyroZ);
}

void getReading()
{
  // put your main code here, to run repeatedly:

  currentMillis = millis();

  if (currentMillis - previousMillis >= SAMPLE_INTERVAL)
  {
    previousMillis = currentMillis;

    myIMU.getMotion6(&accX, &accY, &accZ, &gyroX, &gyroY, &gyroZ); // take all measurements in same instant

    /* filtered values, reduce range to fit into int8_t*/
    accXFilter.Filter(accX);
    filteredAccX = (int16_t)(accXFilter.Current());
    accYFilter.Filter(accY);
    filteredAccY = (int16_t)(accYFilter.Current());
    accZFilter.Filter(accZ);
    filteredAccZ = (int16_t)(accZFilter.Current());
    gyroXFilter.Filter(gyroX);
    filteredGyroX = (int16_t)(gyroXFilter.Current());
    gyroYFilter.Filter(gyroY);
    filteredGyroY = (int16_t)(gyroYFilter.Current());
    gyroZFilter.Filter(gyroZ);
    filteredGyroZ = (int16_t)(gyroZFilter.Current());

    dataReady = true;
  }
}

// Main Program Loop
void setup()
{
  Serial.begin(115200);
  currState = &Start_State;
  nextID = SLEEP_STATE_ID;
  initSensor();
}

void loop()
{
  getReading();
  switch (nextID)
  {
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
