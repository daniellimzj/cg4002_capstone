-- ==============================================================
-- Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
-- Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
-- ==============================================================
library ieee; 
use ieee.std_logic_1164.all; 
use ieee.std_logic_unsigned.all;

entity myip_v1_0_HLS_weiyd2_rom is 
    generic(
             DWIDTH     : integer := 32; 
             AWIDTH     : integer := 8; 
             MEM_SIZE    : integer := 172
    ); 
    port (
          addr0      : in std_logic_vector(AWIDTH-1 downto 0); 
          ce0       : in std_logic; 
          q0         : out std_logic_vector(DWIDTH-1 downto 0);
          clk       : in std_logic
    ); 
end entity; 


architecture rtl of myip_v1_0_HLS_weiyd2_rom is 

signal addr0_tmp : std_logic_vector(AWIDTH-1 downto 0); 
type mem_array is array (0 to MEM_SIZE-1) of std_logic_vector (DWIDTH-1 downto 0); 
signal mem : mem_array := (
    0 => "00111101001000100010010100110101", 
    1 => "10111100110101011001000111000111", 
    2 => "10111101100110011100001100010101", 
    3 => "10111101110110110001011101101110", 
    4 => "00111110001110011101011001111001", 
    5 => "00111101101100100000111000010111", 
    6 => "10111110001001110011111010001100", 
    7 => "00111101010011011011111101101111", 
    8 => "00111110000000010110111101101001", 
    9 => "00111101001001010000000010011001", 
    10 => "10111100101010000111001101000101", 
    11 => "10111101000000110111000111011001", 
    12 => "10111100111011001101100000111011", 
    13 => "00111101110010110000100100101000", 
    14 => "10111100100100001100010110001000", 
    15 => "10111110011000111000110100111001", 
    16 => "10111101101010110010011010010110", 
    17 => "10111110100111101100011111100101", 
    18 => "00111100010100101001010000111111", 
    19 => "10111110011100100100000000101111", 
    20 => "10111110100001000010010001110110", 
    21 => "10111100110011010111100101101001", 
    22 => "00111101101111011111110110111111", 
    23 => "00111101001000101010011100011101", 
    24 => "00111110001110110010110110000100", 
    25 => "10111110000010010010011100011010", 
    26 => "00111101111001000111100011100011", 
    27 => "10111101110110101110011011101000", 
    28 => "00111101111001010101101110100110", 
    29 => "00111110010000100110011110000101", 
    30 => "10111101100000010000010000010100", 
    31 => "00111100001010010000010100101010", 
    32 => "10111110001000101001000101010000", 
    33 => "10111110000110100111011011010110", 
    34 => "10111101111100110101000010000000", 
    35 => "10111101111111001101010001010001", 
    36 => "10111110000101000010101111100110", 
    37 => "00111110010110010011010011110011", 
    38 => "00111100110000011000111110100101", 
    39 => "00111100100011001111001101101000", 
    40 => "00111101101100000100000001000001", 
    41 => "10111101100000000001011100000111", 
    42 => "00111110001111111111000001011110", 
    43 => "10111101101100011011101100100011", 
    44 => "10111110010011011000101100110110", 
    45 => "00111101010110011000111101000000", 
    46 => "10111101101000011011111010110001", 
    47 => "10111101001111001100101100000111", 
    48 => "10111101101100100000011011010001", 
    49 => "00111110001110100101000111000111", 
    50 => "10111100101010000101001000001101", 
    51 => "10111101001001011010000011010110", 
    52 => "10111110011110010010100101101111", 
    53 => "10111110001001011011111111011110", 
    54 => "10111101111000011100101011100010", 
    55 => "00111110011111011101010011000100", 
    56 => "10111110011010000000000000111010", 
    57 => "10111101111100011111110010110110", 
    58 => "00111110010100011110000011111001", 
    59 => "00111110001001011001111101000111", 
    60 => "10111110100101001110100101101111", 
    61 => "00111101100000100100110111011110", 
    62 => "10111110000010111010010000100010", 
    63 => "00111110011010001010100001010110", 
    64 => "00111101000010000000000001001001", 
    65 => "10111110010100001110001011111000", 
    66 => "00111110100000100101000111101111", 
    67 => "10111101101010001111110100110100", 
    68 => "00111101101001111010111100101100", 
    69 => "00111100011111000000110101100000", 
    70 => "10111101001111010011110100100001", 
    71 => "00111100111100111010001100111010", 
    72 => "00111101100111000001111010011000", 
    73 => "10111011101001011010011100000100", 
    74 => "10111110100000000001111000100100", 
    75 => "00111110110100001001011100000100", 
    76 => "10111101010101010111111001001110", 
    77 => "00111100101101100101101111101010", 
    78 => "10111100110001000001001100011010", 
    79 => "00111101101000100100010000001001", 
    80 => "00111101100110111100100001101011", 
    81 => "00111101011001010111010010110000", 
    82 => "10111110101000010001111100101000", 
    83 => "10111110011110000011010110111011", 
    84 => "10111101111101100101011111110011", 
    85 => "10111101110101001011101110111000", 
    86 => "10111110101010010101100000101010", 
    87 => "10111110100010000110110110100010", 
    88 => "00111110001111111000111110010011", 
    89 => "00111101001111000100111111110001", 
    90 => "00111110010011000101110111100101", 
    91 => "10111110001010010110110000100100", 
    92 => "10111101100010000111101111100010", 
    93 => "00111101110010101110010001100100", 
    94 => "10111101110111100110001010010111", 
    95 => "00111101100110101001001101110100", 
    96 => "10111110011001001000011001001100", 
    97 => "00111110100000000011001101111001", 
    98 => "10111101100110100010110111000110", 
    99 => "00111100011011000110111010010111", 
    100 => "00111101001101000110111000110100", 
    101 => "00111101100010111100000101000101", 
    102 => "10111110010010010100010001101110", 
    103 => "10111110100111100110100110110010", 
    104 => "10111101001110010001100010010010", 
    105 => "00111110100000000010100110110011", 
    106 => "00111101011011100010001000010100", 
    107 => "00111101111001111001000111110001", 
    108 => "10111110010000001010001100011010", 
    109 => "10111101010011000010000011000101", 
    110 => "10111101001111100011011010001111", 
    111 => "00111110100101001010000110111110", 
    112 => "10111101000111100111100111101001", 
    113 => "00111110000000101000001110111011", 
    114 => "10111100101100111110111000100101", 
    115 => "00111101010011011100001111101111", 
    116 => "00111101001110101111101111001101", 
    117 => "10111101110100111011011011111101", 
    118 => "10111101000110110010001101011011", 
    119 => "10111101011111110011000000111010", 
    120 => "10111100110000000110010111111101", 
    121 => "10111110001000010110011110101011", 
    122 => "10111100111010101100000110011000", 
    123 => "10111101100101111011101101111011", 
    124 => "00111110000101110111111010010101", 
    125 => "10111110010110111010001001011001", 
    126 => "10111101110010001100011011100001", 
    127 => "00111110001000000000000100100100", 
    128 => "10111100110101111000101000010101", 
    129 => "00111110000001101011010111100011", 
    130 => "00111110000100011101111001110111", 
    131 => "10111101111000011011101110010001", 
    132 => "10111100000011110000100011110011", 
    133 => "10111110000110101111111111000100", 
    134 => "00111101110001001111001001110101", 
    135 => "10111110010001011010101010101111", 
    136 => "10111101101001011101111111110111", 
    137 => "10111110011000000000100011001111", 
    138 => "00111101110110101001000010101111", 
    139 => "10111110001000011100011101000111", 
    140 => "00111110000100001111011011011110", 
    141 => "00111011111100100111110111001010", 
    142 => "10111101101010110011000010100111", 
    143 => "10111101101011011111010010100011", 
    144 => "10111101101011111000110000011000", 
    145 => "00111110000001111011011000100000", 
    146 => "10111101111001100001000001010010", 
    147 => "00111110001010100101001001011101", 
    148 => "00111100101110001110010110111010", 
    149 => "00111110011011000001000100101100", 
    150 => "00111101111010111000101000111101", 
    151 => "10111101100100011101011001101001", 
    152 => "00111110000101100000101101110011", 
    153 => "10111101011010011100010111010111", 
    154 => "10111100101010001011000100001100", 
    155 => "10111110010100000111111010000011", 
    156 => "10111101001010111000011011100000", 
    157 => "10111101111011110110110010110110", 
    158 => "10111101011011000011111001000100", 
    159 => "00111110000110111000001000101100", 
    160 => "10111100111110101111001111110110", 
    161 => "00111101101001000010101000110010", 
    162 => "10111101011011101000000000000001", 
    163 => "10111110000111110101011001001111", 
    164 => "00111101010000001111001110111011", 
    165 => "00111110100111111000001000010100", 
    166 => "00111100010011100111111101111101", 
    167 => "10111101010100010001100000000010", 
    168 => "00111110000010010101100010111010", 
    169 => "00111100000011000010001001001110", 
    170 => "10111110000000010000111000101010", 
    171 => "10111110100101011100001101001010" );


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

entity myip_v1_0_HLS_weiyd2 is
    generic (
        DataWidth : INTEGER := 32;
        AddressRange : INTEGER := 172;
        AddressWidth : INTEGER := 8);
    port (
        reset : IN STD_LOGIC;
        clk : IN STD_LOGIC;
        address0 : IN STD_LOGIC_VECTOR(AddressWidth - 1 DOWNTO 0);
        ce0 : IN STD_LOGIC;
        q0 : OUT STD_LOGIC_VECTOR(DataWidth - 1 DOWNTO 0));
end entity;

architecture arch of myip_v1_0_HLS_weiyd2 is
    component myip_v1_0_HLS_weiyd2_rom is
        port (
            clk : IN STD_LOGIC;
            addr0 : IN STD_LOGIC_VECTOR;
            ce0 : IN STD_LOGIC;
            q0 : OUT STD_LOGIC_VECTOR);
    end component;



begin
    myip_v1_0_HLS_weiyd2_rom_U :  component myip_v1_0_HLS_weiyd2_rom
    port map (
        clk => clk,
        addr0 => address0,
        ce0 => ce0,
        q0 => q0);

end architecture;

