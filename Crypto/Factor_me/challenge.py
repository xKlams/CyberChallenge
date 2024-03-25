from Crypto.Util.number import getPrime, bytes_to_long

flag = "REDACTED"

N = 1
for _ in range(20):
    N *= getPrime(75)

print(f'N = {N}')
print(f'c = {pow(bytes_to_long(flag.encode()), 65537, N)}')


