from pwn import *
import base64
from hashlib import md5
import string

elf = ELF("./sw-19")
if args.REMOTE:
	p = remote("software-17.challs.olicyber.it", 13002)
else:
	p = process([elf.path])

p.sendline(b'a')
for i in range(20):
	junk = p.recvuntil(b"-> ")
	
	function_name = p.recvuntil(b":")[:-1]
	print(function_name)
	payload = elf.sym[function_name.decode()]
	print(hex(payload))
	p.sendline(str(hex(payload)).encode())



p.interactive()