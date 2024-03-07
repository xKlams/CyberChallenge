from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

IV = bytes.fromhex("c62696d325a3a6021c12b13446a8cf6c37003678510d582179d1ee150a2af65a"[:AES.block_size])

token = bytes.fromhex("c62696d325a3a6021c12b13446a8cf6c37003678510d582179d1ee150a2af65a"[AES.block_size:])
print((xor(IV[:1], 15) + IV[1:] + token).hex())
