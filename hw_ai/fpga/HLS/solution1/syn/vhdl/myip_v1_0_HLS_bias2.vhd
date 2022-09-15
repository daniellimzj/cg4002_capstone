-- ==============================================================
-- Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
-- Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
-- ==============================================================
library ieee; 
use ieee.std_logic_1164.all; 
use ieee.std_logic_unsigned.all;

entity myip_v1_0_HLS_bias2_rom is 
    generic(
             DWIDTH     : integer := 32; 
             AWIDTH     : integer := 6; 
             MEM_SIZE    : integer := 50
    ); 
    port (
          addr0      : in std_logic_vector(AWIDTH-1 downto 0); 
          ce0       : in std_logic; 
          q0         : out std_logic_vector(DWIDTH-1 downto 0);
          clk       : in std_logic
    ); 
end entity; 


architecture rtl of myip_v1_0_HLS_bias2_rom is 

signal addr0_tmp : std_logic_vector(AWIDTH-1 downto 0); 
type mem_array is array (0 to MEM_SIZE-1) of std_logic_vector (DWIDTH-1 downto 0); 
signal mem : mem_array := (
    0 => "00111101110011000100100110000000", 
    1 => "00111101010000010011110010111101", 
    2 => "10111101010011101011000011000011", 
    3 => "00111110001111101011111101100111", 
    4 => "10111110100101101111101111111000", 
    5 => "10111110101001100011000001111010", 
    6 => "00111110110000101110110011100111", 
    7 => "10111101011000101010000010101101", 
    8 => "00111100101001100001001001100100", 
    9 => "00111101010011100101010111100010", 
    10 => "10111110010101111101100010000010", 
    11 => "10111110001101100001001000111010", 
    12 => "10111110011111111000010100100111", 
    13 => "10111110110000100001010110010000", 
    14 => "10111110010010010100000010100011", 
    15 => "10111110001100001101110010100111", 
    16 => "00111110100111010000001111100010", 
    17 => "10111100100001111101100101111101", 
    18 => "00111110111111110000100111101101", 
    19 => "10111110000000011011111101101011", 
    20 => "00111101111011011100001100010000", 
    21 => "10111101101110001001110000010110", 
    22 => "10111101110000110000100110011011", 
    23 => "10111011001011101101011111000011", 
    24 => "00111110011111001110111101110111", 
    25 => "10111110101110001000101100000101", 
    26 => "00111101111010111100010101110011", 
    27 => "00111110111000000100111000100001", 
    28 => "10111110101001110110011100110001", 
    29 => "00111110010110111111101100010011", 
    30 => "10111110100110011010011001101000", 
    31 => "00111110000000001011110100011100", 
    32 => "00111110001101001011110100011101", 
    33 => "00111101000100110010011000001110", 
    34 => "00111011111111001111100000111010", 
    35 => "00111101110110110110100111011101", 
    36 => "10111110100001010011010000011101", 
    37 => "00111110101100011110101111101010", 
    38 => "10111110100110110000011001000101", 
    39 => "10111101000010001010001001010111", 
    40 => "00111101011011011000111110101010", 
    41 => "00111010010111110011101001100100", 
    42 => "10111110011101010010100101100011", 
    43 => "10111110011101111111011000000000", 
    44 => "10111110100011111001100000000000", 
    45 => "00111101111010100001101000101000", 
    46 => "00111101111101010110110111100011", 
    47 => "00111110011100100110011010101100", 
    48 => "00111101111100111010010101001011", 
    49 => "00111101110000110010001010001110" );


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

entity myip_v1_0_HLS_bias2 is
    generic (
        DataWidth : INTEGER := 32;
        AddressRange : INTEGER := 50;
        AddressWidth : INTEGER := 6);
    port (
        reset : IN STD_LOGIC;
        clk : IN STD_LOGIC;
        address0 : IN STD_LOGIC_VECTOR(AddressWidth - 1 DOWNTO 0);
        ce0 : IN STD_LOGIC;
        q0 : OUT STD_LOGIC_VECTOR(DataWidth - 1 DOWNTO 0));
end entity;

architecture arch of myip_v1_0_HLS_bias2 is
    component myip_v1_0_HLS_bias2_rom is
        port (
            clk : IN STD_LOGIC;
            addr0 : IN STD_LOGIC_VECTOR;
            ce0 : IN STD_LOGIC;
            q0 : OUT STD_LOGIC_VECTOR);
    end component;



begin
    myip_v1_0_HLS_bias2_rom_U :  component myip_v1_0_HLS_bias2_rom
    port map (
        clk => clk,
        addr0 => address0,
        ce0 => ce0,
        q0 => q0);

end architecture;


