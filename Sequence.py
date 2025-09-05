Sequence = int(input())

a, b, c, = 1, 2, 3

print(a)
print(b)
print(c)

for i in range(3, Sequence):
    d = a + b + c
    print(d)
    a,b,c = b, c, d
