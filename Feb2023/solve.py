N = None
G = [
    [0, 0, 6, 3, 7, 0, 4],
    [0, 0, 7, 0, 6, 2, 5],
    [5, 7, N, N, N, N, N],
    [5, 0, N, N, N, N, N],
    [7, 2, N, N, N, N, N],
    [0, 4, N, N, N, N, N],
    [3, 7, N, N, N, N, 0],
]
# G = [
#     [N, N, N, N, N, N, N],
#     [N, N, N, N, N, N, N],
#     [N, N, N, N, N, N, N],
#     [N, N, N, N, N, N, N],
#     [N, N, N, N, N, N, N],
#     [N, N, N, N, N, N, N],
#     [N, N, N, N, N, N, N],
# ]

col_sum = [0] * 8
row_sum = [0] * 8
col_count = [0] * 8
row_count = [0] * 8
col_blank = [0] * 8
row_blank = [0] * 8
used = [0] * 8

def print_grid():
    for row in G:
        print(*row)
    print()

def is_solved():
    for i in range(7):
        if col_count[i] != 4 or row_count[i] != 4 or col_sum[i] != 20 or row_sum[i] != 20:
            return False
    
    for i in range(1, 8):
        if used[i] != i:
            return False
    
    if [c for c in G[-1] if c > 0][-1] != 7:
        return False
    
    if [r[-1] for r in G if r[-1] > 0][-1] != 5:
        return False
    
    return True

def search(i, j):
    if i == 7:
        if is_solved():
            print_grid()
        return
    
    ni, nj = i, j+1
    if nj == 7:
        nj = 0
        ni += 1
    
    if G[i][j] is not None:
        if G[i][j] != 0:
            col_sum[j] += G[i][j]
            row_sum[i] += G[i][j]
            col_count[j] += 1
            row_count[i] += 1
            used[G[i][j]] += 1
        else:
            col_blank[j] += 1
            row_blank[i] += 1
        
        search(ni, nj)

        if G[i][j] != 0:
            col_sum[j] -= G[i][j]
            row_sum[i] -= G[i][j]
            col_count[j] -= 1
            row_count[i] -= 1
            used[G[i][j]] -= 1
        else:
            col_blank[j] -= 1
            row_blank[i] -= 1
        
        return
    
    # print_grid()
    
    for o in range(8):
        G[i][j] = o
        if o > 0:
            col_sum[j] += o
            row_sum[i] += o
            col_count[j] += 1
            row_count[i] += 1
            used[o] += 1
        else:
            col_blank[j] += 1
            row_blank[i] += 1
        
        if col_sum[j] <= 20 and row_sum[i] <= 20 and col_count[j] <= 4 and row_count[i] <= 4 and used[o] <= o and col_blank[j] <= 3 and row_blank[i] <= 3 and \
            (row_blank[i] + row_count[i] < 7 or row_sum[i] == 20) and (col_blank[j] + col_count[j] < 7 or col_sum[j] == 20):
            search(ni, nj)
        
        G[i][j] = N
        if o > 0:
            col_sum[j] -= o
            row_sum[i] -= o
            col_count[j] -= 1
            row_count[i] -= 1
            used[o] -= 1
        else:
            col_blank[j] -= 1
            row_blank[i] -= 1

search(0, 0)
