
def get_num(x):
    try:
        return int(x)
    except ValueError:
        return 0


def clean(c):
    c = c.strip('[]{}')
    c = c.replace(']', '')
    c = c.replace('}', '')
    return c


with open('advent12.in') as f:
    content = f.read()

key_vals = content.split(':')
vals = []
for e in key_vals:
    for cell in e.split(','):
        cell = clean(cell)
        vals.append(get_num(cell))
        print cell

print sum(vals)
