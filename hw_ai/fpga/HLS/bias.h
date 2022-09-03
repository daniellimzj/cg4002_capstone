#ifndef BIAS_H_
#define BIAS_H_

#define NUM_FEATURES 36
#define HIDDEN_LAYER1_SIZE 5
#define NUM_OUTPUT 6

float bias1[HIDDEN_LAYER1_SIZE] = {
		-1.650204647574, 0.113251805025, 1.606062586265, 1.158742765899,
		       -2.931719489912};


float bias2[NUM_OUTPUT] = {-0.677513635279, -0.180616010174, -0.559465318045, -0.482801205545,
	       -1.014485715112, -0.090735693150};

#endif
