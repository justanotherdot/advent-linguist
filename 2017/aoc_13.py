from collections import defaultdict

s = """
0: 3
1: 2
4: 4
6: 4
"""

s = """
0: 4
1: 2
2: 3
4: 4
6: 8
8: 5
10: 6
12: 6
14: 10
16: 8
18: 6
20: 9
22: 8
24: 6
26: 8
28: 8
30: 12
32: 12
34: 12
36: 12
38: 10
40: 12
42: 12
44: 14
46: 8
48: 14
50: 12
52: 14
54: 14
58: 14
60: 12
62: 14
64: 14
66: 12
68: 12
72: 14
74: 18
76: 17
86: 14
88: 20
92: 14
94: 14
96: 18
98: 18
"""

def firewall(s):
    '''
    A firewall layer is it's
        * N-1 indexed layer
        * Max bound size
        * Polarity to increase or decrease by
        * Current position of scanner
    '''
    ls = (l for l in s.splitlines() if l)
    ns = [map(int, l.split(': ')) + [1] + [0] for l in ls]
    assert ns == sorted(ns, key=lambda n: n[0])
    return ns

fwall = firewall(s)
max_picoseconds = fwall[-1][0] + 1
total = 0
for ps in range(max_picoseconds):
    for layer in fwall:
        pos = layer[-1]
        depth = layer[0]
        range = layer[1]
        if pos == 0 and depth == ps:
            # Caught.
            total += depth*range
        if layer[-1] == 0:
            layer[2] = 1
        elif layer[-1]+1 == layer[1]:
            layer[2] = -1
        layer[-1] += layer[2]

print(total)
