-- ==============================================================
-- Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
-- Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
-- ==============================================================
library ieee; 
use ieee.std_logic_1164.all; 
use ieee.std_logic_unsigned.all;

entity myip_v1_0_HLS_bias1_rom is 
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


architecture rtl of myip_v1_0_HLS_bias1_rom is 

signal addr0_tmp : std_logic_vector(AWIDTH-1 downto 0); 
type mem_array is array (0 to MEM_SIZE-1) of std_logic_vector (DWIDTH-1 downto 0); 
signal mem : mem_array := (
    0 => "00111100001001000110001001000111", 
    1 => "10111110000011101010001101010100", 
    2 => "10111101111110100100011011111010", 
    3 => "00111100111111011110001111010110", 
    4 => "10111101111011011111101101010101", 
    5 => "00111101010001010101100010001111", 
    6 => "00111111000000111110001110110001", 
    7 => "00111110110110110101110000101111", 
    8 => "00111101101110001001000111011110", 
    9 => "00111111000000100101110100100100", 
    10 => "10111111001001101010101001111101", 
    11 => "10111100111100000011000110010000", 
    12 => "10111111000000110110001111011000", 
    13 => "00111111011010010010000110110000", 
    14 => "00111101010000100000111000011101", 
    15 => "00111110111110111111111100011101", 
    16 => "00111110100111111100100001011011", 
    17 => "00111101101011111001111011000011", 
    18 => "00111110111101000100111011011010", 
    19 => "00111101110110001001000000000111", 
    20 => "10111101101111010011000100011010", 
    21 => "00111101100001000001001110100011", 
    22 => "00111111000001110111110000110100", 
    23 => "10111111011000100101110110100100", 
    24 => "10111110110101101010000011011000", 
    25 => "00111110110111010110111011100100", 
    26 => "00111111000010101000111001101011", 
    27 => "00111111000101001110101000001100", 
    28 => "10111101001111111011111111011011", 
    29 => "10111110001100101100001111001010", 
    30 => "10111110101100010100100000001000", 
    31 => "00111110011110001101001110000000", 
    32 => "10111110110010010101011100110000", 
    33 => "10111110110110011000111100011101", 
    34 => "10111110010001011111100010101010", 
    35 => "00111110010111110111110111100000", 
    36 => "10111110110001010000010011011011", 
    37 => "10111110010000000111011001011000", 
    38 => "10111110001011100101000110000110", 
    39 => "10111110100000010100110100110000", 
    40 => "00111110100011111111000101101111", 
    41 => "10111110001011001001001011101111", 
    42 => "00111110100000000010101110111010", 
    43 => "10111110001110111011001010000001", 
    44 => "00111101111101110001110111111000", 
    45 => "10111110010110011111110110111111", 
    46 => "10111110010000011011111110001110", 
    47 => "10111110111011010010010111110100", 
    48 => "10111111011100100111110101001101", 
    49 => "00111110110100001010100011100111" );


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

entity myip_v1_0_HLS_bias1 is
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

architecture arch of myip_v1_0_HLS_bias1 is
    component myip_v1_0_HLS_bias1_rom is
        port (
            clk : IN STD_LOGIC;
            addr0 : IN STD_LOGIC_VECTOR;
            ce0 : IN STD_LOGIC;
            q0 : OUT STD_LOGIC_VECTOR);
    end component;



begin
    myip_v1_0_HLS_bias1_rom_U :  component myip_v1_0_HLS_bias1_rom
    port map (
        clk => clk,
        addr0 => address0,
        ce0 => ce0,
        q0 => q0);

end architecture;


