from pwn import *
import base64
from hashlib import md5
import string


list = [0x63,
0x62,
0x6b,
0x77,
0x7f,
0x62,
0x69,
0x68,
0x6c,
0x56,
0x60,
0x3b,
0x6e,
0x52,
0x61,
0x61,
0x4f,
0x68,
0x7d,
0x66,
0x66,
0x4a,
0x70,
0x7e,
0x6a,
0x6a,
0x6e,
0x44,
0x7f,
0x6f,
0x2a,
0x7c,
0x4b,
0x4c,
0x11,
0x7c,
0x53,
0x44,
0x55,
0x78,
0x41,
0x5d,
0x75,
0x43,
0x4d,
0x5f,
0x4a,
0x52,]

for i in range(0, len(list)):
    print(chr(list[i] ^ i), end="")
print("")
#flag = ccit{good_j0b_on_your_first_cr4ckm3_was_it_hard} #alberto finocchio 
