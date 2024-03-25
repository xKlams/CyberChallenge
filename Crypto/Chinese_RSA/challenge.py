from Crypto.Util.number import getPrime, bytes_to_long

flag = "REDACTED"
flag = bytes_to_long(flag.encode())
for p,q in [(getPrime(512), getPrime(512)) for _ in range(5)]:
    n = p * q
    print(n, pow(flag, 5, n))
    

