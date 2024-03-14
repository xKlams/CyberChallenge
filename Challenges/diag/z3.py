from z3 import *

solver = Solver()

ins = [Int(f'ins_{i}') for i in range(20)]

for c in ins:
    solver.add(c>= 0)
    solver.add(c <= 2)

s = 0
a = 0
x = 0
y = 0

# 0 r
# 1 L
# 2 R

for c in ins:
    s = If(c == 0, s + 1 , s)
    a = If(
        c == 1,
        (a + 1) % 4,
        If(
            c == 2,
            (a + 3) % 4, 
            a
        )
    )
    x = If(
        a == 0,
        x + s,
        If(
            a == 2,
            x - s,
            x
        )
    )
    Y = If(a == 1, y + s, y)
    Y = If(a == 3, y - s, y)
solver.add(x == 168)
solver.add(y == 32)

if solver.check() == sat:
    print(s.model())