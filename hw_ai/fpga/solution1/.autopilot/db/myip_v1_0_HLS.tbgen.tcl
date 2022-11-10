set moduleName myip_v1_0_HLS
set isTopModule 1
set isTaskLevelControl 1
set isCombinational 0
set isDatapathOnly 0
set isFreeRunPipelineModule 0
set isPipelined 0
set pipeline_type none
set FunctionProtocol ap_ctrl_none
set isOneStateSeq 0
set ProfileFlag 0
set StallSigGenFlag 0
set isEnableWaveformDebug 1
set C_modelName {myip_v1_0_HLS}
set C_modelType { void 0 }
set C_modelArgList {
	{ S_AXIS_V_data float 32 regular {axi_s 0 volatile  { S_AXIS Data } }  }
	{ S_AXIS_V_last int 1 regular {axi_s 0 volatile  { S_AXIS Last } }  }
	{ M_AXIS_V_data float 32 regular {axi_s 1 volatile  { M_AXIS Data } }  }
	{ M_AXIS_V_last int 1 regular {axi_s 1 volatile  { M_AXIS Last } }  }
}
set C_modelArgMapList {[ 
	{ "Name" : "S_AXIS_V_data", "interface" : "axis", "bitwidth" : 32, "direction" : "READONLY", "bitSlice":[{"low":0,"up":31,"cElement": [{"cName": "S_AXIS.V.data","cData": "float","bit_use": { "low": 0,"up": 31},"cArray": [{"low" : 0,"up" : 0,"step" : 1}]}]}]} , 
 	{ "Name" : "S_AXIS_V_last", "interface" : "axis", "bitwidth" : 1, "direction" : "READONLY", "bitSlice":[{"low":0,"up":0,"cElement": [{"cName": "S_AXIS.V.last","cData": "bool","bit_use": { "low": 0,"up": 0},"cArray": [{"low" : 0,"up" : 0,"step" : 1}]}]}]} , 
 	{ "Name" : "M_AXIS_V_data", "interface" : "axis", "bitwidth" : 32, "direction" : "WRITEONLY", "bitSlice":[{"low":0,"up":31,"cElement": [{"cName": "M_AXIS.V.data","cData": "float","bit_use": { "low": 0,"up": 31},"cArray": [{"low" : 0,"up" : 0,"step" : 1}]}]}]} , 
 	{ "Name" : "M_AXIS_V_last", "interface" : "axis", "bitwidth" : 1, "direction" : "WRITEONLY", "bitSlice":[{"low":0,"up":0,"cElement": [{"cName": "M_AXIS.V.last","cData": "bool","bit_use": { "low": 0,"up": 0},"cArray": [{"low" : 0,"up" : 0,"step" : 1}]}]}]} ]}
# RTL Port declarations: 
set portNum 10
set portList { 
	{ ap_clk sc_in sc_logic 1 clock -1 } 
	{ ap_rst_n sc_in sc_logic 1 reset -1 active_low_sync } 
	{ S_AXIS_TDATA sc_in sc_lv 32 signal 0 } 
	{ S_AXIS_TVALID sc_in sc_logic 1 invld 1 } 
	{ S_AXIS_TREADY sc_out sc_logic 1 inacc 1 } 
	{ S_AXIS_TLAST sc_in sc_logic 1 signal 1 } 
	{ M_AXIS_TDATA sc_out sc_lv 32 signal 2 } 
	{ M_AXIS_TVALID sc_out sc_logic 1 outvld 3 } 
	{ M_AXIS_TREADY sc_in sc_logic 1 outacc 3 } 
	{ M_AXIS_TLAST sc_out sc_logic 1 signal 3 } 
}
set NewPortList {[ 
	{ "name": "ap_clk", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "clock", "bundle":{"name": "ap_clk", "role": "default" }} , 
 	{ "name": "ap_rst_n", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "reset", "bundle":{"name": "ap_rst_n", "role": "default" }} , 
 	{ "name": "S_AXIS_TDATA", "direction": "in", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "S_AXIS_V_data", "role": "default" }} , 
 	{ "name": "S_AXIS_TVALID", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "invld", "bundle":{"name": "S_AXIS_V_last", "role": "default" }} , 
 	{ "name": "S_AXIS_TREADY", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "inacc", "bundle":{"name": "S_AXIS_V_last", "role": "default" }} , 
 	{ "name": "S_AXIS_TLAST", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "S_AXIS_V_last", "role": "default" }} , 
 	{ "name": "M_AXIS_TDATA", "direction": "out", "datatype": "sc_lv", "bitwidth":32, "type": "signal", "bundle":{"name": "M_AXIS_V_data", "role": "default" }} , 
 	{ "name": "M_AXIS_TVALID", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "outvld", "bundle":{"name": "M_AXIS_V_last", "role": "default" }} , 
 	{ "name": "M_AXIS_TREADY", "direction": "in", "datatype": "sc_logic", "bitwidth":1, "type": "outacc", "bundle":{"name": "M_AXIS_V_last", "role": "default" }} , 
 	{ "name": "M_AXIS_TLAST", "direction": "out", "datatype": "sc_logic", "bitwidth":1, "type": "signal", "bundle":{"name": "M_AXIS_V_last", "role": "default" }}  ]}

set RtlHierarchyInfo {[
	{"ID" : "0", "Level" : "0", "Path" : "`AUTOTB_DUT_INST", "Parent" : "", "Child" : ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65"],
		"CDFG" : "myip_v1_0_HLS",
		"Protocol" : "ap_ctrl_none",
		"ControlExist" : "0", "ap_start" : "0", "ap_ready" : "0", "ap_done" : "0", "ap_continue" : "0", "ap_idle" : "0",
		"Pipeline" : "None", "UnalignedPipeline" : "0", "RewindPipeline" : "0", "ProcessNetwork" : "0",
		"II" : "0",
		"VariableLatency" : "1", "ExactLatency" : "-1", "EstimateLatencyMin" : "25836", "EstimateLatencyMax" : "25836",
		"Combinational" : "0",
		"Datapath" : "0",
		"ClockEnable" : "0",
		"HasSubDataflow" : "0",
		"InDataflowNetwork" : "0",
		"HasNonBlockingOperation" : "0",
		"Port" : [
			{"Name" : "S_AXIS_V_data", "Type" : "Axis", "Direction" : "I",
				"BlockSignal" : [
					{"Name" : "S_AXIS_TDATA_blk_n", "Type" : "RtlSignal"}]},
			{"Name" : "S_AXIS_V_last", "Type" : "Axis", "Direction" : "I"},
			{"Name" : "M_AXIS_V_data", "Type" : "Axis", "Direction" : "O",
				"BlockSignal" : [
					{"Name" : "M_AXIS_TDATA_blk_n", "Type" : "RtlSignal"}]},
			{"Name" : "M_AXIS_V_last", "Type" : "Axis", "Direction" : "O"},
			{"Name" : "weights1_0", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_1", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_2", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_3", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_4", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_5", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_6", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_7", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_8", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_9", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_10", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_11", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_12", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_13", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_14", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_15", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_16", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_17", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_18", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_19", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_20", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_21", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_22", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_23", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_24", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_25", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_26", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_27", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_28", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_29", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_30", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_31", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_32", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_33", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_34", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_35", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_36", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_37", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_38", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_39", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_40", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights1_41", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "bias1", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "weights2", "Type" : "Memory", "Direction" : "I"},
			{"Name" : "bias2", "Type" : "Memory", "Direction" : "I"}]},
	{"ID" : "1", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_0_U", "Parent" : "0"},
	{"ID" : "2", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_1_U", "Parent" : "0"},
	{"ID" : "3", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_2_U", "Parent" : "0"},
	{"ID" : "4", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_3_U", "Parent" : "0"},
	{"ID" : "5", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_4_U", "Parent" : "0"},
	{"ID" : "6", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_5_U", "Parent" : "0"},
	{"ID" : "7", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_6_U", "Parent" : "0"},
	{"ID" : "8", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_7_U", "Parent" : "0"},
	{"ID" : "9", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_8_U", "Parent" : "0"},
	{"ID" : "10", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_9_U", "Parent" : "0"},
	{"ID" : "11", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_10_U", "Parent" : "0"},
	{"ID" : "12", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_11_U", "Parent" : "0"},
	{"ID" : "13", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_12_U", "Parent" : "0"},
	{"ID" : "14", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_13_U", "Parent" : "0"},
	{"ID" : "15", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_14_U", "Parent" : "0"},
	{"ID" : "16", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_15_U", "Parent" : "0"},
	{"ID" : "17", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_16_U", "Parent" : "0"},
	{"ID" : "18", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_17_U", "Parent" : "0"},
	{"ID" : "19", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_18_U", "Parent" : "0"},
	{"ID" : "20", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_19_U", "Parent" : "0"},
	{"ID" : "21", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_20_U", "Parent" : "0"},
	{"ID" : "22", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_21_U", "Parent" : "0"},
	{"ID" : "23", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_22_U", "Parent" : "0"},
	{"ID" : "24", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_23_U", "Parent" : "0"},
	{"ID" : "25", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_24_U", "Parent" : "0"},
	{"ID" : "26", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_25_U", "Parent" : "0"},
	{"ID" : "27", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_26_U", "Parent" : "0"},
	{"ID" : "28", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_27_U", "Parent" : "0"},
	{"ID" : "29", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_28_U", "Parent" : "0"},
	{"ID" : "30", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_29_U", "Parent" : "0"},
	{"ID" : "31", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_30_U", "Parent" : "0"},
	{"ID" : "32", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_31_U", "Parent" : "0"},
	{"ID" : "33", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_32_U", "Parent" : "0"},
	{"ID" : "34", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_33_U", "Parent" : "0"},
	{"ID" : "35", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_34_U", "Parent" : "0"},
	{"ID" : "36", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_35_U", "Parent" : "0"},
	{"ID" : "37", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_36_U", "Parent" : "0"},
	{"ID" : "38", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_37_U", "Parent" : "0"},
	{"ID" : "39", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_38_U", "Parent" : "0"},
	{"ID" : "40", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_39_U", "Parent" : "0"},
	{"ID" : "41", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_40_U", "Parent" : "0"},
	{"ID" : "42", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights1_41_U", "Parent" : "0"},
	{"ID" : "43", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.bias1_U", "Parent" : "0"},
	{"ID" : "44", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.weights2_U", "Parent" : "0"},
	{"ID" : "45", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.bias2_U", "Parent" : "0"},
	{"ID" : "46", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.v_U", "Parent" : "0"},
	{"ID" : "47", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.v2_U", "Parent" : "0"},
	{"ID" : "48", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.input_U", "Parent" : "0"},
	{"ID" : "49", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fadShg_U1", "Parent" : "0"},
	{"ID" : "50", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fmuThq_U2", "Parent" : "0"},
	{"ID" : "51", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fmuThq_U3", "Parent" : "0"},
	{"ID" : "52", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fmuThq_U4", "Parent" : "0"},
	{"ID" : "53", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fmuThq_U5", "Parent" : "0"},
	{"ID" : "54", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fmuThq_U6", "Parent" : "0"},
	{"ID" : "55", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fmuThq_U7", "Parent" : "0"},
	{"ID" : "56", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fmuThq_U8", "Parent" : "0"},
	{"ID" : "57", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fmuThq_U9", "Parent" : "0"},
	{"ID" : "58", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fmuThq_U10", "Parent" : "0"},
	{"ID" : "59", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fmuThq_U11", "Parent" : "0"},
	{"ID" : "60", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fmuThq_U12", "Parent" : "0"},
	{"ID" : "61", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.myip_v1_0_HLS_fcmUhA_U13", "Parent" : "0"},
	{"ID" : "62", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.regslice_both_S_AXIS_V_data_U", "Parent" : "0"},
	{"ID" : "63", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.regslice_both_w1_S_AXIS_V_last_U", "Parent" : "0"},
	{"ID" : "64", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.regslice_both_M_AXIS_V_data_U", "Parent" : "0"},
	{"ID" : "65", "Level" : "1", "Path" : "`AUTOTB_DUT_INST.regslice_both_w1_M_AXIS_V_last_U", "Parent" : "0"}]}


set ArgLastReadFirstWriteLatency {
	myip_v1_0_HLS {
		S_AXIS_V_data {Type I LastRead 1 FirstWrite -1}
		S_AXIS_V_last {Type I LastRead 1 FirstWrite -1}
		M_AXIS_V_data {Type O LastRead -1 FirstWrite 112}
		M_AXIS_V_last {Type O LastRead -1 FirstWrite 112}
		weights1_0 {Type I LastRead -1 FirstWrite -1}
		weights1_1 {Type I LastRead -1 FirstWrite -1}
		weights1_2 {Type I LastRead -1 FirstWrite -1}
		weights1_3 {Type I LastRead -1 FirstWrite -1}
		weights1_4 {Type I LastRead -1 FirstWrite -1}
		weights1_5 {Type I LastRead -1 FirstWrite -1}
		weights1_6 {Type I LastRead -1 FirstWrite -1}
		weights1_7 {Type I LastRead -1 FirstWrite -1}
		weights1_8 {Type I LastRead -1 FirstWrite -1}
		weights1_9 {Type I LastRead -1 FirstWrite -1}
		weights1_10 {Type I LastRead -1 FirstWrite -1}
		weights1_11 {Type I LastRead -1 FirstWrite -1}
		weights1_12 {Type I LastRead -1 FirstWrite -1}
		weights1_13 {Type I LastRead -1 FirstWrite -1}
		weights1_14 {Type I LastRead -1 FirstWrite -1}
		weights1_15 {Type I LastRead -1 FirstWrite -1}
		weights1_16 {Type I LastRead -1 FirstWrite -1}
		weights1_17 {Type I LastRead -1 FirstWrite -1}
		weights1_18 {Type I LastRead -1 FirstWrite -1}
		weights1_19 {Type I LastRead -1 FirstWrite -1}
		weights1_20 {Type I LastRead -1 FirstWrite -1}
		weights1_21 {Type I LastRead -1 FirstWrite -1}
		weights1_22 {Type I LastRead -1 FirstWrite -1}
		weights1_23 {Type I LastRead -1 FirstWrite -1}
		weights1_24 {Type I LastRead -1 FirstWrite -1}
		weights1_25 {Type I LastRead -1 FirstWrite -1}
		weights1_26 {Type I LastRead -1 FirstWrite -1}
		weights1_27 {Type I LastRead -1 FirstWrite -1}
		weights1_28 {Type I LastRead -1 FirstWrite -1}
		weights1_29 {Type I LastRead -1 FirstWrite -1}
		weights1_30 {Type I LastRead -1 FirstWrite -1}
		weights1_31 {Type I LastRead -1 FirstWrite -1}
		weights1_32 {Type I LastRead -1 FirstWrite -1}
		weights1_33 {Type I LastRead -1 FirstWrite -1}
		weights1_34 {Type I LastRead -1 FirstWrite -1}
		weights1_35 {Type I LastRead -1 FirstWrite -1}
		weights1_36 {Type I LastRead -1 FirstWrite -1}
		weights1_37 {Type I LastRead -1 FirstWrite -1}
		weights1_38 {Type I LastRead -1 FirstWrite -1}
		weights1_39 {Type I LastRead -1 FirstWrite -1}
		weights1_40 {Type I LastRead -1 FirstWrite -1}
		weights1_41 {Type I LastRead -1 FirstWrite -1}
		bias1 {Type I LastRead -1 FirstWrite -1}
		weights2 {Type I LastRead -1 FirstWrite -1}
		bias2 {Type I LastRead -1 FirstWrite -1}}}

set hasDtUnsupportedChannel 0

set PerformanceInfo {[
	{"Name" : "Latency", "Min" : "25836", "Max" : "25836"}
	, {"Name" : "Interval", "Min" : "25837", "Max" : "25837"}
]}

set PipelineEnableSignalInfo {[
]}

set Spec2ImplPortList { 
	S_AXIS_V_data { axis {  { S_AXIS_TDATA in_data 0 32 } } }
	S_AXIS_V_last { axis {  { S_AXIS_TVALID in_vld 0 1 }  { S_AXIS_TREADY in_acc 1 1 }  { S_AXIS_TLAST in_data 0 1 } } }
	M_AXIS_V_data { axis {  { M_AXIS_TDATA out_data 1 32 } } }
	M_AXIS_V_last { axis {  { M_AXIS_TVALID out_vld 1 1 }  { M_AXIS_TREADY out_acc 0 1 }  { M_AXIS_TLAST out_data 1 1 } } }
}

set busDeadlockParameterList { 
}

# RTL port scheduling information:
set fifoSchedulingInfoList { 
}

# RTL bus port read request latency information:
set busReadReqLatencyList { 
}

# RTL bus port write response latency information:
set busWriteResLatencyList { 
}

# RTL array port load latency information:
set memoryLoadLatencyList { 
}
