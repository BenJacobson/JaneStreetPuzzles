class Die:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.front = None
        self.back = None
    
    def roll_forward(self):
        d = Die()
        d.top, d.front, d.bottom, d.back = self.back, self.top, self.front, self.bottom
        d.left = self.left
        d.right = self.right
        return d
    
    def roll_backwards(self):
        d = Die()
        d.top, d.front, d.bottom, d.back = self.front, self.bottom, self.back, self.top
        d.left = self.left
        d.right = self.right
        return d

    def roll_left(self):
        d = Die()
        d.top, d.left, d.bottom, d.right = self.right, self.top, self.left, self.bottom
        d.front = self.front
        d.back = self.back
        return d
    
    def roll_right(self):
        d = Die()
        d.top, d.left, d.bottom, d.right = self.left, self.bottom, self.right, self.top
        d.front = self.front
        d.back = self.back
        return d

board = [
    [0, 77, 32, 403, 337, 452],
    [5, 23, -4, 592, 445, 620],
    [-7, 2, 357, 452, 317, 395],
    [186, 42, 195, 704, 452, 228],
    [81, 123, 240, 443, 353, 508],
    [57, 33, 132, 268, 492, 732],
]

def solution(seen, die):
    for row in reversed(seen):
        print(row)

    ans = 0
    for i in range(6):
        for j in range(6):
            if seen[i][j] == 0:
                ans += board[i][j]
    print(ans)

    print('Die')
    print(die.top, die.front, die.bottom, die.back, die.left, die.right)

def search(i, j, move_num, die, score, seen):
    if move_num > 0:
        if not (0 <= i < 6 and 0 <= j < 6):
            return
        
        if die.top is None:
            diff = board[i][j] - score
            if abs(diff) % move_num != 0:
                return
            diff //= move_num
            die.top = diff
        
        score += die.top * move_num

        if score != board[i][j]:
            return
    
    seen[i][j] += 1

    if i == 5 and j == 5:
        solution(seen, die)
    else:
        search(i-1, j, move_num+1, die.roll_backwards(), score, seen)
        search(i+1, j, move_num+1, die.roll_forward(), score, seen)
        search(i, j-1, move_num+1, die.roll_left(), score, seen)
        search(i, j+1, move_num+1, die.roll_right(), score, seen)

    seen[i][j] -= 1

def solve():
    seen = [[0] * len(row) for row in board]
    search(0, 0, 0, Die(), 0, seen)

if __name__ == '__main__':
    solve()
