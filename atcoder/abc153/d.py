H = int(input())

def rec(h):
    if h == 1:
        return 1
    return 2 * rec(h//2) + 1

print(rec(H))