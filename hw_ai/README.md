# Hardware AI

## FPGA folder:
- my_ip_v1_0_HLS.cpp is the file that describes the neural network on the FPGA
- bias.h and weight.h are the header files that are used to store the bias and weights respectively. 
- test_my_ip_v1_0_HLS.cpp is the testbench file. 

## Model folder:
- mlp_sklearn.py is the file that is used to train the MLP neural network in software.
- data_processing.py is the file that is used to preprocess and feature extract from the raw data files, which generates main.csv.
- scaler.joblib is the file that is used to scale our extracted features; it can be exported to be used on the main script.
