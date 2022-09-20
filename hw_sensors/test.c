#include <stdio.h>
#include <stdlib.h>

#define NUM_READINGS 10
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

int compare (const void * a, const void * b)
{
    float fa = *(const float*) a;
    float fb = *(const float*) b;
    return (fa > fb) - (fa < fb);
}

float* getStats(float* arr, float* results) {
    
    float sum = 0, maxReading = -10000000, minReading = 10000000;

    for (int i = 0; i < NUM_READINGS; i++) {
        sum += arr[i];
        if (maxReading < arr[i]) {
        maxReading = arr[i];
        }
        if (minReading > arr[i]) {
        minReading = arr[i]; 
        }
    }

    results[RANGE] = maxReading - minReading;
    results[MEAN] = sum / NUM_READINGS;

    for (int i = 0; i < NUM_READINGS; i++) {
        results[VARIANCE] += (arr[i] - results[MEAN]) * (arr[i] - results[MEAN]);
    }

    results[VARIANCE] = results[VARIANCE] / NUM_READINGS;

    qsort(arr, NUM_READINGS, sizeof(float), compare);

    if (NUM_READINGS % 2 == 0) {
        results[MEDIAN] = (arr[NUM_READINGS / 2] + arr[NUM_READINGS / 2 - 1]) / 2.0 ;
    }
    else {
        results[MEDIAN] = arr[NUM_READINGS / 2 + 1];
    }

    return results;
}

void printStats(float* stats) {
    printf("Mean is %.2f\n", stats[MEAN]);
    printf("Median is %.2f\n", stats[MEDIAN]);
    printf("Variance is %.2f\n", stats[VARIANCE]);
    printf("Range is %.2f\n\n", stats[RANGE]);
}

int main() {

    float readings[NUM_FEATURES][NUM_READINGS];
    float stats[NUM_FEATURES][NUM_STATS];

    for (int i = 0; i < NUM_FEATURES; i++) {
        for (int j = 0; j < NUM_READINGS; j++) {
            readings[i][j] = (i + 1) * (j + 1);
        }
    }

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

    return 0;
}
