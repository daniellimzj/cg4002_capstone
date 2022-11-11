fpga folder:
- contains the c++ code for the fpga portion
- my_ip_v1_0_HLS.cpp is the file we use to generate the neural network on the FPGA
- bias.h and weight.h are the header files that are used to store the bias and weights respectively. 
- test_my_ip_v1_0_HLS.cpp is the testbench file. 

model folder:
- mlp_sklearn.py is the file that is used to train the MLP neural network in software.
- data_processing.py is the file that is used to preprocess and feature extract from the raw data files, which generates main.csv.
- scaler.joblib is the file that is used to scale our extracted features.  
