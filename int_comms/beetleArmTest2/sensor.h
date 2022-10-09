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

#define SAMPLE_RATE 25                     // sample rate in Hz
#define SAMPLE_INTERVAL 1000 / SAMPLE_RATE // sample interval in ms
#define FILTER_WEIGHT 10                   // 0 to 100; the lower the value, more smoothed and slower the response

volatile boolean dataReady = false;

// getStats uses the values in arr to calculate the 4 things we need; mean, median, range, variance.
// It then stores these values into results.
void getStats(int16_t *arr, float *results)
{

  int16_t maxR = -32768;
  int16_t minR = 32767;

  for (int i = 0; i < NUM_READINGS; i++)
  {
    results[MEAN] += arr[i];
    if (arr[i] < minR)
    {
      minR = arr[i];
    }
    if (arr[i] > maxR)
    {
      maxR = arr[i];
    }
  }

  results[MEAN] /= NUM_READINGS;

  for (int i = 0; i < NUM_READINGS; i++)
  {
    results[VARIANCE] += (arr[i] - results[MEAN]) * (arr[i] - results[MEAN]);
  }

  results[VARIANCE] /= NUM_READINGS;

  results[RANGE] = (float)maxR - (float)minR;

  results[MEDIAN] = (float)QuickMedian<int16_t>::GetMedian(arr, sizeof(arr) / sizeof(int16_t));
}

void printStats(float *stats)
{
  Serial.print(stats[MEAN]);
  Serial.print(", ");
  Serial.print(stats[RANGE]);
  Serial.print(", ");
  Serial.print(stats[VARIANCE]);
  Serial.print(", ");
  Serial.print(stats[MEDIAN]);
  Serial.println("");
}
