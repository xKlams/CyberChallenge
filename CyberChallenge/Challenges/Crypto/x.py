from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long
import string
import math

n = 110968599119650947755713144315887249858445735232963073262615997352849701072880107890292973637413044852856494455186015464049133877730723919630224538313174163309200300818616925517843938300839825492729539483588597127943241769264032242964151707268136387330738824537859607227724901404407691099027974359478993558423                                                                  
e = 65537
d = 15988517813659825991545955985069268830279337309099582115870352996584760425370644044922305248437964989709216549056306341280924589612768091283219152139684946925162780711002318042525925352146836819888474757252547432952647003492886727982135445873893929941734077309767533402422877400018568452297342121983838410113
ct = "58725126cb90cb7113a6e2507bd658b010d35b387c1dd09f240410085b41bc742037298092e34bfaa57cdbbe40da7e1a89321f4ed08bcb61b287aaf380982b2041ea7fd4628a5a3a4dbecae36990f21cd572154240d0bfed0263f7e104068b4e82234c9af918800bf3b6124d3c83cdb139d0680849a5916a86bb987e99ae1e8a"  

# print(long_to_bytes(pow(ct, d, n)))

# key = RSA.construct((n, e, d))
# cipher = PKCS1_OAEP.new(key)
# message = cipher.decrypt(bytes.fromhex(ct))
# print(message)
a = 1045691
b = 696937
n = 728780748467
ct =47646886470

phi = (a-1) * (b-1)

d = pow(e, -1, phi)
# print
# ciphertext = bytes_to_long(ciphertext)
# phi = (n-1)
# d = pow(e, -1, phi)
# ct = bytes_to_long(ct)
print(long_to_bytes(pow(ct, d, n)))
