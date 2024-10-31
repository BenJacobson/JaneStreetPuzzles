from random import uniform

jump = 0.4
total = 10_000_000
discard = 0

for _ in range(total):
    p = 0.0
    while p < jump:
        p += uniform(0.0, 1.0)
    if p > 1.0:
        discard += 1

print(f"{100*discard/total:.2f}% scores 0")

# The answer seems to be roughly 10.5%