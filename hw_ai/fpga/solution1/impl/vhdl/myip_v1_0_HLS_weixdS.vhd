-- ==============================================================
-- Vivado(TM) HLS - High-Level Synthesis from C, C++ and SystemC v2019.2 (64-bit)
-- Copyright 1986-2019 Xilinx, Inc. All Rights Reserved.
-- ==============================================================
library ieee; 
use ieee.std_logic_1164.all; 
use ieee.std_logic_unsigned.all;

entity myip_v1_0_HLS_weixdS_rom is 
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


architecture rtl of myip_v1_0_HLS_weixdS_rom is 

signal addr0_tmp : std_logic_vector(AWIDTH-1 downto 0); 
type mem_array is array (0 to MEM_SIZE-1) of std_logic_vector (DWIDTH-1 downto 0); 
signal mem : mem_array := (
    0 => "10111100111010111100110100111111", 
    1 => "10111101001110111011011101011110", 
    2 => "00111110001000001111110111000001", 
    3 => "00111101101100100010011110001111", 
    4 => "10111011010111000100111010110111", 
    5 => "10111100110001110001000101000100", 
    6 => "00111110000100111111101100000011", 
    7 => "00111110000010001110010010010110", 
    8 => "10111101111110100101001111010000", 
    9 => "00111100101001011111000101001000", 
    10 => "10111011000101101110010110111011", 
    11 => "00111101110011000110110101011010", 
    12 => "10111011011011000101001011001100", 
    13 => "10111110011001110000010101101001", 
    14 => "00111110010010001001000111010011", 
    15 => "10111011101011100101110010000110", 
    16 => "10111011011000011110111001110110", 
    17 => "10111101101010110001001110100111", 
    18 => "00111100011010011000101100111011", 
    19 => "10111110000100000110100101100110", 
    20 => "10111100100100010011100101010110", 
    21 => "00111101011111111101110010110000", 
    22 => "10111110011000010000100110100001", 
    23 => "10111110101001101110000101111011", 
    24 => "00111110000100110001100110101000", 
    25 => "10111110000000011001000111100011", 
    26 => "10111101101110101110110011110110", 
    27 => "00111100101010000000011001011010", 
    28 => "00111101010011100011110000000100", 
    29 => "00111110010110110001010100001010", 
    30 => "00111101001101111111000100111110", 
    31 => "10111101110110101101000001000001", 
    32 => "10111110010110010000110001111000", 
    33 => "00111101011001001000011001010111", 
    34 => "00111110001100011010010001111101", 
    35 => "10111101100000000110111111111100", 
    36 => "00111101110110001000100000110000", 
    37 => "00111110001101101100010010111010", 
    38 => "00111110001000111000011110011011", 
    39 => "10111101011110101001000100000001", 
    40 => "10111100111100101011010011010101", 
    41 => "00111101101001111010010100011011", 
    42 => "00111101100110001101000001010011", 
    43 => "00111100101110110011100111001010", 
    44 => "10111101110010001011000011001000", 
    45 => "00111101100100110101000001011111", 
    46 => "10111101000011110111001010001101", 
    47 => "00111101101000000100100001101010", 
    48 => "10111101000000011000111111011001", 
    49 => "10111101011011100110100001100001", 
    50 => "00111110000110001010001111010011", 
    51 => "00111101000101101110001101011101", 
    52 => "10111110001010111110010001110100", 
    53 => "10111110001000100000101001111010", 
    54 => "00111101000010000101010001101111", 
    55 => "00111101011001001001101011011100", 
    56 => "10111110001101010110101000110010", 
    57 => "10111110001000100111110100111101", 
    58 => "10111101000110000010000011100111", 
    59 => "10111101010100000011100111001011", 
    60 => "00111101000111011101000000100100", 
    61 => "10111110010000000001100111001010", 
    62 => "10111101111101100111010100000111", 
    63 => "10111101111010001000111001100101", 
    64 => "00111110000010101000111000010100", 
    65 => "10111110010110111101110010101111", 
    66 => "00111101011110001000100010111000", 
    67 => "00111110010111111110001010101001", 
    68 => "10111101000110101101101010001001", 
    69 => "00111101001110011110001010100001", 
    70 => "00111100000011001111000011001000", 
    71 => "00111110000010001000001111101001", 
    72 => "00111110000010011011011110111001", 
    73 => "00111110001110100101011111000110", 
    74 => "10111110001001111011011011101110", 
    75 => "00111101001111001011011101101000", 
    76 => "10111110000100000011111100100101", 
    77 => "00111110001000011110100011011001", 
    78 => "00111101110010001111110100111001", 
    79 => "10111101111011011001100110101111", 
    80 => "00111101011101000010101011100010", 
    81 => "10111101111010111000100110000000", 
    82 => "00111101001101001110100101111011", 
    83 => "10111100110111110011111101001101", 
    84 => "00111110001011101000111111110100", 
    85 => "00111101111111000111110110110101", 
    86 => "00111100100001010010110100001000", 
    87 => "10111100011111101011011011110010", 
    88 => "00111101101000001011010010011110", 
    89 => "00111100100110100000101111000100", 
    90 => "10111101110011100001101011101110", 
    91 => "00111110001001001100100011011000", 
    92 => "00111100100110000000111010001110", 
    93 => "10111100011100001001100010011110", 
    94 => "10111110000100110001010011111111", 
    95 => "00111110010001100111100110000111", 
    96 => "10111101111001001110000001110100", 
    97 => "00111110001110001101010000011000", 
    98 => "10111100111001011010001110011111", 
    99 => "00111110001101000100100110010011", 
    100 => "00111101101001001000010111111000", 
    101 => "00111101100111101101001100110110", 
    102 => "10111110010101101011011111011000", 
    103 => "10111110001100010001101001011111", 
    104 => "10111110000010110111110111010100", 
    105 => "10111101101000100010110111000000", 
    106 => "00111101111100001011010101001100", 
    107 => "00111101110110000000001101111010", 
    108 => "10111110001100100011110101101110", 
    109 => "00111101100100110010000001000111", 
    110 => "10111110000001100110000101000101", 
    111 => "00111101100000000101001101111011", 
    112 => "00111110001011101011101110000000", 
    113 => "00111101101100111100111111000110", 
    114 => "10111110000010111010101011101000", 
    115 => "10111101111001011100011100000010", 
    116 => "00111101001010111111110011100111", 
    117 => "10111110000111011101000001111011", 
    118 => "00111110001100100011100000000011", 
    119 => "00111100000000000000111100010000", 
    120 => "00111101111000111001011011110000", 
    121 => "10111101000111111101111000110111", 
    122 => "00111110001010001001111110000010", 
    123 => "10111110100011000011111010101001", 
    124 => "00111101110101011001101000001011", 
    125 => "10111110000000110000100011100000", 
    126 => "00111100110100011001000011101101", 
    127 => "00111101110010111010100011110101", 
    128 => "10111101110111010110010010000111", 
    129 => "00111110000001010111010001100100", 
    130 => "00111101011000000100000111111110", 
    131 => "10111110001111110111100100100010", 
    132 => "00111100101100000011010110000010", 
    133 => "10111100010001001110010000001100", 
    134 => "00111110001000110001010000000001", 
    135 => "10111100010000010101010111000000", 
    136 => "10111110000000100111101100101100", 
    137 => "10111101010011100110000001001011", 
    138 => "00111101001011010100110001101010", 
    139 => "10111101111110101010001100110111", 
    140 => "00111101001101000001111110010110", 
    141 => "00111110000111001011110111010001", 
    142 => "10111101010000100101011110100001", 
    143 => "10111101010001111101101001101000", 
    144 => "10111110011011001001000111111101", 
    145 => "00111100011000011011000100011111", 
    146 => "10111101110011101001101000000111", 
    147 => "10111101100110100101111110010000", 
    148 => "00111101101000001001111000010111", 
    149 => "00111110001100100000001000111001", 
    150 => "10111101010001111111100001000000", 
    151 => "10111110000010100010100001111001", 
    152 => "10111101011111000101011001100111", 
    153 => "00111101101110000010110011101111", 
    154 => "00111101101001111001110011001000", 
    155 => "10111110001010011101000111011100", 
    156 => "10111101000010101100101110111000", 
    157 => "10111110001011011011011100011010", 
    158 => "00111101111001010100100011001110", 
    159 => "00111110000000110101011001011000", 
    160 => "10111110000110000110110000001110", 
    161 => "00111101001001010110011011000100", 
    162 => "00111110000001010010000010110101", 
    163 => "10111101110110100011110000111010", 
    164 => "10111101100110101100010000001010", 
    165 => "00111101101110011000101000011001", 
    166 => "00111101011001110010100101100111", 
    167 => "10111101100001100101110001000101", 
    168 => "00111101100111111101010100011000", 
    169 => "00111110011001010101110110010110", 
    170 => "00111101010000100101101011111011", 
    171 => "00111101101001000001000011101011" );


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

entity myip_v1_0_HLS_weixdS is
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

architecture arch of myip_v1_0_HLS_weixdS is
    component myip_v1_0_HLS_weixdS_rom is
        port (
            clk : IN STD_LOGIC;
            addr0 : IN STD_LOGIC_VECTOR;
            ce0 : IN STD_LOGIC;
            q0 : OUT STD_LOGIC_VECTOR);
    end component;



begin
    myip_v1_0_HLS_weixdS_rom_U :  component myip_v1_0_HLS_weixdS_rom
    port map (
        clk => clk,
        addr0 => address0,
        ce0 => ce0,
        q0 => q0);

end architecture;

