from itertools import permutations, combinations, product
import re
from random import random
from functools import reduce, cache
from _md5 import md5
from operator import mul
from math import sqrt
from collections import defaultdict, Counter


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def hash(inp):
    return md5(inp.encode()).hexdigest()


def avg(inp):
    return sum(inp)/len(inp)


def printAnswer(result: tuple):
    print("[P1]", result[0])
    print("[P2]", result[1])


def deltas(iter):
    return [iter[n]-iter[n-1] for n in range(1, len(iter))]


def prod(iter):
    return reduce(mul, iter)


def imaginaryCoordToDist(n: complex):
    return int(abs(n.real)) + int(abs(n.imag))


def imaginaryCoordToTuple(n: complex):
    return (int((n.real)), int((n.imag)))


def im2tup(n: complex):
    return imaginaryCoordToTuple(n)


def im2dist(n: complex):
    return imaginaryCoordToDist(n)


def im2prod(n: complex):
    return int(abs(n.real)) * int(abs(n.imag))


def imSub(a, b):
    x1, y1 = im2tup(a)
    x2, y2 = im2tup(a)
    return crd2im(x1-x2, y1-y2)


def tup2im(tup):
    return tup[0]+1j*tup[1]


def crd2im(x, y):
    return x+1j*y


def crange(start, stop, step):
    d = imNorm(stop-start)
    while start != stop:
        yield start
        start += d


def norm(n):
    if n == 0:
        return 0
    return int(n/abs(n))


def imNorm(z):
    x, y = im2tup(z)
    x = norm(x)
    y = norm(y)
    return crd2im(x, y)


def readNums(inp):
    return list(map(int, re.findall(r"(-?\d+)", inp)))


def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def lcm(x, y):
    lcm = (x*y)//gcd(x, y)
    return lcm


def modMult(a, b, mod):
    res = 0
    a = a % mod
    while b:
        if b & 1:
            res = (res+a) % mod
        a = (a*2) % mod
        b >>= 1
    return res


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if not n % i)))

# x = a1 mod n1
# x = a2 mod n2


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod//n_i
        sum += a_i * mul_inv(p, n_i)*p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def printSet(toColor, point="#", space=' '):
    lx = hx = ly = hy = 0
    for p in toColor:
        x, y = imaginaryCoordToTuple(p)
        lx = min(lx, x-1)
        ly = min(ly, y)
        hx = max(hx, x+1)
        hy = max(hy, y+1)
    out = "\n"
    for y in range(ly, hy):
        for x in range(lx, hx):
            if (x + y*1j) in toColor:
                out += point
            else:
                out += space
        out += '\n'
    return out


def printCoords(coords, default=" "):
    # format of {pos:val}
    lx = hx = ly = hy = 0
    for p in coords.keys():
        x, y = imaginaryCoordToTuple(p)
        lx = min(lx, x)
        ly = min(ly, y)
        hx = max(hx, x)
        hy = max(hy, y)
    out = ""
    for y in range(ly, hy+1):
        for x in range(lx, hx+1):
            if (x + y*1j) in coords:
                out += str(coords[(x+y*1j)])
            else:
                out += default
        out += '\n'
    return out[:-1]


def gridify(input, mapping=None):
    points = {}
    for y, row in enumerate(input.splitlines()):
        for x, v in enumerate(row):
            if mapping != None:
                if callable(mapping):
                    points[x+y*1j] = mapping(v)
                else:
                    points[x+y*1j] = mapping(v)
            else:
                points[x+y*1j] = v
    return points


def dist(a, b):
    assert(len(a) == len(b))
    s = 0
    for x, y in zip(a, b):
        s += (y-x)**2
    return sqrt(s)


def manhattan(a, b):
    assert len(a) == len(b)
    return sum(abs(x-y) for x, y in zip(a, b))


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def sub(a, b):
    return tuple(x-y for x, y in zip(a, b))


def rot(coords):
    a, b, c = coords

    yield (+a, +b, +c)
    yield (+b, +c, +a)
    yield (+c, +a, +b)
    yield (+c, +b, -a)
    yield (+b, +a, -c)
    yield (+a, +c, -b)
    yield (+a, -b, -c)
    yield (+b, -c, -a)
    yield (+c, -a, -b)
    yield (+c, -b, +a)
    yield (+b, -a, +c)
    yield (+a, -c, +b)
    yield (-a, +b, -c)
    yield (-b, +c, -a)
    yield (-c, +a, -b)
    yield (-c, +b, +a)
    yield (-b, +a, +c)
    yield (-a, +c, +b)
    yield (-a, -b, +c)
    yield (-b, -c, +a)
    yield (-c, -a, +b)
    yield (-c, -b, -a)
    yield (-b, -a, -c)
    yield (-a, -c, -b)


def hash(a, b):
    out = str(dist(a, b))
    out += ","
    out += str(min(abs(x-y) for x, y in zip(a, b)))
    out += ","
    out += str(max(abs(x-y) for x, y in zip(a, b)))
    return out


class Scanner:
    def __init__(self, inp):
        self.id = readNums(inp.splitlines()[0])[0]
        self.beacons = [tuple(readNums(l)) for l in inp.splitlines()[1:]]
        self.hashes = [hash(a, b) for a, b in permutations(self.beacons, 2)]


def main(input: str):
    p2 = 0
    knownPos = {0: (0, 0, 0)}  # scanner 0 known
    scanners = [Scanner(x) for x in input.split("\n\n")]
    while len(knownPos) < len(scanners):
        for a, b in combinations(scanners, 2):
            if (len(set(a.hashes) & set(b.hashes)) == 66):  # 12 choose 2
                if((a.id in knownPos) != (b.id in knownPos)):
                    if b.id in knownPos:
                        a, b = b, a
                    t = list(zip(*[list(rot(p)) for p in b.beacons]))
                    for rotset in t:
                        c = Counter()
                        for p in rotset:
                            c += Counter([sub(n, p) for n in a.beacons])
                            ans = [k for k, v in c.items() if v >= 12]
                            if len(ans):
                                knownPos[b.id] = add(
                                    [k for k, v in c.items() if v >= 12][0], knownPos[a.id])
                                b.beacons = rotset
                                break
                        if b.id in knownPos:
                            break
    p1 = set()
    for sn in scanners:
        for p in sn.beacons:
            p1.add(add(p, knownPos[sn.id]))
    for a in knownPos.values():
        for b in knownPos.values():
            p2 = max(p2, manhattan(a, b))
    return (len(p1), p2)


with open('19.in') as infile:
    input = infile.read()

print(main(input))
