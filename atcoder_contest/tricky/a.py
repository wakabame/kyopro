import sys

n = int(input())

mem_limit = 3 * (10**6)
while True:
    st = sys.stdin.read(mem_limit)
    if len(st) == mem_limit:
        while True:
            app = sys.stdin.read(1)
            if app == "\n":
                break
            else:
                st += app
    else:
        if st in ["\n", ""]:
            break
    A = list(map(int, st.split()))

    for a, b in zip(A[::2], A[1::2]):
        print(abs(a) // abs(b) * (1 - ((a > 0) ^ (b > 0)) * 2))
