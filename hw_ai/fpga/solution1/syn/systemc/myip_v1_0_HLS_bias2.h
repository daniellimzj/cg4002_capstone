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
  static const unsigned AddressRange = 5;
  static const unsigned AddressWidth = 3;

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
        ram[0] = "0b10111110000100101111101101110001";
        ram[1] = "0b10111100101111011100101011010110";
        ram[2] = "0b10111100111011111110101010000011";
        ram[3] = "0b00111110001000110101110110010101";
        ram[4] = "0b10111110010011000000010000000010";


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
static const unsigned AddressRange = 5;
static const unsigned AddressWidth = 3;

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
