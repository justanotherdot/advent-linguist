import fileinput

def len_lit(s):
    return len(s)

def len_esc(s):
    return len(s.decode('string_escape')) - 2

def find_diff():
    a = []
    b = []
    for line in fileinput.input():
        line = line.strip()
        a.append(len_lit(line))
        b.append(len_esc(line))

    print sum(a) - sum(b)

find_diff()
