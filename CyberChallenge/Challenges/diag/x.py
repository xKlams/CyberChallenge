from pwn import *
import base64
from hashlib import md5
import string


p = remote("cyberchallenge.diag.uniroma1.it", 5001)
junk = p.recvuntil(b"^.^")
test = p.recv(1)
# print(b"test = " + test)
while(True):
    line = p.recvline()
    print(line)
    print(line[:len("HI! I'm a random")])
    if line.decode()[:len("Hi! I'm a random")] == "Hi! I'm a random" or line.decode()[:len("Nice job, still")] == "Nice job, still":
        continue
    if line[:1] == b"[":
        ntest = line.decode()[1: line.decode().find("]")]
        # print(b"test = " + test)
        ntest = ntest.split(", ")
        print(ntest)
        a_list = []
        for i in ntest:
            a_list.append(int(i))
        # p.sendline(test.sort())
        a_list.sort()
        print("standard print of test")
        print(a_list)
        payload = b"["
        for i in a_list:
            # payload += (b"'")
            payload += str(i).encode()
            payload += (b", ")
        payload = payload[:-2]
        payload += b"]"

        print(payload)

        p.sendline(payload)

    elif line[:1] == b'x':
        # junk = (b"^ ")
        line = line.decode()
        # print("duceduce")
        first_n = line[line.find("^ ") + 2: line.find(" =")]
        first_n = int(first_n)
        print(first_n)
        # junk = p.recvuntil(b"= ")
        second_n = int(line[line.find("= ") + 2: line.find(" =", line.find(" == ") + 4)])
        print(second_n)
        payload = first_n ^ second_n
        print(payload)
        p.sendline(str(payload).encode())


    elif ord(line.decode()[:1]) in range(ord('a'), ord('z')) or ord(line.decode()[:1]) in range(ord('A'), ord('Z')):
        line = line.decode()
        test = line[: line.find("=> ?") - 1]
        print(test)
        print("i just printed test")
        p.sendline(base64.b64decode(test))
    
    elif line[:1] == b"(":
        line = line.decode()
        f_n = int(line[1:line.find(" + ")])
        s_n = int(line[line.find(" + ") + 3: line.find(" * ")])
        t_n = int(line[line.find(" * ") + 3: line.find(")")])
        a_n = int(line[line.find(" & ") + 3: line.find(" = ")], 16)
        payload = f_n + s_n * t_n
        payload = payload & a_n
        print(str(payload))
        p.sendline(str(payload).encode())


p.interactive()
