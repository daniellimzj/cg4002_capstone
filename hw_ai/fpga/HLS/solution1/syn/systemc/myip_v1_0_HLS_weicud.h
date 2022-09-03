// ==============================================================
// Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
// Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
// ==============================================================
#ifndef __myip_v1_0_HLS_weicud_H__
#define __myip_v1_0_HLS_weicud_H__


#include <systemc>
using namespace sc_core;
using namespace sc_dt;




#include <iostream>
#include <fstream>

struct myip_v1_0_HLS_weicud_ram : public sc_core::sc_module {

  static const unsigned DataWidth = 32;
  static const unsigned AddressRange = 30;
  static const unsigned AddressWidth = 5;

//latency = 1
//input_reg = 1
//output_reg = 0
sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in <sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


sc_lv<DataWidth> ram[AddressRange];


   SC_CTOR(myip_v1_0_HLS_weicud_ram) {
        ram[0] = "0b10111111110101101100000111101111";
        ram[1] = "0b00111110110111101001001011110110";
        ram[2] = "0b10111111100100001010000100001001";
        ram[3] = "0b10111111101010000111010010100000";
        ram[4] = "0b11000000000001001010010000111100";
        ram[5] = "0b01000000101000010000001100001001";
        ram[6] = "0b10111110111101000110100101011000";
        ram[7] = "0b01000000001001010010100111010000";
        ram[8] = "0b01000000100010010000011110010010";
        ram[9] = "0b10111101001011011001000100010001";
        ram[10] = "0b11000000001100111100101100110110";
        ram[11] = "0b10111111101010000101101001110101";
        ram[12] = "0b10111111100000001100111010111111";
        ram[13] = "0b11000000001000101100010010101100";
        ram[14] = "0b01000000000001111011001001111000";
        ram[15] = "0b01000000100111110011011101110110";
        ram[16] = "0b10111111100100001001011001100101";
        ram[17] = "0b10111111100101110010100111000111";
        ram[18] = "0b00111111110100011110011001010110";
        ram[19] = "0b00111110111001011110100101100001";
        ram[20] = "0b00111111101101011000011011100101";
        ram[21] = "0b00111110011001101010100011010101";
        ram[22] = "0b11000000001001011100110001101000";
        ram[23] = "0b10111111001101011110111001000011";
        ram[24] = "0b00111111011101001111101010010000";
        ram[25] = "0b00111111101111000100001100100011";
        ram[26] = "0b11000000100000010001101101010101";
        ram[27] = "0b01000000001000101111011111101010";
        ram[28] = "0b10111110101101010111011110010000";
        ram[29] = "0b00111111000011101110111100110100";


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


SC_MODULE(myip_v1_0_HLS_weicud) {


static const unsigned DataWidth = 32;
static const unsigned AddressRange = 30;
static const unsigned AddressWidth = 5;

sc_core::sc_in <sc_lv<AddressWidth> > address0;
sc_core::sc_in<sc_logic> ce0;
sc_core::sc_out <sc_lv<DataWidth> > q0;
sc_core::sc_in<sc_logic> reset;
sc_core::sc_in<bool> clk;


myip_v1_0_HLS_weicud_ram* meminst;


SC_CTOR(myip_v1_0_HLS_weicud) {
meminst = new myip_v1_0_HLS_weicud_ram("myip_v1_0_HLS_weicud_ram");
meminst->address0(address0);
meminst->ce0(ce0);
meminst->q0(q0);

meminst->reset(reset);
meminst->clk(clk);
}
~myip_v1_0_HLS_weicud() {
    delete meminst;
}


};//endmodule
#endif
