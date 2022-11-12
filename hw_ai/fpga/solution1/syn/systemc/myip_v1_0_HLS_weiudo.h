// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __myip_v1_0_HLS_weiudo_H__
#define __myip_v1_0_HLS_weiudo_H__


#include <systemc>
using namespace sc_core;
using namespace sc_dt;




#include <iostream>
#include <fstream>

struct myip_v1_0_HLS_weiudo_ram : public sc_core::sc_module {

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


   SC_CTOR(myip_v1_0_HLS_weiudo_ram) {
        ram[0] = "0b10111100110001100010000101000011";
        ram[1] = "0b00111100100011101010101100000111";
        ram[2] = "0b00111101111101110001110000011001";
        ram[3] = "0b00111101110000100111101100110100";
        ram[4] = "0b00111110000101101101000100011001";
        ram[5] = "0b00111110001001110100100000010000";
        ram[6] = "0b00111110010001100011100001011001";
        ram[7] = "0b10111110000001110100100000100111";
        ram[8] = "0b10111101011100001110101110010111";
        ram[9] = "0b00111101000010001001010011000100";
        ram[10] = "0b10111101101111110010100010101011";
        ram[11] = "0b10111110010000110011011100010000";
        ram[12] = "0b00111110100000011000010110011110";
        ram[13] = "0b00111110010001101010101000100100";
        ram[14] = "0b00111101100010100101000101011111";
        ram[15] = "0b10111110001100110111100011001001";
        ram[16] = "0b00111101011111110101110000011010";
        ram[17] = "0b10111110011100001001111001000111";
        ram[18] = "0b10111110001001100100100110111011";
        ram[19] = "0b10111011010011111010110001010111";
        ram[20] = "0b10111110011001010111100011101011";
        ram[21] = "0b10111101101100111011000101111011";
        ram[22] = "0b10111110000111110111110010000110";
        ram[23] = "0b00111101100110010111111010101010";
        ram[24] = "0b10111100111010011100111011000100";
        ram[25] = "0b10111101111100111100110000101001";
        ram[26] = "0b00111110001100010101101100001111";
        ram[27] = "0b00111101101000100110111010101010";
        ram[28] = "0b10111101100110010101101101111111";
        ram[29] = "0b00111101101011001001000101111010";
        ram[30] = "0b10111101110010100001011110110110";
        ram[31] = "0b10111101100100010100100101110001";
        ram[32] = "0b00111101101010101100000101101100";
        ram[33] = "0b00111101110111011110000110010100";
        ram[34] = "0b00111100001011000111010001000100";
        ram[35] = "0b10111110000000110100111101110011";
        ram[36] = "0b00111011011101111110110111111100";
        ram[37] = "0b10111101001000100111010001000010";
        ram[38] = "0b10111101110110001111000110111111";
        ram[39] = "0b10111101000111001011110101001110";
        ram[40] = "0b00111101110100110001000001011010";
        ram[41] = "0b10111110000111100110101000011100";
        ram[42] = "0b00111110010001000101100001110001";
        ram[43] = "0b10111110001000011001001011111111";
        ram[44] = "0b00111101100010101111011110101101";
        ram[45] = "0b00111101100101100011100010001101";
        ram[46] = "0b10111110001001010100111101110001";
        ram[47] = "0b10111100000111110110110101010110";
        ram[48] = "0b00111110001101111010000110101111";
        ram[49] = "0b10111101001101010110001011000110";
        ram[50] = "0b00111101110100100111101101110101";
        ram[51] = "0b10111101110111100000001100000111";
        ram[52] = "0b10111101101110100000000000101101";
        ram[53] = "0b00111101011100011110000100100010";
        ram[54] = "0b10111101111000011101100100011100";
        ram[55] = "0b00111101001110110100101110110001";
        ram[56] = "0b10111110001101110101111100101111";
        ram[57] = "0b10111110010100111100000110001011";
        ram[58] = "0b00111110000001000011110110111001";
        ram[59] = "0b10111110011011110101010001001000";
        ram[60] = "0b10111101001111000010011000111000";
        ram[61] = "0b00111110010111100100001001111011";
        ram[62] = "0b10111110000000111111011001010111";
        ram[63] = "0b00111110011001010110100011000001";
        ram[64] = "0b10111101011010000110001101101000";
        ram[65] = "0b10111101011111001111000101111010";
        ram[66] = "0b00111101001110000100010100011100";
        ram[67] = "0b10111110000000000001001111011101";
        ram[68] = "0b00111101101110111110010001010001";
        ram[69] = "0b10111101010000011110110111011111";
        ram[70] = "0b10111110001011011111001001110110";
        ram[71] = "0b00111110001011010111010111110001";
        ram[72] = "0b00111110001001111110111100011000";
        ram[73] = "0b10111110000000011100101111011110";
        ram[74] = "0b10111011000001110110101111100111";
        ram[75] = "0b10111110010111111001101111000110";
        ram[76] = "0b00111110100001110100000011101011";
        ram[77] = "0b10111101101010001101000100111001";
        ram[78] = "0b10111110000000010100001100100111";
        ram[79] = "0b00111101001000111110101111111100";
        ram[80] = "0b00111110010110001110110011011011";
        ram[81] = "0b00111101100000010100001111001010";
        ram[82] = "0b00111101100111111110111101101100";
        ram[83] = "0b10111101110011100111010000100111";
        ram[84] = "0b00111101100000011000101100100001";
        ram[85] = "0b00111101101100110001001110000110";
        ram[86] = "0b00111101000000101001011101101010";
        ram[87] = "0b00111101010000111101110010111101";
        ram[88] = "0b10111110000110000000101011001001";
        ram[89] = "0b00111101100100101110000011100000";
        ram[90] = "0b00111100111111011011110101000000";
        ram[91] = "0b10111101110110110100001011000011";
        ram[92] = "0b00111101001000011000101100001101";
        ram[93] = "0b00111110100000001011101001001011";
        ram[94] = "0b10111110000000001110011110101111";
        ram[95] = "0b00111101010011110101000100110001";
        ram[96] = "0b10111101011001011011111101111110";
        ram[97] = "0b00111110001100111011001010001110";
        ram[98] = "0b10111110010101110011110010011010";
        ram[99] = "0b00111100110110010101001011101011";
        ram[100] = "0b10111101000111011100111011111100";
        ram[101] = "0b00111011110110001110101110011100";
        ram[102] = "0b10111101100000100010101111000100";
        ram[103] = "0b10111101010010011100011111010010";
        ram[104] = "0b10111101001111000011100000000001";
        ram[105] = "0b10111110011010101100010010111110";
        ram[106] = "0b00111110000111001100110000101110";
        ram[107] = "0b00111101011011110111010110011001";
        ram[108] = "0b10111100101010001001010000111111";
        ram[109] = "0b00111100101111101001001001001010";
        ram[110] = "0b10111110010100111100110110001100";
        ram[111] = "0b00111101111100011011110100001001";
        ram[112] = "0b00111101100111010101100011100110";
        ram[113] = "0b00111101100001111001100010110101";
        ram[114] = "0b10111100110101110011100100011110";
        ram[115] = "0b00111110011010111001010110111011";
        ram[116] = "0b00111101000001010000101110001001";
        ram[117] = "0b10111100110101010111100010000011";
        ram[118] = "0b10111110000001011010011010001010";
        ram[119] = "0b00111100010011110110111111111110";
        ram[120] = "0b10111110000001011001000010100111";
        ram[121] = "0b10111101100101011001011010100100";
        ram[122] = "0b00111110010111001010110111000001";
        ram[123] = "0b10111101100001000010011000111010";
        ram[124] = "0b00111110001100110100111011010010";
        ram[125] = "0b10111100001011000110101111010110";
        ram[126] = "0b10111101001000110010010000010000";
        ram[127] = "0b10111101001001010011010101000001";
        ram[128] = "0b10111101100101000110000110011001";
        ram[129] = "0b00111101001001000101011000010110";
        ram[130] = "0b00111010000010111100010111111010";
        ram[131] = "0b10111110010011001100100100001101";
        ram[132] = "0b10111110010110001000001101111111";
        ram[133] = "0b00111110000000011110110000110011";
        ram[134] = "0b10111100101011000100010011100001";
        ram[135] = "0b10111100001010010110101111000101";
        ram[136] = "0b10111110010011001001011001001010";
        ram[137] = "0b10111101110010001110001110000000";
        ram[138] = "0b00111101110000010110110000100101";
        ram[139] = "0b00111101000101011101010101110000";
        ram[140] = "0b00111101111111110111110100010010";
        ram[141] = "0b00111101111010100110100110011111";
        ram[142] = "0b00111101001011000010010110011110";
        ram[143] = "0b10111101101000111011101001000011";
        ram[144] = "0b10111110000011011000000010011111";
        ram[145] = "0b00111101101100001101011000101011";
        ram[146] = "0b10111101111000111001100111101011";
        ram[147] = "0b00111110000101011110111001010111";
        ram[148] = "0b00111110010111011100101100100000";
        ram[149] = "0b00111101101010111111010000000100";
        ram[150] = "0b00111110000110101011010000000001";
        ram[151] = "0b10111110001100100011011010110100";
        ram[152] = "0b10111101111001001111111100101110";
        ram[153] = "0b00111101011001111010010100000010";
        ram[154] = "0b00111101100001111001101011101110";
        ram[155] = "0b10111101001111010110100011000111";
        ram[156] = "0b00111110000100100010001001010110";
        ram[157] = "0b10111101001011010000011110111111";
        ram[158] = "0b10111101100110100011011011100001";
        ram[159] = "0b00111101100110100001110101110100";
        ram[160] = "0b10111101101100000100111011010010";
        ram[161] = "0b10111011000101111011110001110100";
        ram[162] = "0b10111110000101001010001111101000";
        ram[163] = "0b10111101011110000111101101010100";
        ram[164] = "0b10111110001000010000111110111101";
        ram[165] = "0b00111101111011100001001110001000";
        ram[166] = "0b00111101111010011000111001010101";
        ram[167] = "0b10111110010100110100000011010110";
        ram[168] = "0b00111101100000011011110110110100";
        ram[169] = "0b10111101100000001111000000110100";
        ram[170] = "0b10111100010001110111011110000000";
        ram[171] = "0b00111110011001111001010111111111";


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


SC_MODULE(myip_v1_0_HLS_weiudo) {


static const unsigned DataWidth = 32;
static const unsigned AddressRange = 172;
static const unsigned AddressWidth = 8;

sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in<sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


myip_v1_0_HLS_weiudo_ram* meminst;


SC_CTOR(myip_v1_0_HLS_weiudo) {
meminst = new myip_v1_0_HLS_weiudo_ram("myip_v1_0_HLS_weiudo_ram");
meminst->address0(address0);
meminst->ce0(ce0);
meminst->q0(q0);

meminst->reset(reset);
meminst->clk(clk);
}
~myip_v1_0_HLS_weiudo() {
    delete meminst;
}


};//endmodule
#endif