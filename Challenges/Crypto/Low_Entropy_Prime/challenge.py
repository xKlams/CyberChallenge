from sympy import nextprime
from Crypto.Util.number import bytes_to_long, long_to_bytes
import random
flag = "REDACTED"

k = random.randint(2, 2**256-1)

p = nextprime(k**4 + 3*k**2 + 1)
q = nextprime(14*k**2)

n = p*q
e = 65537
c = pow(bytes_to_long(flag.encode()), e, n)
print("n =", n)
print("e =", e)
print("c =", c)