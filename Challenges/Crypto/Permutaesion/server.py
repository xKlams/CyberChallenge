#! /usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from math import factorial
import random
import secrets
from binascii import hexlify, unhexlify
import os


def lehmer_decode(n, size):
    num_length = len(str(size))
    n = n.zfill(size * len(str(size)))
    permutation = list(
        map(
            int,
            [
                n[i : i + len(str(size))]
                for i in range(0, size * len(str(size)), len(str(size)))
            ],
        )
    )

    for i in range(len(permutation) - 1, -1, -1):
        for j in range(i + 1, len(permutation)):
            if permutation[j] >= permutation[i]:
                permutation[j] += 1

    return permutation


def lehmer_encode(permutation):
    permutation = permutation[::]
    n = len(str(len(permutation)))  # lol
    assert all(sorted(permutation)[i] == i for i in range(len(permutation)))
    digits = ""
    for i in range(len(permutation) - 1):
        for j in range(i + 1, len(permutation)):
            if permutation[j] >= permutation[i]:
                permutation[j] -= 1
        digits += str(permutation[i]).zfill(n)
    digits += str(permutation[-1]).zfill(n)

    return int(digits)


def apply_permutation(text, permutation):
    text = b"".join([bin(char)[2:].zfill(8).encode() for char in text])

    new_text = [None] * len(text)

    for idx, e in enumerate(permutation):
        new_text[e] = text[idx]

    new_text = bytes(new_text)
    return bytes([int(new_text[i : i + 8], 2) for i in range(0, len(new_text), 8)])


def main():
    flag = pad(secrets.flag, 16)
    key = os.urandom(16)
    iv = os.urandom(16)
    while True:
        print("Provide a permutation")
        permutation = lehmer_decode(input(), len(flag) * 8)
        perm_flag = apply_permutation(flag, permutation)

        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        print(hexlify(cipher.encrypt(perm_flag)).decode("ascii"))


if __name__ == "__main__":
    try:
        main()
    except:
        pass
