// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __myip_v1_0_HLS_weimb6_H__
#define __myip_v1_0_HLS_weimb6_H__


#include <systemc>
using namespace sc_core;
using namespace sc_dt;




#include <iostream>
#include <fstream>

struct myip_v1_0_HLS_weimb6_ram : public sc_core::sc_module {

  static const unsigned DataWidth = 32;
  static const unsigned AddressRange = 172;
  static const unsigned AddressWidth = 8;

//latency = 1
//input_reg = 1
//output_reg = 0
sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in <sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


sc_lv<DataWidth> ram[AddressRange];


   SC_CTOR(myip_v1_0_HLS_weimb6_ram) {
        ram[0] = "0b10111101111110010011111011101000";
        ram[1] = "0b00111101101110101011110111111011";
        ram[2] = "0b10111100100100011000010000011010";
        ram[3] = "0b10111100110010001100100101010011";
        ram[4] = "0b00111110001000110110010010011100";
        ram[5] = "0b10111100010101000011011011110111";
        ram[6] = "0b00111100100110110010100010100110";
        ram[7] = "0b00111110010101001010000000010001";
        ram[8] = "0b10111101011101110001001101101001";
        ram[9] = "0b00111101101010100110001111100010";
        ram[10] = "0b10111101111101001010001101000011";
        ram[11] = "0b10111110010001000111000100110111";
        ram[12] = "0b00111101101011011100100000001010";
        ram[13] = "0b10111110100010011010000000010000";
        ram[14] = "0b00111101100010001011001100001111";
        ram[15] = "0b10111101010101001110101100001011";
        ram[16] = "0b00111101011100010001101101011101";
        ram[17] = "0b00111110001000110010001110001010";
        ram[18] = "0b10111100010100001100001101100110";
        ram[19] = "0b10111101101001011000101101100001";
        ram[20] = "0b00111101101011001011011111100001";
        ram[21] = "0b10111101110010000111100111100000";
        ram[22] = "0b10111110001110010011100000100111";
        ram[23] = "0b00111101100010110000000000011111";
        ram[24] = "0b00111100100001010001010011010100";
        ram[25] = "0b00111100111101011001100111110000";
        ram[26] = "0b00111100111000011110010001001111";
        ram[27] = "0b10111110000110110110111000010011";
        ram[28] = "0b10111101100101011010001001110100";
        ram[29] = "0b00111101011000100010000011010100";
        ram[30] = "0b00111101111110101010010010100101";
        ram[31] = "0b10111100111001111101011000110101";
        ram[32] = "0b10111101001010010010111110010101";
        ram[33] = "0b10111101101111110011000111100101";
        ram[34] = "0b00111101101001000101100110100111";
        ram[35] = "0b10111101110001000010110010101110";
        ram[36] = "0b10111101100000101011010110110000";
        ram[37] = "0b00111101100111010111110100110011";
        ram[38] = "0b00111110010100010101001101100101";
        ram[39] = "0b00111100101111100100001010110001";
        ram[40] = "0b00111100111000010110010101000011";
        ram[41] = "0b10111100101000101011101000110011";
        ram[42] = "0b00111110001010001010100110011011";
        ram[43] = "0b00111101000011001110010111011101";
        ram[44] = "0b00111101100100111111000111101011";
        ram[45] = "0b00111101111011000011000101110100";
        ram[46] = "0b10111101111111101011001001101111";
        ram[47] = "0b00111101101110101000111110001111";
        ram[48] = "0b10111110000001111111111001001100";
        ram[49] = "0b00111100001011110010011110010111";
        ram[50] = "0b10111101101100000110111101101101";
        ram[51] = "0b10111110010011000001100001011000";
        ram[52] = "0b10111100000111100000010111000101";
        ram[53] = "0b10111101101011101101010011111000";
        ram[54] = "0b00111101101011010010111100000010";
        ram[55] = "0b00111101101100101010000001101111";
        ram[56] = "0b10111101111010010111001100001110";
        ram[57] = "0b00111001000011001001111010011001";
        ram[58] = "0b00111101000001010111111101100011";
        ram[59] = "0b00111101101011100101101010000001";
        ram[60] = "0b10111100010111100000001111101110";
        ram[61] = "0b00111011000100101100000000001000";
        ram[62] = "0b10111110011110101101011001111100";
        ram[63] = "0b10111101111101100000110010010100";
        ram[64] = "0b10111110001100000010000001111010";
        ram[65] = "0b10111101000100000100010011100111";
        ram[66] = "0b10111101000010111001100110111000";
        ram[67] = "0b10111101110001011001010011000111";
        ram[68] = "0b00111101101011000111011010001100";
        ram[69] = "0b10111001110011011001011110001010";
        ram[70] = "0b10111101101111010000110111101101";
        ram[71] = "0b00111101010011110001010110111001";
        ram[72] = "0b10111110001011101101110101010110";
        ram[73] = "0b10111110001010011000010001110100";
        ram[74] = "0b10111101110000100101110110100110";
        ram[75] = "0b10111101100011110111110001101111";
        ram[76] = "0b10111101000110111111010111001101";
        ram[77] = "0b00111101011001010011010011100100";
        ram[78] = "0b10111100011010000110100111101001";
        ram[79] = "0b10111110000010011010010010111011";
        ram[80] = "0b00111110011111100011000111101111";
        ram[81] = "0b00111101011001111100010111111000";
        ram[82] = "0b10111110100010000010000011110110";
        ram[83] = "0b00111101011001011010101001100011";
        ram[84] = "0b00111101011101100101100010000010";
        ram[85] = "0b00111110001011011001001111110011";
        ram[86] = "0b10111110000001010101001110011100";
        ram[87] = "0b10111101101101111100110011001010";
        ram[88] = "0b10111100100101001001100110010100";
        ram[89] = "0b10111101100000001000111101110010";
        ram[90] = "0b10111101100001111010110011000011";
        ram[91] = "0b00111101001101000011001101001000";
        ram[92] = "0b10111110100011110101011010101010";
        ram[93] = "0b10111110011010110001011010010100";
        ram[94] = "0b10111101101001010000100111010010";
        ram[95] = "0b00111110010010111001011111000001";
        ram[96] = "0b10111110000111011101001001100001";
        ram[97] = "0b10111100001110100100100010111101";
        ram[98] = "0b10111110001100100011000101111101";
        ram[99] = "0b00111101100011000001110110110010";
        ram[100] = "0b10111011100100000000001111000100";
        ram[101] = "0b10111101010111101000011001010111";
        ram[102] = "0b00111110010010110010000000110101";
        ram[103] = "0b00111101000000001111100001101111";
        ram[104] = "0b10111100100101010011011101011001";
        ram[105] = "0b00111101111101001010011011011000";
        ram[106] = "0b10111110000011111110001001000110";
        ram[107] = "0b00111110000001101001001001110011";
        ram[108] = "0b00111101001000101110000001010001";
        ram[109] = "0b00111110001001010110101011010001";
        ram[110] = "0b10111110001010001110100010011010";
        ram[111] = "0b10111100101110000111111000111110";
        ram[112] = "0b00111101000100110111111110000101";
        ram[113] = "0b00111100110101001000110000111101";
        ram[114] = "0b10111100001010010011101100010000";
        ram[115] = "0b10111101110100011000001111001110";
        ram[116] = "0b10111101000111110100101011101110";
        ram[117] = "0b10111110000001000111110101110001";
        ram[118] = "0b00111110010111011100001101000100";
        ram[119] = "0b10111101111110101111000100011010";
        ram[120] = "0b00111101101100011000010101110011";
        ram[121] = "0b10111110000101110011101111111011";
        ram[122] = "0b10111100101100100011111111101000";
        ram[123] = "0b10111101110001011110000010110000";
        ram[124] = "0b00111101101100001111001011101101";
        ram[125] = "0b10111110011101001100001111010011";
        ram[126] = "0b10111110010110101101010011011010";
        ram[127] = "0b00111100000000000000001110011000";
        ram[128] = "0b00111101001100011110001101110100";
        ram[129] = "0b00111100110111110110100111110111";
        ram[130] = "0b10111110000110010101010100100011";
        ram[131] = "0b00111101011110000111001101100111";
        ram[132] = "0b10111101111011000101110010010001";
        ram[133] = "0b10111101110110100000110101111101";
        ram[134] = "0b00111110001010111010000000111100";
        ram[135] = "0b10111101001110011100011101001001";
        ram[136] = "0b10111101100001000100101110000011";
        ram[137] = "0b10111101110000011101111110110010";
        ram[138] = "0b00111100100110100010001110111111";
        ram[139] = "0b00111110011011100110011100010110";
        ram[140] = "0b10111101101110100011001000000101";
        ram[141] = "0b10111110000100111011100011101011";
        ram[142] = "0b00111110000011011000010110001000";
        ram[143] = "0b00111110001110101000011101001101";
        ram[144] = "0b10111110010011110001100010101011";
        ram[145] = "0b00111101111000101010000111000000";
        ram[146] = "0b00111110001101111111111000111011";
        ram[147] = "0b00111110000010011111000111110010";
        ram[148] = "0b00111110000010010101100100101010";
        ram[149] = "0b10111101010100111011100100111111";
        ram[150] = "0b00111101110101101011101001010111";
        ram[151] = "0b00111100100110111010011001010001";
        ram[152] = "0b10111101110110101010010101101011";
        ram[153] = "0b10111101111110100000000011001000";
        ram[154] = "0b00111110100001001111100000111010";
        ram[155] = "0b10111101011111000100000010010111";
        ram[156] = "0b10111110010001111101010000111000";
        ram[157] = "0b00111101010000100101101000010011";
        ram[158] = "0b10111110001001001111101010011101";
        ram[159] = "0b00111101101100001001010101010010";
        ram[160] = "0b10111110001100100010100010111111";
        ram[161] = "0b00111101110011110011110101010110";
        ram[162] = "0b10111101001011111000001110110000";
        ram[163] = "0b10111101111010111001000111111101";
        ram[164] = "0b00111101011101110010100100110100";
        ram[165] = "0b00111101101110111111110001000001";
        ram[166] = "0b10111110001100001111110111111001";
        ram[167] = "0b00111101010111110000110100100001";
        ram[168] = "0b10111110001110011111010110000001";
        ram[169] = "0b00111110000000111001110000010110";
        ram[170] = "0b10111110110011100110011111010001";
        ram[171] = "0b10111101100011011010001110001101";


SC_METHOD(prc_write_0);
  sensitive<<clk.pos();
   }


void prc_write_0()
{
    if (ce0.read() == sc_dt::Log_1) 
    {
            if(address0.read().is_01() && address0.read().to_uint()<AddressRange)
              q0 = ram[address0.read().to_uint()];
            else
              q0 = sc_lv<DataWidth>();
    }
}


}; //endmodule


SC_MODULE(myip_v1_0_HLS_weimb6) {


static const unsigned DataWidth = 32;
static const unsigned AddressRange = 172;
static const unsigned AddressWidth = 8;

sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in<sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


myip_v1_0_HLS_weimb6_ram* meminst;


SC_CTOR(myip_v1_0_HLS_weimb6) {
meminst = new myip_v1_0_HLS_weimb6_ram("myip_v1_0_HLS_weimb6_ram");
meminst->address0(address0);
meminst->ce0(ce0);
meminst->q0(q0);

meminst->reset(reset);
meminst->clk(clk);
}
~myip_v1_0_HLS_weimb6() {
    delete meminst;
}


};//endmodule
#endif