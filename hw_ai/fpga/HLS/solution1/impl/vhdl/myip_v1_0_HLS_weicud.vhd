-- ==============================================================
-- Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
-- Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
-- ==============================================================
library ieee; 
use ieee.std_logic_1164.all; 
use ieee.std_logic_unsigned.all;

entity myip_v1_0_HLS_weicud_rom is 
    generic(
             DWIDTH     : integer := 32; 
             AWIDTH     : integer := 5; 
             MEM_SIZE    : integer := 30
    ); 
    port (
          addr0      : in std_logic_vector(AWIDTH-1 downto 0); 
          ce0       : in std_logic; 
          q0         : out std_logic_vector(DWIDTH-1 downto 0);
          clk       : in std_logic
    ); 
end entity; 


architecture rtl of myip_v1_0_HLS_weicud_rom is 

signal addr0_tmp : std_logic_vector(AWIDTH-1 downto 0); 
type mem_array is array (0 to MEM_SIZE-1) of std_logic_vector (DWIDTH-1 downto 0); 
signal mem : mem_array := (
    0 => "10111111110101101100000111101111", 
    1 => "00111110110111101001001011110110", 
    2 => "10111111100100001010000100001001", 
    3 => "10111111101010000111010010100000", 
    4 => "11000000000001001010010000111100", 
    5 => "01000000101000010000001100001001", 
    6 => "10111110111101000110100101011000", 
    7 => "01000000001001010010100111010000", 
    8 => "01000000100010010000011110010010", 
    9 => "10111101001011011001000100010001", 
    10 => "11000000001100111100101100110110", 
    11 => "10111111101010000101101001110101", 
    12 => "10111111100000001100111010111111", 
    13 => "11000000001000101100010010101100", 
    14 => "01000000000001111011001001111000", 
    15 => "01000000100111110011011101110110", 
    16 => "10111111100100001001011001100101", 
    17 => "10111111100101110010100111000111", 
    18 => "00111111110100011110011001010110", 
    19 => "00111110111001011110100101100001", 
    20 => "00111111101101011000011011100101", 
    21 => "00111110011001101010100011010101", 
    22 => "11000000001001011100110001101000", 
    23 => "10111111001101011110111001000011", 
    24 => "00111111011101001111101010010000", 
    25 => "00111111101111000100001100100011", 
    26 => "11000000100000010001101101010101", 
    27 => "01000000001000101111011111101010", 
    28 => "10111110101101010111011110010000", 
    29 => "00111111000011101110111100110100" );

attribute syn_rom_style : string;
attribute syn_rom_style of mem : signal is "select_rom";
attribute ROM_STYLE : string;
attribute ROM_STYLE of mem : signal is "distributed";

begin 


memory_access_guard_0: process (addr0) 
begin
      addr0_tmp <= addr0;
--synthesis translate_off
      if (CONV_INTEGER(addr0) > mem_size-1) then
           addr0_tmp <= (others => '0');
      else 
           addr0_tmp <= addr0;
      end if;
--synthesis translate_on
end process;

p_rom_access: process (clk)  
begin 
    if (clk'event and clk = '1') then
        if (ce0 = '1') then 
            q0 <= mem(CONV_INTEGER(addr0_tmp)); 
        end if;
    end if;
end process;

end rtl;

Library IEEE;
use IEEE.std_logic_1164.all;

entity myip_v1_0_HLS_weicud is
    generic (
        DataWidth : INTEGER := 32;
        AddressRange : INTEGER := 30;
        AddressWidth : INTEGER := 5);
    port (
        reset : IN STD_LOGIC;
        clk : IN STD_LOGIC;
        address0 : IN STD_LOGIC_VECTOR(AddressWidth - 1 DOWNTO 0);
        ce0 : IN STD_LOGIC;
        q0 : OUT STD_LOGIC_VECTOR(DataWidth - 1 DOWNTO 0));
end entity;

architecture arch of myip_v1_0_HLS_weicud is
    component myip_v1_0_HLS_weicud_rom is
        port (
            clk : IN STD_LOGIC;
            addr0 : IN STD_LOGIC_VECTOR;
            ce0 : IN STD_LOGIC;
            q0 : OUT STD_LOGIC_VECTOR);
    end component;



begin
    myip_v1_0_HLS_weicud_rom_U :  component myip_v1_0_HLS_weicud_rom
    port map (
        clk => clk,
        addr0 => address0,
        ce0 => ce0,
        q0 => q0);

end architecture;


