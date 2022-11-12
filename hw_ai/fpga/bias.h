#ifndef BIAS_H_
#define BIAS_H_

#define NUM_FEATURES 42
#define HIDDEN_LAYER1_SIZE 172
#define NUM_OUTPUT 5

float bias1[HIDDEN_LAYER1_SIZE] = {0.106582267908, -0.003847554491, 0.125658827860, 0.074900449210,
	       0.146626718609, -0.011235818904, 0.093056558828, -0.000237236928,
	       -0.096034681727, -0.155014980927, 0.161439965461, -0.106034911459,
	       -0.183478193381, 0.207056435628, 0.257889060944, 0.076251236629,
	       0.104959052573, -0.032073629274, 0.115994566177, -0.067348228830,
	       0.070289189858, 0.294273959618, -0.044163919507, -0.078725927293,
	       -0.083143332316, -0.094348685844, 0.185655239206, 0.158208491223,
	       0.159415288122, -0.003300039310, 0.123694266546, 0.139494294957,
	       0.125417712520, 0.120981172021, -0.094127094299, 0.129184901219,
	       0.060477398947, 0.115304626020, 0.146344290615, 0.159247684515,
	       0.094460757925, 0.155460437950, -0.046354039980, 0.059823745935,
	       0.015812208933, 0.197126317209, -0.129393933162, 0.188373369264,
	       0.283904296697, 0.153133942664, 0.135643415464, 0.046844878862,
	       -0.124266591294, 0.045922449178, 0.268191378962, -0.037930645242,
	       0.037331731825, 0.130784936475, 0.101769631520, -0.106583852322,
	       0.092345481706, 0.100228729957, 0.234099396757, 0.011521351239,
	       0.009335796816, 0.168184965962, -0.071954845539, -0.027904729299,
	       0.063108382123, 0.072534669247, -0.030959822342, 0.184330115942,
	       0.023852619038, 0.023045038461, -0.081917709701, -0.031745656577,
	       -0.006216880913, 0.192952411276, -0.020098061374, -0.032525965285,
	       -0.083759974693, 0.021969557314, 0.040511239487, -0.052391379091,
	       0.272131486696, -0.078651172800, -0.043071956686, 0.032837381738,
	       0.055977584730, 0.000519033187, 0.085193318875, 0.230471170236,
	       -0.027570212559, -0.174421593222, 0.114031729256, -0.154350422946,
	       0.238798772305, 0.055762557194, -0.186288886573, 0.035132104039,
	       -0.215188515761, 0.019511172970, -0.027657034052, -0.018199011576,
	       -0.050978555157, 0.050360803329, 0.041891049357, -0.048715614903,
	       0.227285682058, 0.011010928099, -0.061916135144, -0.062392842983,
	       0.214025748658, 0.135319228820, 0.172624437563, 0.084275133245,
	       -0.079410823358, 0.079082772512, 0.245755938294, 0.011924882373,
	       -0.090569884847, 0.096549776619, 0.080160793039, 0.131297282403,
	       0.162025246056, 0.214112916992, -0.079733243433, 0.083406814905,
	       -0.164063518504, -0.065145645082, -0.041592722186, -0.008243097935,
	       0.137989747234, 0.116183485938, 0.125411598336, 0.227330441480,
	       0.116286539905, 0.147808274570, 0.162474642052, 0.145350361090,
	       0.086746323102, 0.095518205496, 0.094160692628, -0.039791688727,
	       0.047417344281, 0.091886750997, 0.254037481070, 0.115886344288,
	       0.077174109644, 0.232548774715, -0.048521047797, -0.063776304807,
	       0.114176764817, -0.132484213112, -0.118078421536, 0.143441794149,
	       0.208301623450, 0.195624613932, 0.143032513718, 0.198680475976,
	       -0.023015961178, 0.082228069170, -0.175917475728, 0.163429027060,
	       -0.040363881398, -0.011835430322, 0.042649865939, -0.118193488034,
	       0.244776314136, 0.269700752078, -0.030211828113, 0.119798576870};

float bias2[NUM_OUTPUT] = {-0.143537305088, -0.023168009145, -0.029286629332, 0.159536676289,
	       -0.199234036172};

#endif