t = int(input())

for _ in range(t):
    r, u, l, d, k = map(int, input().split())

    x_max = max(r, l)
    x_min = min(r, l)

    y_max = max(u, d)
    y_min = min(u, d)

    h1 = max(x_max - x_min, y_max - y_min) # longer
    h2 = min(x_max - x_min, y_max - y_min) # long
    temp = x_min + y_min

    if k <= temp:
        h1 += k
        h2 += k
        temp -= k
        k = 0
    else:
        h1 += temp
        h2 += temp
        k -= temp
        temp = 0
        if h2 >= k:
            h1 += k
            h2 -= k
            k = 0
        else:
            h1 += h2
            k -= h2
            h2 = 0
    print((h1 ** 2) + (h2 ** 2))