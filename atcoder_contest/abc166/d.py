import sys

X = int(input())

A = 0
while True:
    for B in range(A + 1):
        if A**5 + B**5 == X:
            print(A, -B)
            sys.exit()
        if A**5 - B**5 == X:
            print(A, B)
            sys.exit()
        if -(A**5) + B**5 == X:
            print(-A, -B)
            sys.exit()
    A += 1
