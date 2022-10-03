#include <MegunoLink.h>
#include "Filter.h"

#include <I2Cdev.h>
#include <helper_3dmath.h>
#include <MPU6050.h>
#include <QuickMedianLib.h>

#include <stdio.h>
#include <stdlib.h>

#define NUM_READINGS 50
#define NUM_STATS 4
#define NUM_FEATURES 6

#define MEAN 0
#define MEDIAN 1
#define RANGE 2
#define VARIANCE 3

#define ACCEL_X 0
#define ACCEL_Y 1
#define ACCEL_Z 2
#define ROTATE_X 3
#define ROTATE_Y 4
#define ROTATE_Z 5

#define SAMPLE_RATE 25 //sample rate in Hz
#define SAMPLE_INTERVAL 1000 / SAMPLE_RATE // sample interval in ms
#define FILTER_WEIGHT 10 //0 to 100; the lower the value, more smoothed and slower the response

MPU6050 myIMU;

int16_t accX, accY, accZ, gyroX, gyroY, gyroZ;
int8_t filteredAccX, filteredAccY, filteredAccZ, filteredGyroX, filteredGyroY, filteredGyroZ;

int8_t readings[NUM_FEATURES][NUM_READINGS];
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

// getStats uses the values in arr to calculate the 4 things we need; mean, median, range, variance.
// It then stores these values into results.
void getStats(int8_t* arr, float* results) {

  int8_t maxR = -128;
  int8_t minR = 127;


  for (int i = 0; i < NUM_READINGS; i++) {
    results[MEAN] += arr[i];
    if (arr[i] < minR) {
      minR = arr[i];
    }
    if (arr[i] > maxR) {
      maxR = arr[i];
    }
  }

  results[MEAN] /= NUM_READINGS;

  for (int i = 0; i < NUM_READINGS; i++) {
    results[VARIANCE] += (arr[i] - results[MEAN]) * (arr[i] - results[MEAN]);
  }

  results[VARIANCE] /= NUM_READINGS;

  results[RANGE] = (float)maxR - (float)minR;

  results[MEDIAN] = (float)QuickMedian<int8_t>::GetMedian(arr, sizeof(arr) / sizeof(int8_t));

}

void printStats(float* stats) {
  Serial.print(stats[MEAN]);
  Serial.print(", ");
  Serial.print(stats[MEDIAN]);
  Serial.print(", ");
  Serial.print(stats[RANGE]);
  Serial.print(", ");
  Serial.print(stats[VARIANCE]);
  Serial.println("");
}

void setup() {
  Serial.begin(115200);

  myIMU.initialize(); //MPU6050 starts in sleep mode, need to wake it up to use it

  myIMU.setDLPFMode(6);

  if (myIMU.getRate() == 0) {
    myIMU.setRate((8000 / SAMPLE_RATE) - 1);
  } else {
    myIMU.setRate((1000 / SAMPLE_RATE) - 1);
  }
  //set initial value for filtered values
  myIMU.getMotion6(&accX, &accY, &accZ, &gyroX, &gyroY, &gyroZ); //take all measurements in same instant
  accXFilter.SetCurrent(accX);
  accYFilter.SetCurrent(accY);
  accZFilter.SetCurrent(accZ);
  gyroXFilter.SetCurrent(gyroX);
  gyroYFilter.SetCurrent(gyroY);
  gyroZFilter.SetCurrent(gyroZ);
  Serial.println("ready!");
}

void loop() {
  // put your main code here, to run repeatedly:

  currentMillis = millis();

  if (currentMillis - previousMillis >= SAMPLE_INTERVAL) {

    if (currentMillis - previousMillis > SAMPLE_INTERVAL){
      Serial.println("too long!");
    }

    previousMillis = currentMillis;

    myIMU.getMotion6(&accX, &accY, &accZ, &gyroX, &gyroY, &gyroZ); //take all measurements in same instant

    /* filtered values, reduce range to fit into int8_t*/
    accXFilter.Filter(accX);
    filteredAccX = (int8_t)(accXFilter.Current() / 256);
    accYFilter.Filter(accY);
    filteredAccY = (int8_t)(accYFilter.Current() / 256);
    accZFilter.Filter(accZ);
    filteredAccZ = (int8_t)(accZFilter.Current() / 256);
    gyroXFilter.Filter(gyroX);
    filteredGyroX = (int8_t)(gyroXFilter.Current() / 256);
    gyroYFilter.Filter(gyroY);
    filteredGyroY = (int8_t)(gyroYFilter.Current() / 256);
    gyroZFilter.Filter(gyroZ);
    filteredGyroZ = (int8_t)(gyroZFilter.Current() / 256);

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

    if (i == NUM_READINGS - 1) {
      unsigned long curr = millis();
      getStats(readings[ACCEL_X], stats[ACCEL_X]);
      getStats(readings[ACCEL_Y], stats[ACCEL_Y]);
      getStats(readings[ACCEL_Z], stats[ACCEL_Z]);
      getStats(readings[ROTATE_X], stats[ROTATE_X]);
      getStats(readings[ROTATE_Y], stats[ROTATE_Y]);
      getStats(readings[ROTATE_Z], stats[ROTATE_Z]);
      

      printStats(stats[ACCEL_X]);
      printStats(stats[ACCEL_Y]);
      printStats(stats[ACCEL_Z]);
      printStats(stats[ROTATE_X]);
      printStats(stats[ROTATE_Y]);
      printStats(stats[ROTATE_Z]);

      Serial.println(millis() - curr);
      i = 0;
    } else {
      i++;
    }
    
  }
}
