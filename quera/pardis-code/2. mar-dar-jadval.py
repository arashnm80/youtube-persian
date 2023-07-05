n, m = map(int, input().split())

t = 1
for i in range(1 , 1 + n):
    if i % 2 == 1: # odd
        line = map(str, range(t, t + m))
        print(" ".join(line))
        t += m
    else: # even
        line = map(str, reversed(range(t, t + m)))
        print(" ".join(line))
        t += m