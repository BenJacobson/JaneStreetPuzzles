import matplotlib.pyplot as plt
from random import uniform

jump = 0.5

def u():
    return uniform(0.0, 1.0)

def attempt():
    at = 0
    while at < jump:
        at += u()
        if at > 1.0:
            return 0.0
    return at + u()

iters = 1_000_000
data = []
zero = 0
for _ in range(iters):
    result = attempt()
    if result > 0:
        data.append(result)
    else:
        zero += 1

print(f"zero {100*zero/iters:.2f}")

num_bins = 1000

fig, ax = plt.subplots()

# the histogram of the data
n, bins, patches = ax.hist(data, num_bins, density=True)
ax.set_xlabel('Score')
ax.set_ylabel('Probability density')

# Tweak spacing to prevent clipping of ylabel
fig.tight_layout()
plt.show()