from pwn import *

plain = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
enc = bytes.fromhex("14b491390429d661e4d5eb583cfb8aade04f80aa041e9147a0d2e6bd4e7fcdb762b9bba012307449193fe3d66990deb2e8ab9688f791a03b0e37a7e6f11f8c43834e250a2e8884381ba7b025bab8177342deb05cce84")

key = xor(plain, enc)


flag = bytes.fromhex("16b6992c1e07e350dac0fd0902ee82a1b25ddeea5a5e8d")

flag_de = xor(flag, key)
print(flag_de)  