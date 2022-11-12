// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __myip_v1_0_HLS_weieOg_H__
#define __myip_v1_0_HLS_weieOg_H__


#include <systemc>
using namespace sc_core;
using namespace sc_dt;




#include <iostream>
#include <fstream>

struct myip_v1_0_HLS_weieOg_ram : public sc_core::sc_module {

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


   SC_CTOR(myip_v1_0_HLS_weieOg_ram) {
        ram[0] = "0b10111101101101101100000111001011";
        ram[1] = "0b10111101110111011100001100001001";
        ram[2] = "0b10111101111010110001001111110001";
        ram[3] = "0b00111101100010111101100011000100";
        ram[4] = "0b00111110001100011111000110110011";
        ram[5] = "0b10111110000011100001001011101000";
        ram[6] = "0b00111101011010100100101111010110";
        ram[7] = "0b10111101110100110001001110111100";
        ram[8] = "0b00111110100101111111011001011111";
        ram[9] = "0b10111110001000110101011111110010";
        ram[10] = "0b10111100110100000010111101110011";
        ram[11] = "0b10111101100100001000010011010000";
        ram[12] = "0b10111101100111000111010010001011";
        ram[13] = "0b00111110011010011111101101011010";
        ram[14] = "0b10111100111110100001110010100110";
        ram[15] = "0b10111110000101101011111101100101";
        ram[16] = "0b00111101110001010001011110000011";
        ram[17] = "0b00111101100001010100100001101001";
        ram[18] = "0b10111101110010000001001100010010";
        ram[19] = "0b10111110000000111010000101100100";
        ram[20] = "0b10111101100110011011010001101010";
        ram[21] = "0b10111110100110101110111000110011";
        ram[22] = "0b10111101010100000101110101101001";
        ram[23] = "0b10111110010011100000110011000011";
        ram[24] = "0b10111110001011100001001011011110";
        ram[25] = "0b10111110011000010011010100010001";
        ram[26] = "0b00111101101011000110000011101010";
        ram[27] = "0b10111110001010111101000010011100";
        ram[28] = "0b10111110100110000001110000111000";
        ram[29] = "0b00111101110011101101111111010111";
        ram[30] = "0b00111101110100000100000011101111";
        ram[31] = "0b00111110011010110110000010010010";
        ram[32] = "0b00111100100010010110010011101001";
        ram[33] = "0b00111110100010101010100111110011";
        ram[34] = "0b00111110000111000010010011101101";
        ram[35] = "0b10111101001100100000011010011010";
        ram[36] = "0b10111010111101111101001010100000";
        ram[37] = "0b00111100100110110001011100011100";
        ram[38] = "0b10111101101110001001101101010111";
        ram[39] = "0b10111110001010010100101011100011";
        ram[40] = "0b00111110010101001110011010010001";
        ram[41] = "0b10111101111010100100010100011110";
        ram[42] = "0b10111110011110100111001010000110";
        ram[43] = "0b00111101111110110111001010001011";
        ram[44] = "0b10111101100001000011001110001110";
        ram[45] = "0b10111110000100100110110010001001";
        ram[46] = "0b00111110001011001000010110111011";
        ram[47] = "0b00111110000011101101001010110110";
        ram[48] = "0b10111101001110000101011000010000";
        ram[49] = "0b00111100011101110010100001100100";
        ram[50] = "0b00111110011010000010110111111100";
        ram[51] = "0b10111101100100110011111011001101";
        ram[52] = "0b00111101001001001000110000100011";
        ram[53] = "0b00111101110100001110111000001100";
        ram[54] = "0b00111101100001010101001110100000";
        ram[55] = "0b00111101001101000111100111001011";
        ram[56] = "0b00111110001001100000011101010000";
        ram[57] = "0b10111110010101110011100010000001";
        ram[58] = "0b10111110001100010000110100110011";
        ram[59] = "0b10111110000010010010010110001111";
        ram[60] = "0b10111110010101011100000110101001";
        ram[61] = "0b10111100101100100011101000100100";
        ram[62] = "0b10111110001111100011000000110011";
        ram[63] = "0b00111101101110011111100011011101";
        ram[64] = "0b00111101111100110001101101011010";
        ram[65] = "0b00111110011100001111011110000010";
        ram[66] = "0b10111101011001000101011001111101";
        ram[67] = "0b10111100111110110101100111011110";
        ram[68] = "0b10111110100001010011010010111001";
        ram[69] = "0b10111101010000110110011001111010";
        ram[70] = "0b10111101101011101001101000111010";
        ram[71] = "0b10111101100110010101110000001000";
        ram[72] = "0b00111110000000011111100000001110";
        ram[73] = "0b00111011100100001011111010100100";
        ram[74] = "0b10111101101110000110010100110000";
        ram[75] = "0b10111110001111010101000001111000";
        ram[76] = "0b10111101110011010110000011100111";
        ram[77] = "0b10111101011000000010001010000010";
        ram[78] = "0b00111100100100001111011010111001";
        ram[79] = "0b10111110001101010110101100011000";
        ram[80] = "0b00111100110011101011100101101000";
        ram[81] = "0b10111100111011101010001000100110";
        ram[82] = "0b10111101111100100000101100110000";
        ram[83] = "0b10111101011010001000001001101100";
        ram[84] = "0b00111101000010111110110101100101";
        ram[85] = "0b10111110001010101101010001111000";
        ram[86] = "0b00111011010111010100000110001111";
        ram[87] = "0b10111110100000111101010110101001";
        ram[88] = "0b10111110010001000101110010011001";
        ram[89] = "0b10111101111110001011010101110000";
        ram[90] = "0b10111100101111111110000101000001";
        ram[91] = "0b00111101011001111110101000100011";
        ram[92] = "0b10111101101100011011110111000010";
        ram[93] = "0b00111110010001110111001011101100";
        ram[94] = "0b10111101101110001010001011110000";
        ram[95] = "0b10111101111001010001110110111011";
        ram[96] = "0b10111110001010011011110101011111";
        ram[97] = "0b00111110010100001000100010010110";
        ram[98] = "0b10111101110000001010001010110101";
        ram[99] = "0b10111110011101000001000010000100";
        ram[100] = "0b00111101000101111011100001101101";
        ram[101] = "0b00111101100001110101011101000010";
        ram[102] = "0b00111101111000010010010100010110";
        ram[103] = "0b10111101001111100100001011100000";
        ram[104] = "0b10111110100010000000111000100101";
        ram[105] = "0b10111110000000000000001110011000";
        ram[106] = "0b10111101000100011101001010000010";
        ram[107] = "0b10111101010111110100110111001000";
        ram[108] = "0b00111011011010101000001001010111";
        ram[109] = "0b10111101110101101111011110100100";
        ram[110] = "0b10111110000111000001001000110010";
        ram[111] = "0b00111110001010011010111101110000";
        ram[112] = "0b10111101111100000111001111111111";
        ram[113] = "0b10111100111001001010011010100111";
        ram[114] = "0b00111110010001010100100001000101";
        ram[115] = "0b10111101010111110001011010110001";
        ram[116] = "0b00111110001011110000111111101100";
        ram[117] = "0b00111101110101011110000001001101";
        ram[118] = "0b10111110010000000001100010010110";
        ram[119] = "0b10111100111110110001010010100000";
        ram[120] = "0b10111110011010100011101000010110";
        ram[121] = "0b10111101100011001110111100100001";
        ram[122] = "0b10111101001011000101100100100011";
        ram[123] = "0b10111110000111011110111101111110";
        ram[124] = "0b10111101100111100000000100011100";
        ram[125] = "0b00111110011011010100101101010100";
        ram[126] = "0b00111101100010100010100001111001";
        ram[127] = "0b00111011100101101000110011011111";
        ram[128] = "0b00111101010100011100011100111010";
        ram[129] = "0b00111101000000110001001000011010";
        ram[130] = "0b10111101100101001000111100111011";
        ram[131] = "0b00111101100101101001110111011111";
        ram[132] = "0b10111101100011111100001101111111";
        ram[133] = "0b10111101110000100100100100000100";
        ram[134] = "0b00111110010101101001011011101111";
        ram[135] = "0b00111101000110000011101011010101";
        ram[136] = "0b00111110001101100010001101110001";
        ram[137] = "0b00111110010011011111101000011100";
        ram[138] = "0b00111110100000111101110010010011";
        ram[139] = "0b10111110001000011110111001001111";
        ram[140] = "0b10111101101110011111001110011001";
        ram[141] = "0b00111110010000111110010001001101";
        ram[142] = "0b10111011011000100111010000100100";
        ram[143] = "0b10111110000100001101010010110110";
        ram[144] = "0b10111101010000100101001010010100";
        ram[145] = "0b00111101011000101011011011110010";
        ram[146] = "0b00111110001010110100000010101111";
        ram[147] = "0b10111110001101110111010010001111";
        ram[148] = "0b00111110001000100010101000110011";
        ram[149] = "0b00111101011010110101010011001000";
        ram[150] = "0b00111110010011001101000000010101";
        ram[151] = "0b00111101100111011111010111100110";
        ram[152] = "0b10111110000101000001110011111000";
        ram[153] = "0b00111101111000000110010000110101";
        ram[154] = "0b10111100001001010010010101010010";
        ram[155] = "0b10111110001001110100001010101101";
        ram[156] = "0b00111110011100100010110110111100";
        ram[157] = "0b00111100111101110110111000100110";
        ram[158] = "0b10111110010110001101010000101101";
        ram[159] = "0b10111110010001111010010001000011";
        ram[160] = "0b00111101101101010111010000110101";
        ram[161] = "0b10111110011100001111011010000011";
        ram[162] = "0b00111010111110011111011111001110";
        ram[163] = "0b00111110001100110011010010000000";
        ram[164] = "0b10111100110001100000100001001100";
        ram[165] = "0b00111101011001011101111000101110";
        ram[166] = "0b00111100100100100110011101110010";
        ram[167] = "0b00111010000111000110100111010001";
        ram[168] = "0b00111101110110001101110000111001";
        ram[169] = "0b00111110001000010010001111010101";
        ram[170] = "0b10111101111100101001110000010110";
        ram[171] = "0b00111110001100011110101000111011";


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


SC_MODULE(myip_v1_0_HLS_weieOg) {


static const unsigned DataWidth = 32;
static const unsigned AddressRange = 172;
static const unsigned AddressWidth = 8;

sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in<sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


myip_v1_0_HLS_weieOg_ram* meminst;


SC_CTOR(myip_v1_0_HLS_weieOg) {
meminst = new myip_v1_0_HLS_weieOg_ram("myip_v1_0_HLS_weieOg_ram");
meminst->address0(address0);
meminst->ce0(ce0);
meminst->q0(q0);

meminst->reset(reset);
meminst->clk(clk);
}
~myip_v1_0_HLS_weieOg() {
    delete meminst;
}


};//endmodule
#endif