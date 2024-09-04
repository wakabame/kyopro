def LIS(Lis):
    from bisect import bisect

    seq = []
    for i in Lis:
        pos = bisect(seq, i)
        if len(seq) <= pos:
            seq.append(i)
        else:
            seq[pos] = i
    return len(seq)


N = int(input())
a = list(map(int, input().split()))
print(LIS(a))
