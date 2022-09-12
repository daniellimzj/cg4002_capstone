// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __myip_v1_0_HLS_bias2_H__
#define __myip_v1_0_HLS_bias2_H__


#include <systemc>
using namespace sc_core;
using namespace sc_dt;




#include <iostream>
#include <fstream>

struct myip_v1_0_HLS_bias2_ram : public sc_core::sc_module {

  static const unsigned DataWidth = 32;
  static const unsigned AddressRange = 50;
  static const unsigned AddressWidth = 6;

//latency = 1
//input_reg = 1
//output_reg = 0
sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in <sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


sc_lv<DataWidth> ram[AddressRange];


   SC_CTOR(myip_v1_0_HLS_bias2_ram) {
        ram[0] = "0b00111101110011000100100110000000";
        ram[1] = "0b00111101010000010011110010111101";
        ram[2] = "0b10111101010011101011000011000011";
        ram[3] = "0b00111110001111101011111101100111";
        ram[4] = "0b10111110100101101111101111111000";
        ram[5] = "0b10111110101001100011000001111010";
        ram[6] = "0b00111110110000101110110011100111";
        ram[7] = "0b10111101011000101010000010101101";
        ram[8] = "0b00111100101001100001001001100100";
        ram[9] = "0b00111101010011100101010111100010";
        ram[10] = "0b10111110010101111101100010000010";
        ram[11] = "0b10111110001101100001001000111010";
        ram[12] = "0b10111110011111111000010100100111";
        ram[13] = "0b10111110110000100001010110010000";
        ram[14] = "0b10111110010010010100000010100011";
        ram[15] = "0b10111110001100001101110010100111";
        ram[16] = "0b00111110100111010000001111100010";
        ram[17] = "0b10111100100001111101100101111101";
        ram[18] = "0b00111110111111110000100111101101";
        ram[19] = "0b10111110000000011011111101101011";
        ram[20] = "0b00111101111011011100001100010000";
        ram[21] = "0b10111101101110001001110000010110";
        ram[22] = "0b10111101110000110000100110011011";
        ram[23] = "0b10111011001011101101011111000011";
        ram[24] = "0b00111110011111001110111101110111";
        ram[25] = "0b10111110101110001000101100000101";
        ram[26] = "0b00111101111010111100010101110011";
        ram[27] = "0b00111110111000000100111000100001";
        ram[28] = "0b10111110101001110110011100110001";
        ram[29] = "0b00111110010110111111101100010011";
        ram[30] = "0b10111110100110011010011001101000";
        ram[31] = "0b00111110000000001011110100011100";
        ram[32] = "0b00111110001101001011110100011101";
        ram[33] = "0b00111101000100110010011000001110";
        ram[34] = "0b00111011111111001111100000111010";
        ram[35] = "0b00111101110110110110100111011101";
        ram[36] = "0b10111110100001010011010000011101";
        ram[37] = "0b00111110101100011110101111101010";
        ram[38] = "0b10111110100110110000011001000101";
        ram[39] = "0b10111101000010001010001001010111";
        ram[40] = "0b00111101011011011000111110101010";
        ram[41] = "0b00111010010111110011101001100100";
        ram[42] = "0b10111110011101010010100101100011";
        ram[43] = "0b10111110011101111111011000000000";
        ram[44] = "0b10111110100011111001100000000000";
        ram[45] = "0b00111101111010100001101000101000";
        ram[46] = "0b00111101111101010110110111100011";
        ram[47] = "0b00111110011100100110011010101100";
        ram[48] = "0b00111101111100111010010101001011";
        ram[49] = "0b00111101110000110010001010001110";


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


SC_MODULE(myip_v1_0_HLS_bias2) {


static const unsigned DataWidth = 32;
static const unsigned AddressRange = 50;
static const unsigned AddressWidth = 6;

sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in<sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


myip_v1_0_HLS_bias2_ram* meminst;


SC_CTOR(myip_v1_0_HLS_bias2) {
meminst = new myip_v1_0_HLS_bias2_ram("myip_v1_0_HLS_bias2_ram");
meminst->address0(address0);
meminst->ce0(ce0);
meminst->q0(q0);

meminst->reset(reset);
meminst->clk(clk);
}
~myip_v1_0_HLS_bias2() {
    delete meminst;
}


};//endmodule
#endif
