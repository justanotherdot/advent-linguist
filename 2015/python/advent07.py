import fileinput
import ctypes

wires = {}
known_values = {}

def lookup(argument):
    if argument in known_values:
        return known_values[argument]
    else:
        a = wires.get(argument, None)
        if isinstance(a, str):
            return lookup(a)
        else:
            if isinstance(a, Wire):
                known_values[a] = a.evaluate()
                return known_values[a]
            else:
                return a

class Wire():
    def __init__(self, name, thunk, arg_names):
        self.name = name.strip()
        self.thunk = thunk
        self.arg_names = arg_names

    def evaluate(self):
        args = [lookup(arg) for arg in self.arg_names if lookup(arg)]
        args = map(int, args)
        try:
            return apply(self.thunk, args)
        except TypeError:
            print args

# Examples...

# x AND y -> d
# Wire(d, lambda x,y: x and y, ['x','y'])
# Example input

test_in_01 = """
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
123 -> x
456 -> y
"""

def is_num(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def analyze_rvalue(rvalue):
    elems = rvalue.split()
    if 'RSHIFT' in elems:
        return (lambda x: x >> int(elems[2]), [elems[0]])
    elif 'LSHIFT' in elems:
        return (lambda x: x << int(elems[2]), [elems[0]])
    elif 'OR' in elems:
        if is_num(elems[0]):
            return (lambda x: int(elems[0]) | x, [elems[2]])
        elif is_num(elems[2]):
            return (lambda x: x | int(elems[2]), [elems[0]])
        else:
            return (lambda x,y: x | y, [elems[0], elems[2]])
    elif 'AND' in elems:
        if is_num(elems[0]):
            return (lambda x: int(elems[0]) & x, [elems[2]])
        elif is_num(elems[2]):
            return (lambda x: x & int(elems[2]), [elems[0]])
        else:
            return (lambda x,y: x & y, [elems[0], elems[2]])
    elif 'NOT' in elems:
        return (lambda x: ctypes.c_ushort(~x).value, [elems[1]])
    else:
        return (lambda : elems[0], [])

def parse_instruction(line):
    tokens = line.split('->')
    lvalue = tokens[1].strip()
    rvalue = tokens[0]
    (thunk, arg_names) = analyze_rvalue(rvalue)
    wires[lvalue] = Wire(lvalue, thunk, arg_names)

for line in fileinput.input():
#for line in test_in_01.split('\n'):
    if not line:
        continue
    parse_instruction(line)


print wires['lx'].evaluate()
