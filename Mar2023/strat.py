from random import uniform

def jump(limit):
    p = 0.0

    while p < limit:
        p += uniform(0.0, 1.0)
    
    if p > 1.0:
        return 0.0

    p += uniform(0.0, 1.0)

    return p

def first_wins(limit1, limit2):
    wins1 = 0
    wins2 = 0

    for _ in range(10_000_000):
        robot1 = jump(limit1)
        robot2 = jump(limit2)

        if robot1 > robot2:
            wins1 += 1
        elif robot1 < robot2:
            wins2 += 1
    
    return wins1 > wins2

l = 0.35
r = 0.45
d = 0.001

while l + d < r:
    print(l, r)
    mid1 = l + (r - l) / 3
    mid2 = r - (r - l) / 3

    if not first_wins(mid1, mid1+d):
        l = mid1
    
    if first_wins(mid2, mid2+d):
        r = mid2

print(l, r)

# The optimal strategy seems to be jump after .4
