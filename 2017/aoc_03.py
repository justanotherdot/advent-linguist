# Find the largest and sqrt pair grid size
def rings():
    i = 1
    k = i
    while True:
        yield (i, k)
        i += 2
        k = i**2

def pair(n):
    for i, k in rings():
        if k >= n:
            return (i, k)

# Number of cells in an outermost grid.
def ring_count(i):
    return i**2 - (i-2)**2

def corners(pair):
    i, k = pair
    return [k - (i-1)*s for s in range(4)]

def middles(pair):
    i, _ = pair
    cs = corners(pair)
    return list(map(lambda x: x - (i/2), cs))

# Distance to 'access port'.
# Distance will always be the sum of the two sides.
# i.e. From both sides
def dist(n):
    i, k = pair(n)
    ms = middles((i, k))
    cs = corners((i, k))
    if n in ms:
        return 0 + (i/2)
    elif n in cs:
        return (i/2)*2
    else:
        # Which side is it on?
        if n < cs[-1]:
            # RHS
            delta = abs(ms[-1] - n)
            return delta + (i/2)
        else:
            # No need to check for equality as the above ms and cs checks did that.
            side = [(p, q) for p, q in list(zip(cs, cs[1:])) if n < p and n > q]
            middle = [m for m in ms if m < side[0][0] and m > side[0][1]][0]
            delta = abs(n - middle)
            return delta + (i/2)

print(dist(1))
print('')

print(dist(12))
print('')

print(dist(23))

print(dist(1024))
print('')

print(dist(347991))
print('')
