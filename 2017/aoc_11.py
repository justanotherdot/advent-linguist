s = 'ne, ne, ne'
s = 'ne, ne, sw, sw'
s = 'ne, ne, s, s'
steps = s.split(', ')

ring_depth = 0
last_step = ''

polarity = 1
for s in steps:
    if last_step == s:
        if ring_depth == 0:
            polarity = 1
    if last_step == 'ne':
        if s == 'sw':
            polarity = -1
        elif s == 'nw' or s == 'se':
            pass # polarity = polarity
        elif s == 's':
            polarity = -1
        elif s == 'n':
            polarity = 1
    elif last_step == 'nw': # Same thing as 'ne' but reflected.
        if s == 'se':
            polarity = -1
        elif s == 'ne' or s == 'sw':
            pass # polarity = polarity
        elif s == 's':
            polarity = -1
        elif s == 'n':
            polarity = 1
    elif last_step == 'sw':
        if s == 'ne':
            polarity = -1
        elif s == 'nw' or s == 'se':
            pass # polarity = polarity
        elif s == 's':
            polarity = 1
        elif s == 'n':
            polarity = -1
    elif last_step == 'se':
        if s == 'nw':
            polarity = -1
        elif s == 'ne' or s == 'sw':
            pass # polarity = polarity
        elif s == 's':
            polarity = 1
        elif s == 'n':
            polarity = -1

    ring_depth += polarity
    last_step = s
    assert ring_depth >= 0

print(ring_depth)
