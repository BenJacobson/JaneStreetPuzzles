from collections import defaultdict
from functools import partial

board = [
    'ABBCCC',
    'ABBCCC',
    'AABBCC',
    'AABBCC',
    'AAABBC',
    'AAABBC',
]

k_moves = (
    (2, 1),
    (-2, 1),
    (2, -1),
    (-2, -1),
    (1, 2),
    (-1, 2),
    (1, -2),
    (-1, -2),
)

def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def is_in_range(pos):
    return 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0])

def cmp_pos(curr):
    return lambda npos:board[curr[0]][curr[1]] != board[npos[0]][npos[1]]

def get_paths(curr, end, seen, path, all_paths):
    if len(all_paths) >= 100_000:
        return
    if curr == end:
        all_paths.append(tuple(path))
        assert(len(path) == len(set(path)))
        return
    
    moves = sorted(filter(is_in_range, map(partial(add, curr), k_moves)), key=cmp_pos(curr))
    for npos in moves:
        if not is_in_range(npos):
            continue
        if npos in seen:
            continue
        seen.add(npos)
        path.append(npos)
        get_paths(npos, end, seen, path, all_paths)
        path.pop()
        seen.remove(npos)

start1 = (5, 0)
end1 = (0, 5)
paths1 = []
get_paths(start1, end1, {start1}, [start1], paths1)

start2 = (0, 0)
end2 = (5, 5)
paths2 = []
get_paths(start2, end2, {start2}, [start2], paths2)

class Polynomial:
    def __init__(self, vars):
        self.vars = vars
        self.val = defaultdict(int)
    
    def add_var(self, var_i):
        self.val[tuple(int(i == var_i) for i in range(self.vars))] += 1
    
    def mult_var(self, var_i):
        nval = defaultdict(int)
        for k, v in self.val.items():
            nk = tuple(k[i] + (i==var_i) for i in range(self.vars))
            nval[nk] = v
        self.val = nval
    
    def solve(self, values):
        assert(len(values) == self.vars-1)
        ret = []
        for k, v in self.val.items():
            a = v
            for i, val in enumerate(values):
                a *= pow(val, k[i])
            ret.append([a, k[-1]])
        return ret
    
    def __str__(self):
        return str(self.val)
    
    def __hash__(self):
        return hash(tuple((self.vars, *sorted((k, v) for k, v in self.val.items()))))
    
    def __eq__(self, other):
        return hash(self) == hash(other)

def path_to_polynomial(path):
    p = Polynomial(3)
    last = 'A'
    for pos in path:
        curr = board[pos[0]][pos[1]]
        if last == curr:
            p.add_var(ord(curr) - ord('A'))
        else:
            p.mult_var(ord(curr) - ord('A'))
        last = curr
    return p

polynomials1 = list(map(path_to_polynomial, paths1))
polynomials2 = list(map(path_to_polynomial, paths2))

def apply_val(poly, c):
    ret = 0
    for m, p in poly:
        ret += m*pow(c,p)
    return ret

def search(target, poly, low, high):
    if apply_val(poly, low) > target:
        return None
    if apply_val(poly, high) < target:
        return None
    while low + 1 < high:
        mid = (low + high) // 2
        midv = apply_val(poly, mid)
        if midv == target:
            return mid
        elif midv > target:
            high = mid
        else:
            low = mid
    return None

def path_to_string(path):
    s = ''
    for a, b in path:
        s+=chr(ord('a')+b)
        s+=str(6-a)
        s+=','
    return s[:-1]


for a in range(1, 26):
    for b in range(1, 26):
        matches = dict()
        for i, p in enumerate(polynomials1):
            cm = p.solve([a, b])
            cv = search(2024, cm, 1, 50)
            if cv is not None:
                matches[(a, b, cv)] = i
        for i, p in enumerate(polynomials2):
            cm = p.solve([a, b])
            cv = search(2024, cm, 1, 50)
            if cv is not None and (a, b, cv) in matches:
                print(f'{a},{b},{cv},{path_to_string(paths1[matches[(a, b, cv)]])},{path_to_string(paths2[i])}')
