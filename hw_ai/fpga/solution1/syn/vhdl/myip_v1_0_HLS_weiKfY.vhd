-- ==============================================================
-- Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
-- Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
-- ==============================================================
library ieee; 
use ieee.std_logic_1164.all; 
use ieee.std_logic_unsigned.all;

entity myip_v1_0_HLS_weiKfY_rom is 
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


architecture rtl of myip_v1_0_HLS_weiKfY_rom is 

signal addr0_tmp : std_logic_vector(AWIDTH-1 downto 0); 
type mem_array is array (0 to MEM_SIZE-1) of std_logic_vector (DWIDTH-1 downto 0); 
signal mem : mem_array := (
    0 => "10111110001001011111101010001101", 
    1 => "10111110001101000011000100111111", 
    2 => "10111101011110110100111010001101", 
    3 => "00111101100100011010001001110110", 
    4 => "00111101010010001010011110000011", 
    5 => "00111101110100010111001110101111", 
    6 => "00111101000100110000001111010011", 
    7 => "10111101110111111111111010100100", 
    8 => "00111101110000111001011101010010", 
    9 => "10111101101010111111111100100111", 
    10 => "10111101010101110101010111000000", 
    11 => "10111110010101100100000111111110", 
    12 => "00111101100101011001001101100111", 
    13 => "00111100110110011110100011100100", 
    14 => "00111101101000011000010100011000", 
    15 => "00111100001111110011101010110100", 
    16 => "00111101010001001010100101101001", 
    17 => "00111110010010011100101010010011", 
    18 => "00111110001100101101001111011111", 
    19 => "00111101001001101000110001001000", 
    20 => "10111101110100001100011110000101", 
    21 => "00111110001011010000000001011001", 
    22 => "00111101101011010111110100011000", 
    23 => "10111110001000101110110000011110", 
    24 => "10111101111111110111000000000001", 
    25 => "00111110001000010001001001101000", 
    26 => "00111110010001100001000001010011", 
    27 => "00111101110100011000100100010011", 
    28 => "00111101001010101010001101101011", 
    29 => "00111101110100001101110101010111", 
    30 => "00111101101010000111111110111100", 
    31 => "10111110000100111110111000101100", 
    32 => "10111101001101101010100111011111", 
    33 => "10111110011001000001010011101011", 
    34 => "10111101111111111111101110101100", 
    35 => "00111110000001110010111011101101", 
    36 => "10111110001111000110011000000111", 
    37 => "10111110000100100100110000111110", 
    38 => "10111110001110001000010111001011", 
    39 => "00111101110100010100011101010010", 
    40 => "00111100001111011111010011101101", 
    41 => "10111110000101101101111011000011", 
    42 => "10111101100101101100001011010001", 
    43 => "10111110000110011001100010111011", 
    44 => "00111101100101110111010010101000", 
    45 => "00111101101101111111111011111100", 
    46 => "00111101110100000010110010110011", 
    47 => "00111110000000101101000001111010", 
    48 => "00111110001100010110011010111000", 
    49 => "10111110001110010111001110110100", 
    50 => "10111110001011110101011101000110", 
    51 => "00111100111101101011101111100000", 
    52 => "10111110000101100001010100000011", 
    53 => "10111110001111101010110110010101", 
    54 => "00111110010000110110011100011011", 
    55 => "10111110011110000000111111011101", 
    56 => "10111110001000101010110011011111", 
    57 => "10111101000111101001010111001000", 
    58 => "10111100101110011100001100111100", 
    59 => "10111101110011111101100001100001", 
    60 => "00111101100111010100100000111111", 
    61 => "00111110000111011000010011010011", 
    62 => "10111100100011111011010001010001", 
    63 => "00111101001101110000001111010011", 
    64 => "10111110001100011111101001101010", 
    65 => "00111101110001110111000110101101", 
    66 => "00111101111101011101110110000000", 
    67 => "10111101111001010111101001000010", 
    68 => "00111100101100111101011100000010", 
    69 => "10111101000000011011011011010000", 
    70 => "10111110010100101100000010001010", 
    71 => "10111101010011010010011110101001", 
    72 => "10111101101110100101111111011011", 
    73 => "00111100111011100001110110010110", 
    74 => "00111101000011101101101011101011", 
    75 => "00111101011100001010010100000000", 
    76 => "10111101010001011111100001011011", 
    77 => "00111100111010111100101000010010", 
    78 => "10111101010011110110001010110100", 
    79 => "00111110001111111100110010111110", 
    80 => "10111101001100100111111110011000", 
    81 => "00111101111100101110000000000001", 
    82 => "10111101110010010101111101001100", 
    83 => "00111110000100100000101110001110", 
    84 => "10111100010010111000011101000101", 
    85 => "00111101110110000100011000001100", 
    86 => "00111110000001000000011111011011", 
    87 => "00111101000011100101111000010100", 
    88 => "00111101011011000111000111010000", 
    89 => "10111100111110000001111100111100", 
    90 => "00111100101111010001100010011100", 
    91 => "10111100100101011110111010000011", 
    92 => "00111101001111111101000110010100", 
    93 => "10111101111000111001011010010000", 
    94 => "10111110000101110101111100010111", 
    95 => "00111101100001100101011001100111", 
    96 => "00111101111010001110111110001010", 
    97 => "00111110000101100100001001110100", 
    98 => "10111110000010011110111001111111", 
    99 => "00111101011010110110011101101101", 
    100 => "10111101001010110110111101000101", 
    101 => "10111101001010001010001101111100", 
    102 => "10111101010001111100110111011000", 
    103 => "00111101010111011111001111100001", 
    104 => "10111110000011101110110011111001", 
    105 => "10111100000001100101001001101110", 
    106 => "00111100110111000001101101101000", 
    107 => "10111101100111000011000001101111", 
    108 => "00111101110010001110011001001011", 
    109 => "10111101010000110111011101111101", 
    110 => "00111101100110110000110101011110", 
    111 => "00111101001110001011111011111011", 
    112 => "00111110000001000111010110110011", 
    113 => "10111101001111001000100111010010", 
    114 => "10111110001001111001000011001100", 
    115 => "10111101110111110000000101011001", 
    116 => "00111110001001011001100101011101", 
    117 => "10111110010101000100011100110111", 
    118 => "10111101011011010110101111000001", 
    119 => "00111101000011000011011000100101", 
    120 => "10111101101010110100010111111011", 
    121 => "00111110000100001111100100111110", 
    122 => "00111110001100010101000011010001", 
    123 => "10111110001111001010101100010001", 
    124 => "10111000101110111110100000101011", 
    125 => "00111110000110100101110100010111", 
    126 => "10111101111100010111111011010101", 
    127 => "00111101010101011111100101010110", 
    128 => "00111110010001010011111000010110", 
    129 => "00111100001110101101001110001110", 
    130 => "00111110011100100010110010010001", 
    131 => "10111101100010000110110100111101", 
    132 => "00111011100111001010110101010110", 
    133 => "00111110001011001111001111100111", 
    134 => "00111110000000101111011000010111", 
    135 => "10111101010101011000111011111101", 
    136 => "10111101011100110000001100000001", 
    137 => "10111100010001111100010101100000", 
    138 => "10111011100001111100110011001011", 
    139 => "10111101110110011101010100000010", 
    140 => "10111101111111111100110000110111", 
    141 => "10111110010000111000110000100011", 
    142 => "10111101111011011010101001111111", 
    143 => "00111010100000011001100010100101", 
    144 => "00111100100000011000010001011011", 
    145 => "00111100010011101000111001011100", 
    146 => "10111101011000011111111001111010", 
    147 => "00111101100010010110010000101101", 
    148 => "10111100001110011100110011111100", 
    149 => "10111100110101100011110010000101", 
    150 => "10111100001110000100111000000101", 
    151 => "10111101100100100011101100111111", 
    152 => "00111101101110100101111110101111", 
    153 => "10111110010010001100110111001100", 
    154 => "00111101100000100001010010110101", 
    155 => "00111110000101011100110000110010", 
    156 => "00111101100100010101111100001011", 
    157 => "10111101111100001000101100100010", 
    158 => "10111101001110010100110100000001", 
    159 => "00111101101001111101011111011111", 
    160 => "10111101100000001110111100010011", 
    161 => "00111110001101011010111010000000", 
    162 => "10111100001010011000001111111010", 
    163 => "10111100010001001101011010001000", 
    164 => "10111100000010011010001111010101", 
    165 => "00111101011010000111010011000110", 
    166 => "10111100000100101010000011001100", 
    167 => "10111101100011101010111101010011", 
    168 => "00111101000001110000011011111011", 
    169 => "10111100110001001111000100011010", 
    170 => "00111110000101011001001111010100", 
    171 => "00111110001000100000110110001101" );


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

entity myip_v1_0_HLS_weiKfY is
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

architecture arch of myip_v1_0_HLS_weiKfY is
    component myip_v1_0_HLS_weiKfY_rom is
        port (
            clk : IN STD_LOGIC;
            addr0 : IN STD_LOGIC_VECTOR;
            ce0 : IN STD_LOGIC;
            q0 : OUT STD_LOGIC_VECTOR);
    end component;



begin
    myip_v1_0_HLS_weiKfY_rom_U :  component myip_v1_0_HLS_weiKfY_rom
    port map (
        clk => clk,
        addr0 => address0,
        ce0 => ce0,
        q0 => q0);

end architecture;

