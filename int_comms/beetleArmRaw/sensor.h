#include <MegunoLink.h>
#include "Filter.h"

#include <I2Cdev.h>
#include <helper_3dmath.h>
#include <MPU6050.h>
#include <QuickMedianLib.h>

#include <stdio.h>
#include <stdlib.h>

#define ACCEL_X 0
#define ACCEL_Y 1
#define ACCEL_Z 2
#define ROTATE_X 3
#define ROTATE_Y 4
#define ROTATE_Z 5

#define SAMPLE_RATE 25                     // sample rate in Hz
#define SAMPLE_INTERVAL 1000 / SAMPLE_RATE // sample interval in ms
#define FILTER_WEIGHT 10                   // 0 to 100; the lower the value, more smoothed and slower the response
