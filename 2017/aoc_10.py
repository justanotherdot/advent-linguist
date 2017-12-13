ls0 = "3, 4, 1, 5"  # Lengths.
#  ls0 = "197, 97, 204, 108, 1, 29, 5, 71, 0, 50, 2, 255, 248, 78, 254, 63"
ls1 = list(map(int, [c[:-1] if c[-1] == ',' else c for c in ls0.split()]))

upper_bound = 5
#  upper_bound = 256
xs = range(upper_bound)
skip_size = 0
pos = 0
size = len(xs)

assert all((l <= size and l >= 0 for l in ls1)), \
    'One of the lengths exceeds the size of the list: list {} and size {}'.format(ls1, size)

# For simplicities sake.
ls = ls1


# Man this function is a mess.
def rev_sublist(l, xs, pos):
    size = len(xs)
    if l == 0:  # rev [] == []
        ys = []
    elif l == 1:  # rev [x] == [x]
        ys = [xs[pos]]
    elif pos+l > size:  # Needs to wrap around.
        ys = (xs[pos:size+1] + xs[:(size-l+1)])[::-1]
    else:  # Does not need to wrap around.
        ys = xs[:pos+l+1][::-1]
    assert len(ys) <= len(xs)
    return ys


for l in ls:
    ys = rev_sublist(l, xs, pos)
    for i in range(len(ys)):
        xs[pos] = ys[i]
        pos = (pos+1) % size
    pos += skip_size % size
    skip_size += 1

print('checksum: {}'.format(xs[0] * xs[1]))
