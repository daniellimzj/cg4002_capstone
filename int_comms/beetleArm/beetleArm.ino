#include "sensorArm.h"

#define START_STATE_ID 1
#define SLEEP_STATE_ID 2
#define HANDSHAKE_STATE_ID 3
#define DATA_STATE_ID 4

#define TIMEOUT_ACK 25  
#define TIMEOUT_DATA 35
#define PACKET_SIZE 20

volatile int nextID = SLEEP_STATE_ID;

volatile int current = ACCEL_X;
volatile boolean handshakeDone = false;

// SENSOR
MPU6050 myIMU;

int16_t accX, accY, accZ, gyroX, gyroY, gyroZ;
int16_t filteredAccX, filteredAccY, filteredAccZ, filteredGyroX, filteredGyroY, filteredGyroZ;

int16_t readings[NUM_FEATURES][NUM_READINGS];
float stats[NUM_FEATURES][NUM_STATS];

unsigned long i = 0;
unsigned long previousMillis = 0;
unsigned long currentMillis;

ExponentialFilter<long> accXFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> accYFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> accZFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> gyroXFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> gyroYFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> gyroZFilter(FILTER_WEIGHT, 0);

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
  float range;
  float variance;
  float median;
  boolean isGunShot;
  boolean isHit;
  byte checkSum;
};

//struct DataPacket
//{ 
//  byte packetType = 'D';
//  float mean0; // 4 bytes
//  float median0;
//  float range0;
//  float variance0;
//  float mean1; // 4 bytes
//  float median1;
//  float range1;
//  float variance1;
//  float mean2; // 4 bytes
//  float median2;
//  float range2;
//  float variance2;
//  float mean3; // 4 bytes
//  float median3;
//  float range3;
//  float variance3;
//  float mean4; // 4 bytes
//  float median4;
//  float range4;
//  float variance4;
//  float mean5; // 4 bytes
//  float median5;
//  float range5;
//  float variance5;
//  boolean isGunShot;
//  boolean isHit;
//  byte checkSum;
//};

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
//void sendDummyData()
//{
//  DataPacket dummyPacket;
//  
//  dummyPacket.mean0 = random(1, 500) / 100.0;
//  dummyPacket.median0 = random(1, 500) / 100.0;
//  dummyPacket.range0 = random(1, 500) / 100.0;
//  dummyPacket.variance0 = random(1, 500) / 100.0;
//  dummyPacket.isGunShot = false;
//  dummyPacket.isHit = false;
//  dummyPacket.checkSum = calculateChecksum((uint8_t *)&dummyPacket);
//
//  Serial.write((byte *)&dummyPacket, sizeof(dummyPacket));
//}

void sendArmData(int index)
{
  DataPacket armPacket;
  
  armPacket.mean = stats[index][MEAN];
  armPacket.range = stats[index][RANGE];
  armPacket.variance = stats[index][VARIANCE];
  armPacket.median = stats[index][MEDIAN];
  armPacket.isGunShot = false;
  armPacket.isHit = false;
  armPacket.checkSum = calculateChecksum((uint8_t *)&armPacket);
//  Serial.println(armPacket.mean);
//  Serial.println(armPacket.median);
//  Serial.println(armPacket.range);
//  Serial.println(armPacket.variance);

  Serial.write((byte *)&armPacket, sizeof(armPacket));
}

//void sendArmData()
//{
//  DataPacket armPacket;
//  
//  armPacket.mean0 = stats[ACCEL_X][MEAN];
//  armPacket.median0 = stats[ACCEL_X][MEDIAN];
//  armPacket.range0 = stats[ACCEL_X][RANGE];
//  armPacket.variance0 = stats[ACCEL_X][VARIANCE];
//  armPacket.mean1 = stats[ACCEL_Y][MEAN];
//  armPacket.median1 = stats[ACCEL_Y][MEDIAN];
//  armPacket.range1 = stats[ACCEL_Y][RANGE];
//  armPacket.variance1 = stats[ACCEL_Y][VARIANCE];
//  armPacket.mean2 = stats[ACCEL_Z][MEAN];
//  armPacket.median2 = stats[ACCEL_Z][MEDIAN];
//  armPacket.range2 = stats[ACCEL_Z][RANGE];
//  armPacket.variance2 = stats[ACCEL_Z][VARIANCE];
//  armPacket.mean3 = stats[ROTATE_X][MEAN];
//  armPacket.median3 = stats[ROTATE_X][MEDIAN];
//  armPacket.range3 = stats[ROTATE_X][RANGE];
//  armPacket.variance3 = stats[ROTATE_X][VARIANCE];
//  armPacket.mean4 = stats[ROTATE_Y][MEAN];
//  armPacket.median4 = stats[ROTATE_Y][MEDIAN];
//  armPacket.range4 = stats[ROTATE_Y][RANGE];
//  armPacket.variance4 = stats[ROTATE_Y][VARIANCE];
//  armPacket.mean5 = stats[ROTATE_Z][MEAN];
//  armPacket.median5 = stats[ROTATE_Z][MEDIAN];
//  armPacket.range5 = stats[ROTATE_Z][RANGE];
//  armPacket.variance5 = stats[ROTATE_Z][VARIANCE];
//  armPacket.isGunShot = false;
//  armPacket.isHit = false;
//  armPacket.checkSum = calculateChecksum((uint8_t *)&armPacket);
////  Serial.println(armPacket.mean);
////  Serial.println(armPacket.median);
////  Serial.println(armPacket.range);
////  Serial.println(armPacket.variance);
//
//  Serial.write((byte *)&armPacket, sizeof(armPacket));
//}

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
//    sendDummyData();
      if (dataReady) {
        sendArmData(current);
      }
  }

  void run() override
  {
//    if (Serial.read() == 'H') {
//        nextID = HANDSHAKE_STATE_ID;
//        handshakeDone = false;
//        current = ACCEL_X;
//    } else if (Serial.read() == 'A') {
//      if (current == ROTATE_Z) {
//        current = ACCEL_X;
//        dataReady = false;
//    } else {
//      current += 1;
//    }
////        Serial.println("got ack in data state");
//        nextID = SLEEP_STATE_ID;
//      }
//  }
    while (true) {
      delay(TIMEOUT_DATA);
//      if (current == ROTATE_Z) {
//        current = ACCEL_X;
//        dataReady = false;
//      } else {
//        current += 1;
//      }
//      if (Serial.read() == 'A') {
//        if (current == ROTATE_Z) {
//          current = ACCEL_X;
//          dataReady = false;
//        } else {
//          current += 1;
//        }
////        Serial.println("got ack in data state");
//        nextID = SLEEP_STATE_ID;
//        break;
//      } else if (Serial.read() == 'H') {
////        nextState = &Handshake_State;
//          nextID = HANDSHAKE_STATE_ID;
//          handshakeDone = false;
//          current = ACCEL_X;
//        break;
//      }
      if (Serial.read() == 'H') {
        nextID = HANDSHAKE_STATE_ID;
        handshakeDone = false;
        current = ACCEL_X;
        break;
      } else if (Serial.read() == 'A') {
        if (current == ROTATE_Z) {
          current = ACCEL_X;
          dataReady = false;
        } else {
          current += 1;
        }
        nextID = SLEEP_STATE_ID;
        break;
      }
      sendArmData(current);
//       sendDummyData();
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
      if (Serial.read() == 'H') {
//        nextState = &Handshake_State;
          nextID = HANDSHAKE_STATE_ID;
      } else if (handshakeDone && dataReady) {
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
//    nextState = &Sleep_State;
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
//  Serial.println("ready!");
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

    /* filtered values */
    //  accXFilter.Filter(accX);
    //  int filteredAccX = (int)accXFilter.Current();
    //  accYFilter.Filter(accY);
    //  int filteredAccY = (int)accYFilter.Current();
    //  accZFilter.Filter(accZ);
    //  int filteredAccZ = (int)accZFilter.Current();
    //  gyroXFilter.Filter(gyroX);
    //  int filteredGyroX = (int)gyroXFilter.Current();
    //  gyroYFilter.Filter(gyroY);
    //  int filteredGyroY = (int)gyroYFilter.Current();
    //  gyroZFilter.Filter(gyroZ);
    //  int filteredGyroZ = (int)gyroZFilter.Current();

    readings[ACCEL_X][i] = filteredAccX;
    readings[ACCEL_Y][i] = filteredAccY;
    readings[ACCEL_Z][i] = filteredAccZ;
    readings[ROTATE_X][i] = filteredGyroX;
    readings[ROTATE_Y][i] = filteredGyroY;
    readings[ROTATE_Z][i] = filteredGyroZ;

    if (i == NUM_READINGS - 1)
    {
      getStats(readings[ACCEL_X], stats[ACCEL_X]);
      getStats(readings[ACCEL_Y], stats[ACCEL_Y]);
      getStats(readings[ACCEL_Z], stats[ACCEL_Z]);
      getStats(readings[ROTATE_X], stats[ROTATE_X]);
      getStats(readings[ROTATE_Y], stats[ROTATE_Y]);
      getStats(readings[ROTATE_Z], stats[ROTATE_Z]);

      dataReady = true;
      
//      printStats(stats[ACCEL_X]);
//      printStats(stats[ACCEL_Y]);
//      printStats(stats[ACCEL_Z]);
//      printStats(stats[ROTATE_X]);
//      printStats(stats[ROTATE_Y]);
//      printStats(stats[ROTATE_Z]);

      i = 0;
    }
    else
    {
      i++;
    }
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
