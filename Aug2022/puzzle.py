import msvcrt

raw_grid = """
ytimoiczryzwbus
tegcirbpylkoorb
retpemplompilzy
erhighlipetzxiz
btmloisterslicp
isstopestreetrk
llteczerepzucze
almeptrzlfzrkue
oztbropxyoolegs
ewjfkoreztowpzt
uigrzpcmeptrzlz
ttzlmopeyislzpc
zerzuqsposiczui
tlepputcpzllohu
srzbzyypewnseuu
"""

grid = []
for line in raw_grid.split('\n'):
    line = line.strip()
    if len(line) > 0:
        grid.append([*line])

for row in grid:
    assert(len(grid) == len(row))

dirs = (
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
)
search = ''

def green(string):
    return f"\033[92m{string}\033[0m"

def follow(i, j, dir, idx, matches):
    if idx == len(search):
        return True
    
    if not (0 <= i < len(grid) and 0 <= j < len(grid) and grid[i][j] == search[idx]):
        return False
    
    found = follow(i+dir[0], j+dir[1], dir, idx+1, matches)
    if found:
        matches[i][j] = True
    return found

def search_grid():
    matches = [[False]*len(grid) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            for dir in dirs:
                follow(i, j, dir, 0, matches)
    for i in range(len(grid)):
        for j in range(len(grid)):
            letter = green(grid[i][j]) if matches[i][j] else grid[i][j]
            print(letter, end='')
        print()

while 1:
    c = msvcrt.getch()[0]
    if 97 <= c <= 122:
        search += chr(c)
    elif c == 8 and len(search) > 0:
        search = search[:-1]
    elif c == 27:
        exit()
    
    print()
    print('----')
    print(search)
    print('----')
    search_grid()

"""
notes
no: vd
what is the mew?
"""
