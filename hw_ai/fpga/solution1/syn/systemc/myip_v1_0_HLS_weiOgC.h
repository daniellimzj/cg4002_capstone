// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __myip_v1_0_HLS_weiOgC_H__
#define __myip_v1_0_HLS_weiOgC_H__


#include <systemc>
using namespace sc_core;
using namespace sc_dt;




#include <iostream>
#include <fstream>

struct myip_v1_0_HLS_weiOgC_ram : public sc_core::sc_module {

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


   SC_CTOR(myip_v1_0_HLS_weiOgC_ram) {
        ram[0] = "0b10111110010001101010011011100100";
        ram[1] = "0b10111110001001010110001001001011";
        ram[2] = "0b00111101001111111000101100101100";
        ram[3] = "0b00111101010111010010001001011001";
        ram[4] = "0b00111101101011011011001010000010";
        ram[5] = "0b00111101000010110101001110111101";
        ram[6] = "0b10111101000100011010100011100001";
        ram[7] = "0b10111110000101001100111010110011";
        ram[8] = "0b10111101011001010000011000011100";
        ram[9] = "0b00111101110010001101011111111010";
        ram[10] = "0b00111101101000001000000000001010";
        ram[11] = "0b10111110010111001110101001110111";
        ram[12] = "0b00111110000100001001010101011110";
        ram[13] = "0b10111101101110000110111000111111";
        ram[14] = "0b10111110000010011001010001000001";
        ram[15] = "0b00111101100010000100010100111101";
        ram[16] = "0b00111110001110000110010110111010";
        ram[17] = "0b00111100110111001010110111100100";
        ram[18] = "0b00111101000010000100010101101011";
        ram[19] = "0b00111101010001010001100010111100";
        ram[20] = "0b10111101010001111011001100011010";
        ram[21] = "0b10111110010001101010001011011101";
        ram[22] = "0b00111110000010110100000110011111";
        ram[23] = "0b10111110000110111011001000100100";
        ram[24] = "0b00111110001101011101011101010000";
        ram[25] = "0b10111010101101011010110000110101";
        ram[26] = "0b00111110000111011101010001011110";
        ram[27] = "0b00111100111100111010011110000011";
        ram[28] = "0b10111110101010010100000111001100";
        ram[29] = "0b00111110011011010000100001111111";
        ram[30] = "0b10111101000110001001000010011011";
        ram[31] = "0b10111101011001011000110011010110";
        ram[32] = "0b00111101111000000011111000001100";
        ram[33] = "0b10111110001001011000001001110000";
        ram[34] = "0b10111101100001110100111111101000";
        ram[35] = "0b00111010101000110110011000100010";
        ram[36] = "0b10111101110110000000010001000000";
        ram[37] = "0b10111100101100000010001111000101";
        ram[38] = "0b00111101001011101100111110111110";
        ram[39] = "0b10111101110111110110000101110101";
        ram[40] = "0b10111101100101101100001101011101";
        ram[41] = "0b10111101101101011111011010111010";
        ram[42] = "0b10111101001100111000101110101101";
        ram[43] = "0b10111110010010111001110010101000";
        ram[44] = "0b00111101011001110001101101000111";
        ram[45] = "0b10111110000110111100100101111110";
        ram[46] = "0b00111101110001000010001011110100";
        ram[47] = "0b00111100110001010110001111110011";
        ram[48] = "0b00111011001010101111000110010000";
        ram[49] = "0b10111011110011100110000001110100";
        ram[50] = "0b00111101000110100101111001111110";
        ram[51] = "0b00111101110001001000000101011001";
        ram[52] = "0b10111110000000110010011111011001";
        ram[53] = "0b00111101001101101000000010100101";
        ram[54] = "0b00111101101000101110111110111110";
        ram[55] = "0b10111110011011000110101101110010";
        ram[56] = "0b10111101011100000101110000000101";
        ram[57] = "0b10111100100111100110111100001101";
        ram[58] = "0b10111110011110110100111000011000";
        ram[59] = "0b10111100100101110000101010001101";
        ram[60] = "0b10111110010101001101110110110100";
        ram[61] = "0b00111110000001001111011010000100";
        ram[62] = "0b00111101110000010001100010000100";
        ram[63] = "0b00111110100001100000011001111000";
        ram[64] = "0b10111101100100000111101001000100";
        ram[65] = "0b10111110000110110010001100111111";
        ram[66] = "0b00111101101101110110100001010100";
        ram[67] = "0b10111110000101011111011111100001";
        ram[68] = "0b00111011000000000000001010110001";
        ram[69] = "0b00111101101000001011100100000011";
        ram[70] = "0b10111101000100000010010111011111";
        ram[71] = "0b00111100111010110101011000011101";
        ram[72] = "0b10111101001011001011110001110100";
        ram[73] = "0b00111101010011000110010101000100";
        ram[74] = "0b10111101110001000010011001000100";
        ram[75] = "0b10111110100010100111101001101000";
        ram[76] = "0b10111110000011110000001101111011";
        ram[77] = "0b10111101000110110101110110001010";
        ram[78] = "0b00111101100010100101011101010000";
        ram[79] = "0b00111101000010011001110011010010";
        ram[80] = "0b10111101110001000011010010000100";
        ram[81] = "0b00111100101011011111000101011101";
        ram[82] = "0b00111110001010110100100001000001";
        ram[83] = "0b00111101100011110000001001100000";
        ram[84] = "0b00111101011100101011111000100011";
        ram[85] = "0b10111110010010110010110010100100";
        ram[86] = "0b10111110001011001110011100100101";
        ram[87] = "0b00111101101110001011000100110000";
        ram[88] = "0b10111110001111110100100111000011";
        ram[89] = "0b10111101010101100000010011010110";
        ram[90] = "0b10111100100010101000111101101111";
        ram[91] = "0b10111110000010100011101110110111";
        ram[92] = "0b10111011000110101000000000010110";
        ram[93] = "0b00111100100010001001111110010111";
        ram[94] = "0b00111101101001000101001011010111";
        ram[95] = "0b00111101111111010010100100101101";
        ram[96] = "0b00111101000110001100101110000100";
        ram[97] = "0b10111101010111001101001000011001";
        ram[98] = "0b00111110000010001101010011000110";
        ram[99] = "0b00111101101111101011000010101001";
        ram[100] = "0b00111110000010010010011100110100";
        ram[101] = "0b00111100100000001101110101101011";
        ram[102] = "0b10111101000000001111100110100000";
        ram[103] = "0b00111101101010110011101111011000";
        ram[104] = "0b00111110000011011100110010000110";
        ram[105] = "0b00111110000010011000111111111111";
        ram[106] = "0b10111101110010001101001101100011";
        ram[107] = "0b00111100111110000101000101100000";
        ram[108] = "0b00111101011000100010010001111010";
        ram[109] = "0b00111101110111000100111101001110";
        ram[110] = "0b00111101110000010101100001011101";
        ram[111] = "0b00111101110111111101010100011000";
        ram[112] = "0b10111101111000101110000001111010";
        ram[113] = "0b10111110000000010100111110010100";
        ram[114] = "0b10111100111100010101110110110110";
        ram[115] = "0b00111101000100000101111011000111";
        ram[116] = "0b00111110011101011010101011100110";
        ram[117] = "0b10111100110010000000000110011000";
        ram[118] = "0b00111101100001100010101001010110";
        ram[119] = "0b10111101111110110011110101110011";
        ram[120] = "0b10111101010000000000010011001011";
        ram[121] = "0b00111101001110001001000111111110";
        ram[122] = "0b10111101100011100000100000101000";
        ram[123] = "0b10111110101011101110001000000100";
        ram[124] = "0b10111101101100010001001000101110";
        ram[125] = "0b10111101100001011010010011011001";
        ram[126] = "0b00111101011001010110101011111111";
        ram[127] = "0b00111110000001011011101111111001";
        ram[128] = "0b00111101100111000010010111101000";
        ram[129] = "0b10111110011011010110000001001111";
        ram[130] = "0b00111110011101010001010100100000";
        ram[131] = "0b00111101101110000001111101001000";
        ram[132] = "0b10111101110111011110110010001110";
        ram[133] = "0b00111101011100010001010001101111";
        ram[134] = "0b00111101101011100000111011011001";
        ram[135] = "0b00111101001001111010100100100001";
        ram[136] = "0b10111101000100000010111110000111";
        ram[137] = "0b10111110001001111110101011011111";
        ram[138] = "0b10111101111001101011111000100011";
        ram[139] = "0b00111101110100011001011101111101";
        ram[140] = "0b10111110000100100001001101001111";
        ram[141] = "0b00111110001111010001010100001001";
        ram[142] = "0b10111001001010111000101100001000";
        ram[143] = "0b10111110001110111010010001100110";
        ram[144] = "0b10111101100010000000101011110011";
        ram[145] = "0b10111101000111100001111110111011";
        ram[146] = "0b00111101100010110011110111110010";
        ram[147] = "0b10111101001011110010010000100101";
        ram[148] = "0b10111101100000011001110111110011";
        ram[149] = "0b10111110001111100011011100100101";
        ram[150] = "0b00111110001010100011110110011111";
        ram[151] = "0b00111110001010111001110010110100";
        ram[152] = "0b10111101100111000111111111101000";
        ram[153] = "0b10111101100011100011110101000110";
        ram[154] = "0b00111101111110001010100010110111";
        ram[155] = "0b00111100000101001011001110111010";
        ram[156] = "0b00111101100001010111010000000000";
        ram[157] = "0b10111110011100100011001000101000";
        ram[158] = "0b00111101000010011100010010100110";
        ram[159] = "0b10111110000010001110000111111011";
        ram[160] = "0b00111110010100010010000100011101";
        ram[161] = "0b00111110110010100110110011101110";
        ram[162] = "0b00111101111111101101010111011011";
        ram[163] = "0b10111100000110011111101000110111";
        ram[164] = "0b00111110001100110000111111110110";
        ram[165] = "0b00111110010001101001000101110000";
        ram[166] = "0b10111110001001101101111011011100";
        ram[167] = "0b00111110010010110011111000110111";
        ram[168] = "0b00111110001001001100111001000101";
        ram[169] = "0b10111101110101000110101111101011";
        ram[170] = "0b00111110010110111110110000010111";
        ram[171] = "0b00111101011101010111011001100010";


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


SC_MODULE(myip_v1_0_HLS_weiOgC) {


static const unsigned DataWidth = 32;
static const unsigned AddressRange = 172;
static const unsigned AddressWidth = 8;

sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in<sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


myip_v1_0_HLS_weiOgC_ram* meminst;


SC_CTOR(myip_v1_0_HLS_weiOgC) {
meminst = new myip_v1_0_HLS_weiOgC_ram("myip_v1_0_HLS_weiOgC_ram");
meminst->address0(address0);
meminst->ce0(ce0);
meminst->q0(q0);

meminst->reset(reset);
meminst->clk(clk);
}
~myip_v1_0_HLS_weiOgC() {
    delete meminst;
}


};//endmodule
#endif