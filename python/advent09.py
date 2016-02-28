import sys
from collections import defaultdict, namedtuple

Edge = namedtuple('Edge', ['name', 'cost'])

class DSet():
    parent = None
    name = None
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name


def city_map():
    """
    An adjacency list that represents the given graph
    """
    cities = defaultdict(list)
    if sys.argv:
        with open(sys.argv[1]) as f:
            for line in f:
                line = line.strip()
                elems = line.split()
                start_city = elems[0]
                to_city = elems[2]
                cost = int(elems[4])
                cities[start_city].append(Edge(name=to_city, cost=cost))
                cities[to_city].append(Edge(name=start_city, cost=cost))
    else:
        print "Please provide a filename."
    return cities

def make_dset(x):
    t = DSet()
    t.parent = t
    t.name = x
    return t

def weight(u, v, cities):
    for c in cities[u]:
        if c.name == v:
            return c.cost

def find_set(x):
    if x.parent is x:
        return x
    else:
        return find_set(x.parent)

def union_set(x,y):
    x_root = find_set(x)
    y_root = find_set(y)
    x_root.parent = y_root


def make_ordered_set(cities):
    rl = set()
    for v,l in cities.iteritems():
        for e in l:
            if not (e.name, v, e.cost) in rl:
                tup = (v, e.name, e.cost)
                rl.add(tup)
    return sorted(rl, key=lambda x: x[2])


cities = city_map() # Our adjacency list

paths = set()
for (p,q,c) in make_ordered_set(cities):
    u = make_dset(p)
    v = make_dset(q)
    print int(c)
    if find_set(u) is not find_set(v):
        paths.add((u,v, c))
        union_set(u,v)
res = 0
for p in paths:
    res += p[2]

print res
print paths
