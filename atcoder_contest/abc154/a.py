S, T = map(str, input().split())
A, B = map(int, input().split())

dic = {S: A, T: B}
U = input()
dic[U] = dic[U]-1
print(dic[S], dic[T])