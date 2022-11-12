// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __myip_v1_0_HLS_weisc4_H__
#define __myip_v1_0_HLS_weisc4_H__


#include <systemc>
using namespace sc_core;
using namespace sc_dt;




#include <iostream>
#include <fstream>

struct myip_v1_0_HLS_weisc4_ram : public sc_core::sc_module {

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


   SC_CTOR(myip_v1_0_HLS_weisc4_ram) {
        ram[0] = "0b00111101011110110010100000111100";
        ram[1] = "0b00111110000100100111110110000100";
        ram[2] = "0b10111100101100101000100010010011";
        ram[3] = "0b00111101101100100110101000101101";
        ram[4] = "0b00111110001111000111000110010011";
        ram[5] = "0b10111100011100001101110001001111";
        ram[6] = "0b00111110100011100101001101110100";
        ram[7] = "0b00111101101100111111010001101110";
        ram[8] = "0b00111101100110000001101100100010";
        ram[9] = "0b10111101011010000101111000011001";
        ram[10] = "0b10111100100100011000101010011011";
        ram[11] = "0b00111101110111000111110100001010";
        ram[12] = "0b10111100111101001000000011010110";
        ram[13] = "0b10111100111101001001000001110111";
        ram[14] = "0b10111110011100010100000010110011";
        ram[15] = "0b10111110000100100101000110100111";
        ram[16] = "0b10111110010111110000001000010000";
        ram[17] = "0b10111110001001011101101001000000";
        ram[18] = "0b10111110100110110010010000100001";
        ram[19] = "0b10111101101010010110010100011111";
        ram[20] = "0b00111100101001011000011110010100";
        ram[21] = "0b00111110010011000110101000011001";
        ram[22] = "0b00111101100111110010101011111001";
        ram[23] = "0b10111101101011011101000001101010";
        ram[24] = "0b10111101000000001000100110111001";
        ram[25] = "0b10111101010101000000111100100100";
        ram[26] = "0b00111110001011011001110011001110";
        ram[27] = "0b10111011000100111111110101100000";
        ram[28] = "0b00111101100110101010010101111000";
        ram[29] = "0b00111101010110000011011111011001";
        ram[30] = "0b10111100100000001000001000011011";
        ram[31] = "0b00111101111111001000111111011100";
        ram[32] = "0b10111110011000001011010011010100";
        ram[33] = "0b00111101111000110001100110101010";
        ram[34] = "0b00111101100101001001101100010111";
        ram[35] = "0b10111101110000001101110010001110";
        ram[36] = "0b10111100000100101100101001001001";
        ram[37] = "0b10111110001001100110010001011101";
        ram[38] = "0b00111110010000101100111101100010";
        ram[39] = "0b10111101110111001101010100010111";
        ram[40] = "0b00111110010001000000001001010010";
        ram[41] = "0b00111110001101010000000111001110";
        ram[42] = "0b10111110100010001000101010010010";
        ram[43] = "0b00111101110011110101111001001101";
        ram[44] = "0b10111101001110010100101111000101";
        ram[45] = "0b00111101110010101001110100001010";
        ram[46] = "0b10111101011111101111101110110110";
        ram[47] = "0b10111110000000010010001000101000";
        ram[48] = "0b10111110010100110001111101000000";
        ram[49] = "0b00111101100100110100100101000011";
        ram[50] = "0b10111100101101111010001100100010";
        ram[51] = "0b10111110010100110001001001110111";
        ram[52] = "0b00111100101000000101100000010001";
        ram[53] = "0b00111101111011010110111100001000";
        ram[54] = "0b00111110100000100011100011001010";
        ram[55] = "0b00111101010100011110001000011100";
        ram[56] = "0b00111110000101100110100011100110";
        ram[57] = "0b10111101111010110101001101010100";
        ram[58] = "0b10111110011001101101111011010111";
        ram[59] = "0b00111101011111011011000100110100";
        ram[60] = "0b10111110001100011110111111100101";
        ram[61] = "0b10111110100001000110101100100011";
        ram[62] = "0b00111000111011110010110110101100";
        ram[63] = "0b10111110001010010101111010110101";
        ram[64] = "0b00111100011000110000101010000111";
        ram[65] = "0b00111100111010010000110000010000";
        ram[66] = "0b10111101011111100010111100111110";
        ram[67] = "0b00111110000001101011110000000101";
        ram[68] = "0b00111110100011001010000011000100";
        ram[69] = "0b00111101011111110100000101111011";
        ram[70] = "0b00111101100011010100100100010001";
        ram[71] = "0b10111101101011011101110101000000";
        ram[72] = "0b00111101001110000011010100100000";
        ram[73] = "0b10111100011101101001000111010100";
        ram[74] = "0b10111110010000011010100000000000";
        ram[75] = "0b00111110001111101011100011111001";
        ram[76] = "0b10111101101110101101100110100010";
        ram[77] = "0b00111101001011111011111001010110";
        ram[78] = "0b10111110001111111111110100100101";
        ram[79] = "0b10111101101101101010101001110100";
        ram[80] = "0b10111110010100001010010111000010";
        ram[81] = "0b10111110010011010010111100100010";
        ram[82] = "0b10111110000010010111010111001101";
        ram[83] = "0b10111101110111111010111100000110";
        ram[84] = "0b10111110001001010010100001111100";
        ram[85] = "0b10111110001000111000100101100101";
        ram[86] = "0b10111101111010001110101111001011";
        ram[87] = "0b00111100110010111011111000101110";
        ram[88] = "0b00111101111001100101011000100100";
        ram[89] = "0b10111101100001100100000100001011";
        ram[90] = "0b00111100110100100010011110101100";
        ram[91] = "0b10111101100011110110001110011101";
        ram[92] = "0b10111110011111110100001111010011";
        ram[93] = "0b00111110001000011100011010100011";
        ram[94] = "0b00111101111001110000110110111111";
        ram[95] = "0b10111110001100101010111110000100";
        ram[96] = "0b00111011101000110010001000000010";
        ram[97] = "0b10111100100101100000001010101100";
        ram[98] = "0b00111100110110011100111100000001";
        ram[99] = "0b00111110010010111110100100100111";
        ram[100] = "0b00111101100101011100010101110101";
        ram[101] = "0b00111100001110011010000010110100";
        ram[102] = "0b10111100010000111100100010001101";
        ram[103] = "0b10111101111001100110001011001110";
        ram[104] = "0b00111011101011001010100100001011";
        ram[105] = "0b00111110000101011001001010101110";
        ram[106] = "0b10111101010000000010001101011101";
        ram[107] = "0b10111101110110000001011001110001";
        ram[108] = "0b10111101101001000110011101100011";
        ram[109] = "0b00111101111111010011000110000000";
        ram[110] = "0b10111110000001011110011010101100";
        ram[111] = "0b00111110000011010001101101110110";
        ram[112] = "0b00111110000000100010110110100100";
        ram[113] = "0b00111101111101000101001111110001";
        ram[114] = "0b00111110010000111111000110010100";
        ram[115] = "0b10111011100010001101110100110000";
        ram[116] = "0b10111110100001100110110001001011";
        ram[117] = "0b00111101011110011011100110100010";
        ram[118] = "0b10111101010010010011001110011001";
        ram[119] = "0b10111101011100011100100110100100";
        ram[120] = "0b00111101001101011111110110111000";
        ram[121] = "0b00111100111110011100110111101010";
        ram[122] = "0b00111010011100010011100110010000";
        ram[123] = "0b10111110000010111110001110101111";
        ram[124] = "0b10111101111110111011100111000111";
        ram[125] = "0b10111101001000100110101010100001";
        ram[126] = "0b00111101100000100111111000000000";
        ram[127] = "0b00111011111000101101100101010101";
        ram[128] = "0b10111110001001111100001101001001";
        ram[129] = "0b00111110000011000010011011101011";
        ram[130] = "0b00111101001100110000110110010100";
        ram[131] = "0b00111110001001000100111101001000";
        ram[132] = "0b10111101101101001110111011111011";
        ram[133] = "0b10111110100011101010110101110100";
        ram[134] = "0b10111101101111100110010011100100";
        ram[135] = "0b00111101011000000001011000110101";
        ram[136] = "0b00111101011100011100111001011000";
        ram[137] = "0b00111101100111100111110110111001";
        ram[138] = "0b10111100101010101011100101010010";
        ram[139] = "0b00111011001100010110010101101011";
        ram[140] = "0b00111101100100000000110101001110";
        ram[141] = "0b00111101001101101100111100000000";
        ram[142] = "0b00111101011001010101011000011111";
        ram[143] = "0b10111101111000100010001010110010";
        ram[144] = "0b10111110001000011000011111110011";
        ram[145] = "0b10111110000001001001011111010110";
        ram[146] = "0b00111110010110110101000111110110";
        ram[147] = "0b00111110011000001110010110010000";
        ram[148] = "0b10111100000111011010011001111100";
        ram[149] = "0b00111110010110000101110111001011";
        ram[150] = "0b10111101110101011010110000111100";
        ram[151] = "0b10111101100011001011001101010111";
        ram[152] = "0b10111110001000000011110110100000";
        ram[153] = "0b00111110001001011001101011101111";
        ram[154] = "0b10111110001011101101111101011100";
        ram[155] = "0b10111101001011101010010100011111";
        ram[156] = "0b10111100100000010101100100100111";
        ram[157] = "0b00111101100100000101001011010100";
        ram[158] = "0b10111110000100110011111110000010";
        ram[159] = "0b10111101100111001000000000110110";
        ram[160] = "0b10111100101010001011101010001100";
        ram[161] = "0b10111100100001110011110000100111";
        ram[162] = "0b10111101101001101110001110000010";
        ram[163] = "0b10111110000011001011011101010001";
        ram[164] = "0b00111101101011000100011010111110";
        ram[165] = "0b00111110010011110000011001101111";
        ram[166] = "0b00111101010001101000000011100100";
        ram[167] = "0b00111110001110111000010110001101";
        ram[168] = "0b10111101111001011001011011001001";
        ram[169] = "0b00111110010111111010101111001010";
        ram[170] = "0b10111110101100010010101011110110";
        ram[171] = "0b10111110000110010101100011001101";


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


SC_MODULE(myip_v1_0_HLS_weisc4) {


static const unsigned DataWidth = 32;
static const unsigned AddressRange = 172;
static const unsigned AddressWidth = 8;

sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in<sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


myip_v1_0_HLS_weisc4_ram* meminst;


SC_CTOR(myip_v1_0_HLS_weisc4) {
meminst = new myip_v1_0_HLS_weisc4_ram("myip_v1_0_HLS_weisc4_ram");
meminst->address0(address0);
meminst->ce0(ce0);
meminst->q0(q0);

meminst->reset(reset);
meminst->clk(clk);
}
~myip_v1_0_HLS_weisc4() {
    delete meminst;
}


};//endmodule
#endif