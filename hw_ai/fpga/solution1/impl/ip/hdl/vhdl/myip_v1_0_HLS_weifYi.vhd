-- ==============================================================
-- Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
-- Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
-- ==============================================================
library ieee; 
use ieee.std_logic_1164.all; 
use ieee.std_logic_unsigned.all;

entity myip_v1_0_HLS_weifYi_rom is 
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


architecture rtl of myip_v1_0_HLS_weifYi_rom is 

signal addr0_tmp : std_logic_vector(AWIDTH-1 downto 0); 
type mem_array is array (0 to MEM_SIZE-1) of std_logic_vector (DWIDTH-1 downto 0); 
signal mem : mem_array := (
    0 => "00111110000100010111000100110011", 
    1 => "00111100100101110011100101010001", 
    2 => "00111101101010100000010101001111", 
    3 => "10111101100101000101000110000110", 
    4 => "10111100111011100000011101111001", 
    5 => "10111101110011101100111110100011", 
    6 => "10111110001111111001100011011011", 
    7 => "10111101100110110101111010111110", 
    8 => "00111100110111011111111110010100", 
    9 => "10111100100101000111100001100110", 
    10 => "00111110000001100010010000001011", 
    11 => "10111101101010110100000001111100", 
    12 => "00111101001010011101010000001111", 
    13 => "00111110010000000000101000010100", 
    14 => "00111110001011110011000111110011", 
    15 => "00111110001010101111100111101000", 
    16 => "10111100100111110001000001110110", 
    17 => "10111100110001011111110110011100", 
    18 => "00111110000111011100110101101111", 
    19 => "10111101110100010001100001100010", 
    20 => "10111101101000011100001010000110", 
    21 => "00111101110010100001001010111001", 
    22 => "00111101111011000001011111010100", 
    23 => "10111110011111100111001100101010", 
    24 => "00111101111101011111010101010010", 
    25 => "00111101111011111100011100101000", 
    26 => "10111110000000010101100100010001", 
    27 => "00111110011001011001100110111111", 
    28 => "00111110000001110010110100011110", 
    29 => "00111101111001000101101110111111", 
    30 => "10111101111001011011111100000110", 
    31 => "00111101110101010100010111111111", 
    32 => "00111101011101101111111000101011", 
    33 => "00111101001001000100110101010001", 
    34 => "00111100001101001001101011001110", 
    35 => "10111101101001000011110101010111", 
    36 => "00111110010101000011011011111000", 
    37 => "10111101101101011111101010110110", 
    38 => "00111101101110100101111110101110", 
    39 => "00111110001001110101001100001011", 
    40 => "10111110001001000110000110110010", 
    41 => "00111110010111110000000100010011", 
    42 => "00111110000011000110011101100001", 
    43 => "10111110010101100001100011100111", 
    44 => "00111110010100001101110100110100", 
    45 => "00111101110011010000101000001011", 
    46 => "00111110000111100000101110001011", 
    47 => "10111110000010001100101101100101", 
    48 => "00111100100001010011000010010000", 
    49 => "10111110010011000110001110011110", 
    50 => "10111101110101110000010011100011", 
    51 => "00111110000011011111011110010001", 
    52 => "10111110010100101010010001011101", 
    53 => "00111101101001011101010011010001", 
    54 => "10111101011000110101101111001001", 
    55 => "00111101110110001010011000001110", 
    56 => "10111101111111101101100011010111", 
    57 => "00111101000011100100001010110001", 
    58 => "10111100100011010100110010000100", 
    59 => "00111101110010110010010010111110", 
    60 => "00111110011100110101101001000000", 
    61 => "00111101011101111010110011101111", 
    62 => "10111101100111101000110010001001", 
    63 => "00111101011011111101100010100111", 
    64 => "10111100011110010011100110001110", 
    65 => "10111101111011110001111011000111", 
    66 => "10111101100101111001101111001110", 
    67 => "10111010110001010101010001111111", 
    68 => "00111101001000000010011100011001", 
    69 => "10111101010011001000000100001101", 
    70 => "10111101110101001001110101100001", 
    71 => "10111110000100101110111101010001", 
    72 => "10111100101111001101101010100101", 
    73 => "00111101100100001100101110011111", 
    74 => "00111110011100001110111001100101", 
    75 => "10111101000000010100010001101100", 
    76 => "10111101110001101111100111011011", 
    77 => "10111110000100000000000101000010", 
    78 => "10111100111000100101010001101100", 
    79 => "00111100101110100011100100001000", 
    80 => "10111110000110100001101111100101", 
    81 => "10111110001110010001110010011110", 
    82 => "00111101110001011110100100010000", 
    83 => "00111101010010000011101011110100", 
    84 => "10111101100011101110110010010001", 
    85 => "10111101101011011111100000001110", 
    86 => "00111101111100111100000111001011", 
    87 => "00111100100001010010001100111111", 
    88 => "00111110001001111010110000011011", 
    89 => "00111110001110111101101010001110", 
    90 => "00111110001100101101000000100101", 
    91 => "00111011111100101000000101101111", 
    92 => "00111101100110101000011000010000", 
    93 => "10111101001001001110100100000010", 
    94 => "10111101110111011001000011001010", 
    95 => "00111101101111001111001010101111", 
    96 => "00111101001111010101000000101010", 
    97 => "00111100101011011101010101110010", 
    98 => "10111101000011001010010000101001", 
    99 => "00111100110010000110101100101100", 
    100 => "10111110000000101110000010111001", 
    101 => "00111101000101111010101101111101", 
    102 => "10111011100101001111000100010011", 
    103 => "00111100000101111000011110110110", 
    104 => "00111101101100001110111010110101", 
    105 => "00111110001000111000110001011110", 
    106 => "00111011000111001010100010000010", 
    107 => "00111101010011110011011110111011", 
    108 => "10111101101111000011001011000000", 
    109 => "10111100101000111111011110011100", 
    110 => "10111100011010101011111000000110", 
    111 => "10111100110100100101000011100100", 
    112 => "00111011011111101100011111010111", 
    113 => "10111100010000010110111100010010", 
    114 => "00111101110010100101101101001101", 
    115 => "00111101100110101111111100100001", 
    116 => "10111101100001111011110100010110", 
    117 => "00111100111111111110100111111010", 
    118 => "10111110000011100000001011110000", 
    119 => "00111101001011110000000110010110", 
    120 => "00111101100010100011011111101111", 
    121 => "10111101000110011011111101111100", 
    122 => "10111101110101101011011011011001", 
    123 => "00111101101000011001000100001010", 
    124 => "00111101100000011100000101110100", 
    125 => "10111110000000000010010011101110", 
    126 => "10111110010000110110000101011011", 
    127 => "10111100010110111011010111100011", 
    128 => "00111110100011110000110010010101", 
    129 => "00111101100101001100000100110100", 
    130 => "10111101111100010111000001101101", 
    131 => "00111101110111011010111100011010", 
    132 => "10111110000001000000011011110010", 
    133 => "10111011101110011000000110100010", 
    134 => "10111101100000101100000111010111", 
    135 => "10111101110000100111101101011100", 
    136 => "10111110001000000011100000101000", 
    137 => "00111100100101011111001011011010", 
    138 => "00111101000101111011111111101101", 
    139 => "00111101010010011010111100101011", 
    140 => "10111101100000111110010000101100", 
    141 => "00111100111110101000110011100000", 
    142 => "10111110001000110101011100010100", 
    143 => "00111101011010010011000010100010", 
    144 => "10111100101001000011001110110101", 
    145 => "10111100111100011100100111001111", 
    146 => "10111101101110000101100010001001", 
    147 => "00111101100101001110000111101011", 
    148 => "00111101101001100100010111011111", 
    149 => "10111101001101001000010101110001", 
    150 => "10111101111001001011000101010001", 
    151 => "00111110001010111001101001001011", 
    152 => "10111101100011111010000011111011", 
    153 => "10111100100110010110001101000011", 
    154 => "00111101011111011011100101010101", 
    155 => "00111101111110111110101001011111", 
    156 => "10111101111001000010101000000000", 
    157 => "10111101100100110100101000011011", 
    158 => "00111101001011000101110000111101", 
    159 => "00111011110101100011110001101111", 
    160 => "10111101101011100001010101100101", 
    161 => "10111101000010110010111001011101", 
    162 => "10111101101110000000000000010101", 
    163 => "10111101110110111111111010001111", 
    164 => "00111110000101110001101011110001", 
    165 => "10111101010010011010011000011010", 
    166 => "10111101111000111100011000001111", 
    167 => "00111101011011011111111000001110", 
    168 => "10111100110101111110111111001111", 
    169 => "10111101001100101010011011111100", 
    170 => "00111110001111100010111011001000", 
    171 => "00111101100100010110001110001101" );


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

entity myip_v1_0_HLS_weifYi is
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

architecture arch of myip_v1_0_HLS_weifYi is
    component myip_v1_0_HLS_weifYi_rom is
        port (
            clk : IN STD_LOGIC;
            addr0 : IN STD_LOGIC_VECTOR;
            ce0 : IN STD_LOGIC;
            q0 : OUT STD_LOGIC_VECTOR);
    end component;



begin
    myip_v1_0_HLS_weifYi_rom_U :  component myip_v1_0_HLS_weifYi_rom
    port map (
        clk => clk,
        addr0 => address0,
        ce0 => ce0,
        q0 => q0);

end architecture;

