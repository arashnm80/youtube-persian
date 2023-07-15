t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    country_max = 0
    minimum_city = 10 ** 9

    for j in range(n):
        line = list(map(int, input().split()))
        for k , number in enumerate(line):
            if (j + k) % 2 == 1:
                minimum_city = min(number, minimum_city)
        country_max += sum(line)

    if n % 2 == 0 and m % 2 == 0:
        country_max -= minimum_city

    print(country_max)