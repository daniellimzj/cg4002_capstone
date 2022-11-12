// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __myip_v1_0_HLS_weiDeQ_H__
#define __myip_v1_0_HLS_weiDeQ_H__


#include <systemc>
using namespace sc_core;
using namespace sc_dt;




#include <iostream>
#include <fstream>

struct myip_v1_0_HLS_weiDeQ_ram : public sc_core::sc_module {

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


   SC_CTOR(myip_v1_0_HLS_weiDeQ_ram) {
        ram[0] = "0b00111010010011101111100010010100";
        ram[1] = "0b10111101000110010111101100000111";
        ram[2] = "0b00111100110011001000100111011101";
        ram[3] = "0b00111101101110010010101110100100";
        ram[4] = "0b10111110000101110010011110010101";
        ram[5] = "0b00111110100000111000101110001100";
        ram[6] = "0b10111100000001011000011101010010";
        ram[7] = "0b00111100110001011110010010100110";
        ram[8] = "0b00111110101111111010101000111110";
        ram[9] = "0b00111110000001100011101111000011";
        ram[10] = "0b00111101001011101010110001110101";
        ram[11] = "0b10111101001011110011110001110110";
        ram[12] = "0b00111101111101001011000010000101";
        ram[13] = "0b00111110100011100101011010011111";
        ram[14] = "0b00111011110110010101111111001101";
        ram[15] = "0b10111110000011010101011100110100";
        ram[16] = "0b00111100100101010101100101011011";
        ram[17] = "0b10111101100011001001111011100000";
        ram[18] = "0b10111100100111100011101000011100";
        ram[19] = "0b10111101001001001010010110010100";
        ram[20] = "0b10111101111001011000000101100001";
        ram[21] = "0b00111101000000000001110101100100";
        ram[22] = "0b10111101101011110110011110010010";
        ram[23] = "0b10111101111100101101010111000000";
        ram[24] = "0b10111110000111101101110000101000";
        ram[25] = "0b10111101000101001000011111111111";
        ram[26] = "0b10111101111111111000001110010111";
        ram[27] = "0b10111101101110011101010001011001";
        ram[28] = "0b10111110000000001011011001101011";
        ram[29] = "0b10111101110011111100001001011001";
        ram[30] = "0b00111101101001011111001110101001";
        ram[31] = "0b10111101101010010100100111001011";
        ram[32] = "0b10111101010001000101010011101100";
        ram[33] = "0b00111101100001101000110111000000";
        ram[34] = "0b00111110001000100010101000100111";
        ram[35] = "0b10111101000100110001001000100000";
        ram[36] = "0b10111100100110010011000100111010";
        ram[37] = "0b10111101001001110101100011111111";
        ram[38] = "0b00111110000000111001010001011101";
        ram[39] = "0b10111101000100011110110011000011";
        ram[40] = "0b00111100101001011011111000000101";
        ram[41] = "0b00111110000100110001111110011001";
        ram[42] = "0b00111100110101101011111000111011";
        ram[43] = "0b10111100011110010010111100011000";
        ram[44] = "0b00111110000011100000100010110011";
        ram[45] = "0b10111100101110000101110110010011";
        ram[46] = "0b10111101100010101000000011001111";
        ram[47] = "0b00111101000000001100101011011110";
        ram[48] = "0b00111011100001011011111000101001";
        ram[49] = "0b10111110010011111010010001100110";
        ram[50] = "0b10111110000101011101000011101110";
        ram[51] = "0b00111101100100010111011010000111";
        ram[52] = "0b10111110010101011111111010010000";
        ram[53] = "0b00111110011100110111100000110111";
        ram[54] = "0b10111100110001100001011111100010";
        ram[55] = "0b00111110010100111101101001100000";
        ram[56] = "0b10111100000011111001111010010001";
        ram[57] = "0b10111100100000110110100111011001";
        ram[58] = "0b10111101011011001011101011110010";
        ram[59] = "0b10111101101110100000111100110111";
        ram[60] = "0b00111110001110110100001010011100";
        ram[61] = "0b00111101100110010010000111100111";
        ram[62] = "0b10111101110001111101011100010001";
        ram[63] = "0b10111101010110110100011010010111";
        ram[64] = "0b00111101000001100111011001110100";
        ram[65] = "0b10111100000010011010110101000000";
        ram[66] = "0b00111110000001001110011001110001";
        ram[67] = "0b10111100100110110100101111111010";
        ram[68] = "0b00111110001110001111100101000000";
        ram[69] = "0b10111101110100111000001101101100";
        ram[70] = "0b10111101100111000110000010000000";
        ram[71] = "0b10111010110010101010110111110000";
        ram[72] = "0b10111101101000111101110111001010";
        ram[73] = "0b10111010111111100010011111110000";
        ram[74] = "0b00111101010011111010010111010000";
        ram[75] = "0b10111110010010000010110100000111";
        ram[76] = "0b00111101011010111001110001011011";
        ram[77] = "0b10111101111111000110011001011011";
        ram[78] = "0b10111101011101010101010100001100";
        ram[79] = "0b10111110000111110011101011011110";
        ram[80] = "0b00111101111100100111011011011001";
        ram[81] = "0b00111110001100000001010011101010";
        ram[82] = "0b10111110000010101110100100111011";
        ram[83] = "0b10111101111110101011011010101100";
        ram[84] = "0b00111101111110000100000101001000";
        ram[85] = "0b00111101001010001111110101001000";
        ram[86] = "0b00111110001100101010100000110010";
        ram[87] = "0b00111110000011000000011101100000";
        ram[88] = "0b10111110001111101001011111010001";
        ram[89] = "0b10111101101101101011111111011001";
        ram[90] = "0b10111110001011110001111100101011";
        ram[91] = "0b00111101011001011010011010110001";
        ram[92] = "0b00111100110011011100100100010101";
        ram[93] = "0b10111101110101000000000010101100";
        ram[94] = "0b10111101110101100100000110111111";
        ram[95] = "0b00111110000000100001110101001110";
        ram[96] = "0b00111101111111001011101100001100";
        ram[97] = "0b00111101111010000101000101111101";
        ram[98] = "0b10111110010000001011110001110001";
        ram[99] = "0b10111101011001001011010011010001";
        ram[100] = "0b10111100100010100100111101111001";
        ram[101] = "0b00111101101100111000000111001010";
        ram[102] = "0b10111110011110110110000100000111";
        ram[103] = "0b00111101011111001011011111100011";
        ram[104] = "0b10111100111010001101001010000010";
        ram[105] = "0b00111101110110001000100111010110";
        ram[106] = "0b10111110010100010001010011111000";
        ram[107] = "0b00111101111100101100010000101101";
        ram[108] = "0b10111110000010111000101100111101";
        ram[109] = "0b10111101101000101011001110100001";
        ram[110] = "0b00111101101100110011110110000110";
        ram[111] = "0b00111101110000000110010101000000";
        ram[112] = "0b10111110011110010110001100110101";
        ram[113] = "0b10111110000010011000101100000000";
        ram[114] = "0b00111101111100111110011001001010";
        ram[115] = "0b10111101110000111101001000100000";
        ram[116] = "0b00111101110111001001111110010001";
        ram[117] = "0b10111101100100101101100111001111";
        ram[118] = "0b00111101101101101010000110100101";
        ram[119] = "0b10111101110101010000110100101011";
        ram[120] = "0b00111101001111101110011010011001";
        ram[121] = "0b10111011001100000100010101010001";
        ram[122] = "0b10111110001001011010001100110101";
        ram[123] = "0b10111100111010111000001011001010";
        ram[124] = "0b00111110001110010111010010110110";
        ram[125] = "0b10111100101001111101100010011111";
        ram[126] = "0b00111110001111000010000111110100";
        ram[127] = "0b00111101111000011100011100111111";
        ram[128] = "0b00111101101111010111101100100011";
        ram[129] = "0b00111101001010010011110011111100";
        ram[130] = "0b10111101101111011100100111110001";
        ram[131] = "0b10111101010100010001111001100001";
        ram[132] = "0b00111101110100111111010100001101";
        ram[133] = "0b00111101110011001010100000100110";
        ram[134] = "0b00111110000000010110010111110000";
        ram[135] = "0b00111101011001110111011010100100";
        ram[136] = "0b10111101010110001101001000110010";
        ram[137] = "0b00111101100011010001100010000000";
        ram[138] = "0b10111011010110111010111111010101";
        ram[139] = "0b10111101101000001011101011000011";
        ram[140] = "0b00111101110011110011101111101101";
        ram[141] = "0b10111101011011111011110100101101";
        ram[142] = "0b10111110001000010111110010011101";
        ram[143] = "0b00111110000010010100001111111101";
        ram[144] = "0b10111101110001100010010110111011";
        ram[145] = "0b00111100011111100110011010111100";
        ram[146] = "0b10111110011000101100010110100100";
        ram[147] = "0b10111100010111111011001000011110";
        ram[148] = "0b10111100110001011000100110110101";
        ram[149] = "0b10111100110111101110111010000011";
        ram[150] = "0b00111110010000010111110010111001";
        ram[151] = "0b10111101000110010101100010010111";
        ram[152] = "0b00111110001001011010110111100101";
        ram[153] = "0b00111110010001010000000001111111";
        ram[154] = "0b00111101001011100110111101000111";
        ram[155] = "0b00111100101101110111111010111110";
        ram[156] = "0b00111100101011001101011011011100";
        ram[157] = "0b10111110010011011100010101010101";
        ram[158] = "0b10111100111110111010101101010010";
        ram[159] = "0b10111101110110010011101001110000";
        ram[160] = "0b00111101111101010011100111011011";
        ram[161] = "0b00111110100000100000001010001000";
        ram[162] = "0b10111110001010100110101111101100";
        ram[163] = "0b00111110000110111000011000001101";
        ram[164] = "0b00111101100001001011111110100000";
        ram[165] = "0b10111100011011010100001010000101";
        ram[166] = "0b00111010100110101111001110001001";
        ram[167] = "0b00111100101000010000101011110110";
        ram[168] = "0b00111101110110000110001000000010";
        ram[169] = "0b00111101000011001010000001000011";
        ram[170] = "0b00111110000100011001011100110101";
        ram[171] = "0b00111110001100110110011001001011";


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


SC_MODULE(myip_v1_0_HLS_weiDeQ) {


static const unsigned DataWidth = 32;
static const unsigned AddressRange = 172;
static const unsigned AddressWidth = 8;

sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in<sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


myip_v1_0_HLS_weiDeQ_ram* meminst;


SC_CTOR(myip_v1_0_HLS_weiDeQ) {
meminst = new myip_v1_0_HLS_weiDeQ_ram("myip_v1_0_HLS_weiDeQ_ram");
meminst->address0(address0);
meminst->ce0(ce0);
meminst->q0(q0);

meminst->reset(reset);
meminst->clk(clk);
}
~myip_v1_0_HLS_weiDeQ() {
    delete meminst;
}


};//endmodule
#endif