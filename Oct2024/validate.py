"""
1,2,23,a1,b3,c1,a2,b4,c2,a3,b1,c3,d1,b2,a4,b6,c4,a5,c6,d4,b5,d6,f5,e3,d5,f6,a6,b4,c2,a1,b3,c1,a2,c3,d1,b2,a4,b6,c4,d2,b1,a3,b5,d4,e6,f4,d5,f6,e4,d6,f5,e3,f1
1,3,8,a1,b3,c1,a2,b4,c2,a3,b1,c3,d1,b2,d3,c5,a4,b6,d5,f6,a6,b4,c2,a1,b3,c1,a2,c3,d1,b2,a4,b6,c4,d2,b1,a3,b5,d4,e6,f4,d5,e3,f1
3,1,2,a1,b3,c1,a2,b4,c2,a3,b1,c3,b5,d6,f5,e3,c4,d2,e4,f2,d1,b2,d3,c5,a4,b6,d5,f6,a6,b4,c2,a1,b3,c1,a2,c3,d1,f2,e4,f6,d5,f4,e6,d4,b5,a3,b1,d2,f3,e1,d3,b2,c4,e3,f1
"""

board = [
    'ABBCCC',
    'ABBCCC',
    'AABBCC',
    'AABBCC',
    'AAABBC',
    'AAABBC',
]

def convert_path_entry(entry):
    return (6-int(entry[1]), ord(entry[0])-ord('a'))

def convert_path(path):
    path = path.split(',')
    path = [convert_path_entry(entry) for entry in path]
    return path

def validate_path(path, a, b, c):
    if len(path) != len(set(path)):
        return False
    for i in range(1, len(path)):
        curr = path[i]
        last = path[i-1]
        check = sorted([abs(curr[0] - last[0]), abs(curr[1] - last[1])])
        if check != [1, 2]:
            return False
    
    vals = {'A':a, 'B':b, 'C':c}
    last = 'A'
    total = 0
    for i, j in path:
        letter = board[i][j]
        if letter == last:
            total += vals[letter]
        else:
            total *= vals[letter]
        last = letter
    return total == 2024

def validate(a, b, c, path1, path2):
    path1 = convert_path(path1)
    if not validate_path(path1, a, b, c):
        print('error in path1')
        return False
    path2 = convert_path(path2)
    if not validate_path(path2, a, b, c):
        print('error in path2')
        return False

validate(3, 1, 2, 'a1,b3,c1,a2,b4,c2,a3,b1,c3,b5,d6,f5,e3,c4,d2,e4,f2,d1,b2,d3,c5,a4,b6,d5,f6', 'a6,b4,c2,a1,b3,c1,a2,c3,d1,f2,e4,f6,d5,f4,e6,d4,b5,a3,b1,d2,f3,e1,d3,b2,c4,e3,f1')
