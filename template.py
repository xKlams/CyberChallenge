from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long
import string
import math

# prima di tutto
# context.terminal=["tmux", "splitw", "-h"]
# elf = ELF('./nome-file')
# p = elf.process()

#prima del p.send

# ui.pause()
# gdb.attach(p)