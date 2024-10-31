# Expected: 74649600

G = [
    "-5-6-36---74",
    "-771--5-465-",
    "---7535-6-6-",
    "643--7-571--",
    "7---2742---7",
    "2-666--637-4",
    "544-7--7-625",
    "7---1571--7-",
    "-537-5--5-46",
    "65---72-6--5",
    "-673--4554--",
    "---4637--37-",
]

seen = set()
ans = 1

def dfs(i, j):
    if not (0 <= i < 12 and 0 <= j < 12):
        return 0
    
    if G[i][j] != '-':
        return 0
    
    if (i, j) in seen:
        return 0
    
    seen.add((i, j))

    return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)

for i in range(12):
    for j in range(12):
        if G[i][j] == '-' and (i, j) not in seen:
            s = dfs(i, j)
            if s > 1:
                print(s)
            ans *= s

print(ans)
