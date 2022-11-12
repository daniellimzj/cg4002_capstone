-- ==============================================================
-- Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
-- Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
-- ==============================================================
library ieee; 
use ieee.std_logic_1164.all; 
use ieee.std_logic_unsigned.all;

entity myip_v1_0_HLS_weiOgC_rom is 
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


architecture rtl of myip_v1_0_HLS_weiOgC_rom is 

signal addr0_tmp : std_logic_vector(AWIDTH-1 downto 0); 
type mem_array is array (0 to MEM_SIZE-1) of std_logic_vector (DWIDTH-1 downto 0); 
signal mem : mem_array := (
    0 => "10111110010001101010011011100100", 
    1 => "10111110001001010110001001001011", 
    2 => "00111101001111111000101100101100", 
    3 => "00111101010111010010001001011001", 
    4 => "00111101101011011011001010000010", 
    5 => "00111101000010110101001110111101", 
    6 => "10111101000100011010100011100001", 
    7 => "10111110000101001100111010110011", 
    8 => "10111101011001010000011000011100", 
    9 => "00111101110010001101011111111010", 
    10 => "00111101101000001000000000001010", 
    11 => "10111110010111001110101001110111", 
    12 => "00111110000100001001010101011110", 
    13 => "10111101101110000110111000111111", 
    14 => "10111110000010011001010001000001", 
    15 => "00111101100010000100010100111101", 
    16 => "00111110001110000110010110111010", 
    17 => "00111100110111001010110111100100", 
    18 => "00111101000010000100010101101011", 
    19 => "00111101010001010001100010111100", 
    20 => "10111101010001111011001100011010", 
    21 => "10111110010001101010001011011101", 
    22 => "00111110000010110100000110011111", 
    23 => "10111110000110111011001000100100", 
    24 => "00111110001101011101011101010000", 
    25 => "10111010101101011010110000110101", 
    26 => "00111110000111011101010001011110", 
    27 => "00111100111100111010011110000011", 
    28 => "10111110101010010100000111001100", 
    29 => "00111110011011010000100001111111", 
    30 => "10111101000110001001000010011011", 
    31 => "10111101011001011000110011010110", 
    32 => "00111101111000000011111000001100", 
    33 => "10111110001001011000001001110000", 
    34 => "10111101100001110100111111101000", 
    35 => "00111010101000110110011000100010", 
    36 => "10111101110110000000010001000000", 
    37 => "10111100101100000010001111000101", 
    38 => "00111101001011101100111110111110", 
    39 => "10111101110111110110000101110101", 
    40 => "10111101100101101100001101011101", 
    41 => "10111101101101011111011010111010", 
    42 => "10111101001100111000101110101101", 
    43 => "10111110010010111001110010101000", 
    44 => "00111101011001110001101101000111", 
    45 => "10111110000110111100100101111110", 
    46 => "00111101110001000010001011110100", 
    47 => "00111100110001010110001111110011", 
    48 => "00111011001010101111000110010000", 
    49 => "10111011110011100110000001110100", 
    50 => "00111101000110100101111001111110", 
    51 => "00111101110001001000000101011001", 
    52 => "10111110000000110010011111011001", 
    53 => "00111101001101101000000010100101", 
    54 => "00111101101000101110111110111110", 
    55 => "10111110011011000110101101110010", 
    56 => "10111101011100000101110000000101", 
    57 => "10111100100111100110111100001101", 
    58 => "10111110011110110100111000011000", 
    59 => "10111100100101110000101010001101", 
    60 => "10111110010101001101110110110100", 
    61 => "00111110000001001111011010000100", 
    62 => "00111101110000010001100010000100", 
    63 => "00111110100001100000011001111000", 
    64 => "10111101100100000111101001000100", 
    65 => "10111110000110110010001100111111", 
    66 => "00111101101101110110100001010100", 
    67 => "10111110000101011111011111100001", 
    68 => "00111011000000000000001010110001", 
    69 => "00111101101000001011100100000011", 
    70 => "10111101000100000010010111011111", 
    71 => "00111100111010110101011000011101", 
    72 => "10111101001011001011110001110100", 
    73 => "00111101010011000110010101000100", 
    74 => "10111101110001000010011001000100", 
    75 => "10111110100010100111101001101000", 
    76 => "10111110000011110000001101111011", 
    77 => "10111101000110110101110110001010", 
    78 => "00111101100010100101011101010000", 
    79 => "00111101000010011001110011010010", 
    80 => "10111101110001000011010010000100", 
    81 => "00111100101011011111000101011101", 
    82 => "00111110001010110100100001000001", 
    83 => "00111101100011110000001001100000", 
    84 => "00111101011100101011111000100011", 
    85 => "10111110010010110010110010100100", 
    86 => "10111110001011001110011100100101", 
    87 => "00111101101110001011000100110000", 
    88 => "10111110001111110100100111000011", 
    89 => "10111101010101100000010011010110", 
    90 => "10111100100010101000111101101111", 
    91 => "10111110000010100011101110110111", 
    92 => "10111011000110101000000000010110", 
    93 => "00111100100010001001111110010111", 
    94 => "00111101101001000101001011010111", 
    95 => "00111101111111010010100100101101", 
    96 => "00111101000110001100101110000100", 
    97 => "10111101010111001101001000011001", 
    98 => "00111110000010001101010011000110", 
    99 => "00111101101111101011000010101001", 
    100 => "00111110000010010010011100110100", 
    101 => "00111100100000001101110101101011", 
    102 => "10111101000000001111100110100000", 
    103 => "00111101101010110011101111011000", 
    104 => "00111110000011011100110010000110", 
    105 => "00111110000010011000111111111111", 
    106 => "10111101110010001101001101100011", 
    107 => "00111100111110000101000101100000", 
    108 => "00111101011000100010010001111010", 
    109 => "00111101110111000100111101001110", 
    110 => "00111101110000010101100001011101", 
    111 => "00111101110111111101010100011000", 
    112 => "10111101111000101110000001111010", 
    113 => "10111110000000010100111110010100", 
    114 => "10111100111100010101110110110110", 
    115 => "00111101000100000101111011000111", 
    116 => "00111110011101011010101011100110", 
    117 => "10111100110010000000000110011000", 
    118 => "00111101100001100010101001010110", 
    119 => "10111101111110110011110101110011", 
    120 => "10111101010000000000010011001011", 
    121 => "00111101001110001001000111111110", 
    122 => "10111101100011100000100000101000", 
    123 => "10111110101011101110001000000100", 
    124 => "10111101101100010001001000101110", 
    125 => "10111101100001011010010011011001", 
    126 => "00111101011001010110101011111111", 
    127 => "00111110000001011011101111111001", 
    128 => "00111101100111000010010111101000", 
    129 => "10111110011011010110000001001111", 
    130 => "00111110011101010001010100100000", 
    131 => "00111101101110000001111101001000", 
    132 => "10111101110111011110110010001110", 
    133 => "00111101011100010001010001101111", 
    134 => "00111101101011100000111011011001", 
    135 => "00111101001001111010100100100001", 
    136 => "10111101000100000010111110000111", 
    137 => "10111110001001111110101011011111", 
    138 => "10111101111001101011111000100011", 
    139 => "00111101110100011001011101111101", 
    140 => "10111110000100100001001101001111", 
    141 => "00111110001111010001010100001001", 
    142 => "10111001001010111000101100001000", 
    143 => "10111110001110111010010001100110", 
    144 => "10111101100010000000101011110011", 
    145 => "10111101000111100001111110111011", 
    146 => "00111101100010110011110111110010", 
    147 => "10111101001011110010010000100101", 
    148 => "10111101100000011001110111110011", 
    149 => "10111110001111100011011100100101", 
    150 => "00111110001010100011110110011111", 
    151 => "00111110001010111001110010110100", 
    152 => "10111101100111000111111111101000", 
    153 => "10111101100011100011110101000110", 
    154 => "00111101111110001010100010110111", 
    155 => "00111100000101001011001110111010", 
    156 => "00111101100001010111010000000000", 
    157 => "10111110011100100011001000101000", 
    158 => "00111101000010011100010010100110", 
    159 => "10111110000010001110000111111011", 
    160 => "00111110010100010010000100011101", 
    161 => "00111110110010100110110011101110", 
    162 => "00111101111111101101010111011011", 
    163 => "10111100000110011111101000110111", 
    164 => "00111110001100110000111111110110", 
    165 => "00111110010001101001000101110000", 
    166 => "10111110001001101101111011011100", 
    167 => "00111110010010110011111000110111", 
    168 => "00111110001001001100111001000101", 
    169 => "10111101110101000110101111101011", 
    170 => "00111110010110111110110000010111", 
    171 => "00111101011101010111011001100010" );


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

entity myip_v1_0_HLS_weiOgC is
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

architecture arch of myip_v1_0_HLS_weiOgC is
    component myip_v1_0_HLS_weiOgC_rom is
        port (
            clk : IN STD_LOGIC;
            addr0 : IN STD_LOGIC_VECTOR;
            ce0 : IN STD_LOGIC;
            q0 : OUT STD_LOGIC_VECTOR);
    end component;



begin
    myip_v1_0_HLS_weiOgC_rom_U :  component myip_v1_0_HLS_weiOgC_rom
    port map (
        clk => clk,
        addr0 => address0,
        ce0 => ce0,
        q0 => q0);

end architecture;

