// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __myip_v1_0_HLS_weihbi_H__
#define __myip_v1_0_HLS_weihbi_H__


#include <systemc>
using namespace sc_core;
using namespace sc_dt;




#include <iostream>
#include <fstream>

struct myip_v1_0_HLS_weihbi_ram : public sc_core::sc_module {

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


   SC_CTOR(myip_v1_0_HLS_weihbi_ram) {
        ram[0] = "0b00111110011100010111111111110000";
        ram[1] = "0b00111100111100000001101101000000";
        ram[2] = "0b10111101101011011011100101000111";
        ram[3] = "0b10111101101001110001100101101001";
        ram[4] = "0b10111110001001101111111000111110";
        ram[5] = "0b10111101110111100011101001010110";
        ram[6] = "0b10111101000000101100011101101001";
        ram[7] = "0b00111110010011011110111001100101";
        ram[8] = "0b00111101100110111110111011110111";
        ram[9] = "0b10111100110101100100111010010001";
        ram[10] = "0b10111100000110010010001000110110";
        ram[11] = "0b00111101111010000010000011011111";
        ram[12] = "0b00111101100100000001001000111110";
        ram[13] = "0b00111110001110010111000010001001";
        ram[14] = "0b10111101100001011001111000011101";
        ram[15] = "0b10111101110101111110111001100001";
        ram[16] = "0b00111101111101110110101010100000";
        ram[17] = "0b10111110000101010111000100001000";
        ram[18] = "0b10111101100100111010110100111101";
        ram[19] = "0b10111101101011100000110010101001";
        ram[20] = "0b10111110000010011010111011011001";
        ram[21] = "0b10111011101111011110100111001001";
        ram[22] = "0b10111101101110011110011010101010";
        ram[23] = "0b10111110100010010110010111001110";
        ram[24] = "0b10111101111111011110010011010110";
        ram[25] = "0b00111101001011001000110101000110";
        ram[26] = "0b10111101100010000110010110000010";
        ram[27] = "0b10111101001001000000101010111000";
        ram[28] = "0b10111100001011111000111000010100";
        ram[29] = "0b10111101100010110010001110110101";
        ram[30] = "0b10111110010101010010000001110100";
        ram[31] = "0b10111101101001111011110100111101";
        ram[32] = "0b00111110010010000010001111111101";
        ram[33] = "0b00111101101101100000110010000001";
        ram[34] = "0b00111100111011110100001101000100";
        ram[35] = "0b10111110100001010101111101000100";
        ram[36] = "0b10111100000110110111011110010001";
        ram[37] = "0b10111010110100111010100000111001";
        ram[38] = "0b00111110001110010001001000011100";
        ram[39] = "0b00111110000010001010000000010001";
        ram[40] = "0b10111110001010101010110010111100";
        ram[41] = "0b00111101100011011111100000101100";
        ram[42] = "0b00111110100001001011101100011101";
        ram[43] = "0b00111101100110001010101000001001";
        ram[44] = "0b00111101100010011000111111010001";
        ram[45] = "0b10111110000111000001110100101000";
        ram[46] = "0b10111010110011100001100001001111";
        ram[47] = "0b10111011111001111110011111111101";
        ram[48] = "0b00111101011111110001100101111100";
        ram[49] = "0b00111110000011110101001100011001";
        ram[50] = "0b00111101010101101000101011111110";
        ram[51] = "0b00111110010011010110100010111010";
        ram[52] = "0b10111101001111001100010101011010";
        ram[53] = "0b10111101110010110100100101001000";
        ram[54] = "0b10111101011100000010010000111111";
        ram[55] = "0b00111101110111111001000100000100";
        ram[56] = "0b10111110000101010110100101011000";
        ram[57] = "0b10111100011010001010111100000110";
        ram[58] = "0b00111110010111011110011100111011";
        ram[59] = "0b00111101100110011010011010100110";
        ram[60] = "0b10111100110000110011101000111010";
        ram[61] = "0b10111110000010101010110101101101";
        ram[62] = "0b00111101101011100010100001101111";
        ram[63] = "0b10111110000101111111101011000101";
        ram[64] = "0b10111101100101001101001111111110";
        ram[65] = "0b00111110000111101110110101110110";
        ram[66] = "0b00111101110100111010011010100101";
        ram[67] = "0b10111101000001110000101101001001";
        ram[68] = "0b00111100010001011001000011010110";
        ram[69] = "0b00111100111000010100010100111000";
        ram[70] = "0b00111101000100010011111101001111";
        ram[71] = "0b10111110000110100011011010111111";
        ram[72] = "0b10111110000011100001101000001001";
        ram[73] = "0b00111110001010100011101001101111";
        ram[74] = "0b10111100101011101111101101110001";
        ram[75] = "0b00111110100010000011101011110111";
        ram[76] = "0b00111101000000000001011100111101";
        ram[77] = "0b10111101011111111101001010000000";
        ram[78] = "0b00111100100110110000011010010100";
        ram[79] = "0b10111101100000110001001101111000";
        ram[80] = "0b10111110000111101111011111001110";
        ram[81] = "0b10111110000010101110011000011111";
        ram[82] = "0b00111110011101010101100101111000";
        ram[83] = "0b00111100001001001101001011011111";
        ram[84] = "0b00111101100001100100000100101111";
        ram[85] = "0b10111110001111000101001110010101";
        ram[86] = "0b00111110001101000010010001001000";
        ram[87] = "0b00111110000110111011011110010011";
        ram[88] = "0b00111110100011110100100110110100";
        ram[89] = "0b00111110011111100011100100010010";
        ram[90] = "0b00111101010101010000101101101110";
        ram[91] = "0b10111100111001011100001011101101";
        ram[92] = "0b00111101001111001110011000000011";
        ram[93] = "0b00111101010010111000101111010100";
        ram[94] = "0b10111110001101110001101101101000";
        ram[95] = "0b00111101011110010010101011111001";
        ram[96] = "0b10111101111011011101101100010101";
        ram[97] = "0b10111110001010001111111010100111";
        ram[98] = "0b00111101101100111110111100001101";
        ram[99] = "0b00111100000010010101001000001111";
        ram[100] = "0b00111101100011100101101111101101";
        ram[101] = "0b00111110010001101011110010000010";
        ram[102] = "0b10111110000110000100001101110110";
        ram[103] = "0b00111101110101110010010001001000";
        ram[104] = "0b00111101110111000010100000110110";
        ram[105] = "0b10111110000101010011010000101101";
        ram[106] = "0b10111110100001011101110000011110";
        ram[107] = "0b10111101110000101010111101011110";
        ram[108] = "0b10111101110100111010101011111101";
        ram[109] = "0b10111110001000001000111011000110";
        ram[110] = "0b10111101100101011010111110100010";
        ram[111] = "0b00111101111101110000001011100001";
        ram[112] = "0b00111011000000111010110101010110";
        ram[113] = "0b00111101010100010110011100100110";
        ram[114] = "0b10111101110100110000010000010110";
        ram[115] = "0b10111101111001011100100010011011";
        ram[116] = "0b00111110000101001111000000000101";
        ram[117] = "0b10111010100111101001110111101010";
        ram[118] = "0b10111101101001101000010000000011";
        ram[119] = "0b00111101101000000010101000010001";
        ram[120] = "0b00111100101101101000000000100000";
        ram[121] = "0b00111101000011010100111100010110";
        ram[122] = "0b10111101100100110111100101010110";
        ram[123] = "0b00111110011101011010110000100100";
        ram[124] = "0b10111101111010110011010011100111";
        ram[125] = "0b00111110011010101011111101001010";
        ram[126] = "0b10111110010101100110110111100111";
        ram[127] = "0b00111101111001010011011000010110";
        ram[128] = "0b00111101010001000100001011111111";
        ram[129] = "0b00111101111111010011101101101101";
        ram[130] = "0b10111101111111111011100001001010";
        ram[131] = "0b00111101100000101101001001101001";
        ram[132] = "0b10111101111111100100110111000110";
        ram[133] = "0b00111101011000011000010101000010";
        ram[134] = "0b10111100000001001111100110100010";
        ram[135] = "0b10111101000101111001001000011110";
        ram[136] = "0b10111101111000001100111010001110";
        ram[137] = "0b00111101100111010000001010011001";
        ram[138] = "0b00111110000011110111010011100000";
        ram[139] = "0b00111100110000010011111100001110";
        ram[140] = "0b00111110010000001101000011100110";
        ram[141] = "0b00111101101000100101010111011001";
        ram[142] = "0b10111110000110110011101010000100";
        ram[143] = "0b00111101100101001100000000101100";
        ram[144] = "0b00111110011101010100010001011011";
        ram[145] = "0b10111110000110000110011000111000";
        ram[146] = "0b10111110000111010110101011100000";
        ram[147] = "0b10111101000101000001010101001111";
        ram[148] = "0b10111110000010101100111011100111";
        ram[149] = "0b10111110010000100110101110100000";
        ram[150] = "0b10111100011011101110001000011111";
        ram[151] = "0b10111101100100101111100110011010";
        ram[152] = "0b10111110000001101011011100000010";
        ram[153] = "0b00111101011101000000001101101101";
        ram[154] = "0b10111101011000011101011100111010";
        ram[155] = "0b00111101100110100100011010001001";
        ram[156] = "0b10111110000011011111001100100001";
        ram[157] = "0b10111100100001001111011010100000";
        ram[158] = "0b00111101010100000100101011011110";
        ram[159] = "0b00111101100110000101011010001100";
        ram[160] = "0b00111110000110011011001100011000";
        ram[161] = "0b10111110011000111000001100111010";
        ram[162] = "0b00111100000000111100110011010111";
        ram[163] = "0b10111100010100110010011100110010";
        ram[164] = "0b00111101110110011011010001010111";
        ram[165] = "0b10111101001000011111111100010100";
        ram[166] = "0b10111110000110011010000100111111";
        ram[167] = "0b00111101010100000110010010010010";
        ram[168] = "0b00111110000000011010111010011100";
        ram[169] = "0b00111101000101101011101101010101";
        ram[170] = "0b00111101110000001110110000110011";
        ram[171] = "0b10111101111101010100011010001000";


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


SC_MODULE(myip_v1_0_HLS_weihbi) {


static const unsigned DataWidth = 32;
static const unsigned AddressRange = 172;
static const unsigned AddressWidth = 8;

sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in<sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


myip_v1_0_HLS_weihbi_ram* meminst;


SC_CTOR(myip_v1_0_HLS_weihbi) {
meminst = new myip_v1_0_HLS_weihbi_ram("myip_v1_0_HLS_weihbi_ram");
meminst->address0(address0);
meminst->ce0(ce0);
meminst->q0(q0);

meminst->reset(reset);
meminst->clk(clk);
}
~myip_v1_0_HLS_weihbi() {
    delete meminst;
}


};//endmodule
#endif