// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __myip_v1_0_HLS_bias1_H__
#define __myip_v1_0_HLS_bias1_H__


#include <systemc>
using namespace sc_core;
using namespace sc_dt;




#include <iostream>
#include <fstream>

struct myip_v1_0_HLS_bias1_ram : public sc_core::sc_module {

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


   SC_CTOR(myip_v1_0_HLS_bias1_ram) {
        ram[0] = "0b00111100001001000110001001000111";
        ram[1] = "0b10111110000011101010001101010100";
        ram[2] = "0b10111101111110100100011011111010";
        ram[3] = "0b00111100111111011110001111010110";
        ram[4] = "0b10111101111011011111101101010101";
        ram[5] = "0b00111101010001010101100010001111";
        ram[6] = "0b00111111000000111110001110110001";
        ram[7] = "0b00111110110110110101110000101111";
        ram[8] = "0b00111101101110001001000111011110";
        ram[9] = "0b00111111000000100101110100100100";
        ram[10] = "0b10111111001001101010101001111101";
        ram[11] = "0b10111100111100000011000110010000";
        ram[12] = "0b10111111000000110110001111011000";
        ram[13] = "0b00111111011010010010000110110000";
        ram[14] = "0b00111101010000100000111000011101";
        ram[15] = "0b00111110111110111111111100011101";
        ram[16] = "0b00111110100111111100100001011011";
        ram[17] = "0b00111101101011111001111011000011";
        ram[18] = "0b00111110111101000100111011011010";
        ram[19] = "0b00111101110110001001000000000111";
        ram[20] = "0b10111101101111010011000100011010";
        ram[21] = "0b00111101100001000001001110100011";
        ram[22] = "0b00111111000001110111110000110100";
        ram[23] = "0b10111111011000100101110110100100";
        ram[24] = "0b10111110110101101010000011011000";
        ram[25] = "0b00111110110111010110111011100100";
        ram[26] = "0b00111111000010101000111001101011";
        ram[27] = "0b00111111000101001110101000001100";
        ram[28] = "0b10111101001111111011111111011011";
        ram[29] = "0b10111110001100101100001111001010";
        ram[30] = "0b10111110101100010100100000001000";
        ram[31] = "0b00111110011110001101001110000000";
        ram[32] = "0b10111110110010010101011100110000";
        ram[33] = "0b10111110110110011000111100011101";
        ram[34] = "0b10111110010001011111100010101010";
        ram[35] = "0b00111110010111110111110111100000";
        ram[36] = "0b10111110110001010000010011011011";
        ram[37] = "0b10111110010000000111011001011000";
        ram[38] = "0b10111110001011100101000110000110";
        ram[39] = "0b10111110100000010100110100110000";
        ram[40] = "0b00111110100011111111000101101111";
        ram[41] = "0b10111110001011001001001011101111";
        ram[42] = "0b00111110100000000010101110111010";
        ram[43] = "0b10111110001110111011001010000001";
        ram[44] = "0b00111101111101110001110111111000";
        ram[45] = "0b10111110010110011111110110111111";
        ram[46] = "0b10111110010000011011111110001110";
        ram[47] = "0b10111110111011010010010111110100";
        ram[48] = "0b10111111011100100111110101001101";
        ram[49] = "0b00111110110100001010100011100111";


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


SC_MODULE(myip_v1_0_HLS_bias1) {


static const unsigned DataWidth = 32;
static const unsigned AddressRange = 50;
static const unsigned AddressWidth = 6;

sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in<sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


myip_v1_0_HLS_bias1_ram* meminst;


SC_CTOR(myip_v1_0_HLS_bias1) {
meminst = new myip_v1_0_HLS_bias1_ram("myip_v1_0_HLS_bias1_ram");
meminst->address0(address0);
meminst->ce0(ce0);
meminst->q0(q0);

meminst->reset(reset);
meminst->clk(clk);
}
~myip_v1_0_HLS_bias1() {
    delete meminst;
}


};//endmodule
#endif
