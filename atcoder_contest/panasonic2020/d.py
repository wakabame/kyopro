N = int(input())

def standard_string(N, st):
    if len(st) == N:
        print(st)
    elif st == "":
        standard_string(N, "a")
    else:
        for i in range(97, ord(max(st))+ 2):
            st += chr(i)
            standard_string(N, st)
            st = st[:-1]
standard_string(N, "")