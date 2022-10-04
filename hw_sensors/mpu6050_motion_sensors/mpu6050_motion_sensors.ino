// Megunolink library used to filter values
// https://github.com/Megunolink/MLP
// https://www.megunolink.com/documentation/arduino-library/
#include <MegunoLink.h>
#include "Filter.h"
//#include <CommandHandler.h>
//#include <ArduinoTimer.h>

#include <I2Cdev.h> //https://github.com/jrowberg/i2cdevlib
#include <helper_3dmath.h>
#include <MPU6050.h>
//#include <MPU6050_6Axis_MotionApps20.h>
//#include <MPU6050_6Axis_MotionApps612.h>
//#include <MPU6050_9Axis_MotionApps41.h>

#define SAMPLE_RATE 50 //sample rate in Hz
#define FILTER_WEIGHT 10 //0 to 100; the lower the value, more smoothed and slower the response

MPU6050 myIMU;

// the <float> makes a filter for float numbers, <long> for long numbers
// 20 is the weight (20 => 20%)
// 0 is the initial value of the filter
// https://www.megunolink.com/articles/coding/3-methods-filter-noisy-arduino-measurements/
ExponentialFilter<long> accXFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> accYFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> accZFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> gyroXFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> gyroYFilter(FILTER_WEIGHT, 0);
ExponentialFilter<long> gyroZFilter(FILTER_WEIGHT, 0);

int16_t accX, accY, accZ, gyroX, gyroY, gyroZ;
//int meanAccX, meanAccY, meanAccZ, meanGyroX, meanGyroY, meanGyroZ;
//int medianAccX, medianAccY, medianAccZ, medianGyroX, medianGyroY, medianGyroZ;
//int rangeAccX, rangeAccY, rangeAccZ, rangeGyroX, rangeGyroY, rangeGyroZ;
//int varianceAccX, varianceAccY, varianceAccZ, varianceGyroX, varianceGyroY, varianceGyroZ;
//int accXReadings[50], accYReadings[50], accZReadings[50]; //based on raw or filtered values?
//int gyroXReadings[50], gyroYReadings[50], gyroZReadings[50]; 

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
//  if (myIMU.testConnection()) {
//    Serial.println("Connection with MPU6050 established.");
//  } else {
//    Serial.println("Failed to connect to MPU6050.");
//  }
  
  myIMU.initialize(); //MPU6050 starts in sleep mode, need to wake it up to use it
  
  /* Digital low pass filter modes:
   *          |   ACCELEROMETER    |           GYROSCOPE
   * DLPF_CFG | Bandwidth | Delay  | Bandwidth | Delay  | Sample Rate
   * ---------+-----------+--------+-----------+--------+-------------
   * 0        | 260Hz     | 0ms    | 256Hz     | 0.98ms | 8kHz
   * 1        | 184Hz     | 2.0ms  | 188Hz     | 1.9ms  | 1kHz
   * 2        | 94Hz      | 3.0ms  | 98Hz      | 2.8ms  | 1kHz
   * 3        | 44Hz      | 4.9ms  | 42Hz      | 4.8ms  | 1kHz
   * 4        | 21Hz      | 8.5ms  | 20Hz      | 8.3ms  | 1kHz
   * 5        | 10Hz      | 13.8ms | 10Hz      | 13.4ms | 1kHz
   * 6        | 5Hz       | 19.0ms | 5Hz       | 18.6ms | 1kHz
   * 7        |   -- Reserved --   |   -- Reserved --   | Reserved
   * 
   * Source: i2cdevlib.com/docs/html/class_m_p_u6050.html
   */
  myIMU.setDLPFMode(6);
//  Serial.print("Digital Low Pass Filter mode: ");
//  Serial.println(myIMU.getDLPFMode());

  /* Digital high pass filter modes:
   * ACCEL_HPF | Filter Mode | Cut-off Frequency
   * ----------+-------------+------------------
   * 0         | Reset       | None
   * 1         | On          | 5Hz
   * 2         | On          | 2.5Hz
   * 3         | On          | 1.25Hz
   * 4         | On          | 0.63Hz
   * 7         | Hold        | None
   * 
   * Source: i2cdevlib.com/docs/html/class_m_p_u6050.html
   */
//  Serial.print("Digital High Pass Filter mode: ");
//  Serial.println(myIMU.getDHPFMode());

  /*
   * Sample Rate = Gyroscope Output Rate / (1 + SMPLRT_DIV)
   * where Gyroscope Output Rate = 8kHz when the DLPF is disabled (DLPF_CFG = 0 or 7), and 1kHz when the DLPF is enabled (see Register 26).
   * 
   * Source: i2cdevlib.com/docs/html/class_m_p_u6050.html
   */
  if (myIMU.getRate() == 0) {
    myIMU.setRate((8000 / SAMPLE_RATE) - 1);
  } else {
    myIMU.setRate((1000 / SAMPLE_RATE) - 1);
  }
//  Serial.print("Sample rate: ");
//  Serial.println(SAMPLE_RATE);
//  Serial.print("Sample rate divider: ");
//  Serial.println(myIMU.getRate());
  
//  Serial.println();

//  delay(2000);

  //set initial value for filtered values
  myIMU.getMotion6(&accX, &accY, &accZ, &gyroX, &gyroY, &gyroZ); //take all measurements in same instant
  accXFilter.SetCurrent(accX);
  accYFilter.SetCurrent(accY);
  accZFilter.SetCurrent(accZ);
  gyroXFilter.SetCurrent(gyroX);
  gyroYFilter.SetCurrent(gyroY);
  gyroZFilter.SetCurrent(gyroZ);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  myIMU.getMotion6(&accX, &accY, &accZ, &gyroX, &gyroY, &gyroZ); //take all measurements in same instant

  /* filtered values, reduce range to fit into int8_t*/
//  accXFilter.Filter(accX);
//  int8_t filteredAccX = (int8_t)(accXFilter.Current()/256);
//  accYFilter.Filter(accY);
//  int8_t filteredAccY = (int8_t)(accYFilter.Current()/256);
//  accZFilter.Filter(accZ);
//  int8_t filteredAccZ = (int8_t)(accZFilter.Current()/256);
//  gyroXFilter.Filter(gyroX);
//  int8_t filteredGyroX = (int8_t)(gyroXFilter.Current()/256);
//  gyroYFilter.Filter(gyroY);
//  int8_t filteredGyroY = (int8_t)(gyroYFilter.Current()/256);
//  gyroZFilter.Filter(gyroZ);
//  int8_t filteredGyroZ = (int8_t)(gyroZFilter.Current()/256);

  /* filtered values */
  accXFilter.Filter(accX);
  int filteredAccX = (int)accXFilter.Current();
  accYFilter.Filter(accY);
  int filteredAccY = (int)accYFilter.Current();
  accZFilter.Filter(accZ);
  int filteredAccZ = (int)accZFilter.Current();
  gyroXFilter.Filter(gyroX);
  int filteredGyroX = (int)gyroXFilter.Current();
  gyroYFilter.Filter(gyroY);
  int filteredGyroY = (int)gyroYFilter.Current();
  gyroZFilter.Filter(gyroZ);
  int filteredGyroZ = (int)gyroZFilter.Current();
  
  Serial.print("FilteredAccX:");
  Serial.print(filteredAccX);
  Serial.print(", ");
  Serial.print("FilteredAccY:");
  Serial.print(filteredAccY);
  Serial.print(", ");
  Serial.print("FilteredAccZ:");
  Serial.print(filteredAccZ);
  Serial.print(", ");
  Serial.print("FilteredGyroX:");
  Serial.print(filteredGyroX);
  Serial.print(", ");
  Serial.print("FilteredGyroY:");
  Serial.print(filteredGyroY);
  Serial.print(", ");
  Serial.print("FilteredGyroZ:");
  Serial.print(filteredGyroZ);
  Serial.println("");
  
  delay(1000 / SAMPLE_RATE);
}
