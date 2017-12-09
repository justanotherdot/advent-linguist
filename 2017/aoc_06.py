s = "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"
#  s = "0 2 7 0"
xs = tuple(x for x in map(int, s.split()))

def inc(i):
    return 0 if (i+1) >= len(xs) else i+1

d = {}
i = 0
cycles = 0
d[xs] = 1
while d[xs] < 2:
    m = max(xs)
    tmp = list(xs)
    # Redistribution cycle.
    if tmp[i] == m:
        cycles += 1
        tmp[i] = 0
        while m > 0:
            i = inc(i)
            tmp[i] += 1
            m -= 1
        xs = tuple(tmp)
        d[xs] = d.get(xs, 0) + 1
        i = 0
    # Scanning action.
    else:
        i = inc(i)

print(cycles)

