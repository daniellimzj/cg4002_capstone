/*
----------------------------------------------------------------------------------
--	(c) Rajesh C Panicker, NUS,
--  Description : AXI Stream Coprocessor (HLS), implementing the sum of 4 numbers
--	License terms :
--	You are free to use this code as long as you
--		(i) DO NOT post a modified version of this on any public repository;
--		(ii) use it only for educational purposes;
--		(iii) accept the responsibility to ensure that your implementation does not violate any intellectual property of any entity.
--		(iv) accept that the program is provided "as is" without warranty of any kind or assurance regarding its suitability for any particular purpose;
--		(v) send an email to rajesh.panicker@ieee.org briefly mentioning its use (except when used for the course EE4218 at the National University of Singapore);
--		(vi) retain this notice in this file or any files derived from this.
----------------------------------------------------------------------------------
*/

//#include "ap_axi_sdata.h" // ap_axis can also be used, but it will include all sideband signals which we don't need
#include "hls_stream.h"
#include "hls_math.h"
#include "ap_int.h"
#include "bias.h"
#include "weight.h"


struct AXIS_wLAST{
	float data;
	bool last;
};


void myip_v1_0_HLS(hls::stream<AXIS_wLAST>& S_AXIS, hls::stream<AXIS_wLAST>& M_AXIS){
#pragma HLS INTERFACE ap_ctrl_none port=return
#pragma HLS INTERFACE axis port=S_AXIS
#pragma HLS INTERFACE axis port=M_AXIS

	int word_cnt;
	float v[HIDDEN_LAYER1_SIZE];
	float v2[NUM_OUTPUT];
	float input[NUM_FEATURES];
	float sum = 0;
	float sum2 = 0;
	float sum3 = 0;
	AXIS_wLAST read_input, write_output;


		myip_v1_0_HLS_for1:for(word_cnt = 0; word_cnt < NUM_FEATURES; word_cnt++){
			read_input = S_AXIS.read();
			input[word_cnt] = read_input.data; //extracting that word
		}

		// for each neuron, hidden layer 1
		myip_v1_0_HLS_for2:for(word_cnt = 0; word_cnt < HIDDEN_LAYER1_SIZE; word_cnt++){
			sum = 0;
			myip_v1_0_HLS_label1:for (int i = 0; i < NUM_FEATURES; i++) {
				sum += weights1[i][word_cnt] * input[i] ;
			}

			sum += bias1[word_cnt];
			if (sum > 0){
				v[word_cnt] = sum;
			}
			else {
				v[word_cnt] = 0;
			}
		}

		// output layer
		myip_v1_0_HLS_for3:for(word_cnt = 0; word_cnt < NUM_OUTPUT; word_cnt++){
			sum2 = 0;
			myip_v1_0_HLS_label2:for (int x = 0; x < HIDDEN_LAYER1_SIZE; x++) {
				sum2 += weights2[x][word_cnt] * v[x];
			}
			sum2 += bias2[word_cnt];
			if (sum2 > 0) {
				v2[word_cnt] = sum2;
			}
			else {
				v2[word_cnt] = 0;
			}
		}


		myip_v1_0_HLS_for5:for(word_cnt = 0; word_cnt < NUM_OUTPUT; word_cnt++){
			//write_output.data = sum.to_int();	// using arbitrary precision
			write_output.data = v2[word_cnt];
			// write_output is the element sent by our ip through M_AXIS in one clock cycle.
			write_output.last = 0;
			if(word_cnt==NUM_OUTPUT-1)
			{
				write_output.last = 1;
				// M_AXIS_TLAST is required to be asserted for the last word.
				// Else, the AXI Stream FIFO / AXI DMA will not know if all the words have been received from the co-processor.
			}
			M_AXIS.write(write_output);
			// write() inserts it into the stream. Overloaded operator << can also be used.
		}
}
