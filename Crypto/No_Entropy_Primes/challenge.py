from Crypto.Util.number import bytes_to_long, long_to_bytes, getPrime
from sympy import nextprime

flag = "REDACTED"

p = getPrime(512)
q = nextprime(p+1)

n = p*q
e = 65537
c = pow(bytes_to_long(flag.encode()), e, n)

print("n =", n)
print("e =", e)
print("c =", c)
