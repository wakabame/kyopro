X, Y, A, B, C = map(int, input().split())

p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort(reverse = True)
q.sort(reverse = True)
r.sort(reverse = True)

candidate = p[:X] + q[:Y] + r[:X+Y]
candidate.sort(reverse = True)

print(sum(candidate[:X+Y]))