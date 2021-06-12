N = int(input())
C = [int(input()) for _ in range(N)]

def LIS(L):
    from bisect import bisect_left
    seq = []
    for ai in L:
        pos = bisect_left(seq, ai)
        if len(seq) <= pos:
            seq.append(ai)
        else:
            seq[pos] = ai
    return len(seq)

print(N - LIS(C))
