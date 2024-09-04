from math import gcd
from collections import defaultdict


def to_irreducible(a, b):
    if a == 0:
        return (0, 1)
    GCD = gcd(a, b)
    return (a // GCD, b // GCD)


MOD = 10**9 + 7
N = int(input())
quadrant1 = defaultdict(int)
quadrant2 = defaultdict(int)
zero_cases = 0

for i in range(N):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        zero_cases += 1
    elif a * b >= 0 and b != 0:
        irr = to_irreducible(abs(a), abs(b))
        quadrant1[irr] += 1
    else:
        irr = to_irreducible(abs(b), abs(a))
        quadrant2[irr] += 1
        quadrant1[irr] += 0

ans = 1
for key, v1 in quadrant1.items():
    v2 = quadrant2[key]
    ans *= 2**v1 + 2**v2 - 1
    ans %= MOD
print((ans + zero_cases - 1) % MOD)
