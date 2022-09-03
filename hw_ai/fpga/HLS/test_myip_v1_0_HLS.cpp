/*
----------------------------------------------------------------------------------
--	(c) Rajesh C Panicker, NUS,
--  Description : Self-checking testbench for AXI Stream Coprocessor (HLS) implementing the sum of 4 numbers
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

#include <stdio.h>
#include "hls_stream.h"

/***************** AXIS with TLAST structure declaration *********************/

struct AXIS_wLAST{
	float data;
	bool last;
};

/***************** Coprocessor function declaration *********************/

void myip_v1_0_HLS(hls::stream<AXIS_wLAST>& S_AXIS, hls::stream<AXIS_wLAST>& M_AXIS);

/***************** Macros *********************/
#define NUMBER_OF_INPUT_WORDS 36  // length of an input vector
#define NUMBER_OF_OUTPUT_WORDS 6  // length of an input vector
#define NUMBER_OF_TEST_VECTORS 1  // number of such test vectors (cases)


/************************** Variable Definitions *****************************/
//int test_input_memory [NUMBER_OF_TEST_VECTORS*NUMBER_OF_INPUT_WORDS] = {0x01, 0x02, 0x03, 0x04, 0x02, 0x03, 0x04, 0x05}; // 4 inputs * 2
//int test_result_expected_memory [NUMBER_OF_TEST_VECTORS*NUMBER_OF_OUTPUT_WORDS];// 4 outputs *2
float result_memory [NUMBER_OF_TEST_VECTORS*NUMBER_OF_OUTPUT_WORDS]; // same size as test_result_expected_memory
float test_yh[NUMBER_OF_INPUT_WORDS] = {1.51190225999999,1.175706,0.124010463087184,1.5646025,-1.15061442,0.431065999999999,0.0163457758017208,-1.216116,-2.51870439,6.280483,0.449042987558603,-2.52445849999999,0.06068828,5.779239,2.34714912650658,0.1856425,0.08336651,7.280324,2.10804922927687,0.255263999999999,0.0317874099999999,5.61297,1.75224167279753,0.0568874999999999,0.00878895999999998,2.84349199999999,0.22415354210618,0.008634,0.00956118,1.607578,0.154580156077724,-0.0812829999999999,-0.0371683499999999,1.667564,0.0984474759494217,-0.0843005};

/*****************************************************************************
* Main function
******************************************************************************/
int main()
{
	int word_cnt, test_case_cnt = 0;
	int success;
	AXIS_wLAST read_output, write_input;
	hls::stream<AXIS_wLAST> S_AXIS;
	hls::stream<AXIS_wLAST> M_AXIS;
//	main2();

	for (test_case_cnt=0 ; test_case_cnt < NUMBER_OF_TEST_VECTORS ; test_case_cnt++){


		/******************** Input to Coprocessor : Transmit the Data Stream ***********************/

		printf(" Transmitting Data for test case %d ... \r\n", test_case_cnt);

		for (word_cnt=0 ; word_cnt < NUMBER_OF_INPUT_WORDS ; word_cnt++){

//			write_input.data = test_input_memory[word_cnt+test_case_cnt*NUMBER_OF_INPUT_WORDS];
			write_input.data = test_yh[word_cnt+test_case_cnt*NUMBER_OF_INPUT_WORDS];
			write_input.last = 0;
			if(word_cnt==NUMBER_OF_INPUT_WORDS-1)
			{
				write_input.last = 1;
				// S_AXIS_TLAST is asserted for the last word.
				// Actually, doesn't matter since we are not making using of S_AXIS_TLAST.
			}
			S_AXIS.write(write_input); // insert one word into the stream
		}

		/* Transmission Complete */

		/********************* Call the hardware function (invoke the co-processor / ip) ***************/

		myip_v1_0_HLS(S_AXIS, M_AXIS);

		/******************** Output from Coprocessor : Receive the Data Stream ***********************/

		printf(" Receiving data for test case %d ... \r\n", test_case_cnt);

		for (word_cnt=0 ; word_cnt < NUMBER_OF_OUTPUT_WORDS ; word_cnt++){

			read_output = M_AXIS.read(); // extract one word from the stream
			result_memory[word_cnt+test_case_cnt*NUMBER_OF_OUTPUT_WORDS] = read_output.data;
		}

		/* Reception Complete */
	}

	/************************** Checking correctness of results *****************************/

	success = 1;

	/* Compare the data send with the data received */
//	printf(" Comparing data ...\r\n");
//	for(word_cnt=0; word_cnt < NUMBER_OF_TEST_VECTORS*NUMBER_OF_OUTPUT_WORDS; word_cnt++){
//		printf("%d\n", result_memory[word_cnt]);\
//		printf("%d\n", test_result_expected_memory[word_cnt]);
//		success = success & (result_memory[word_cnt] == test_result_expected_memory[word_cnt]);
//	}
//
//	if (success != 1){
//		printf("Test Failed\r\n");
//		return 1;
//	}
//
//	printf("Test Success\r\n");
	for (int i =0 ; i< NUMBER_OF_OUTPUT_WORDS; i++){
		printf("%f\n", result_memory[i]);
	}

	return 0;
}
