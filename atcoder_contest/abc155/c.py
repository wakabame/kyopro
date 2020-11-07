N = int(input())

dic = {}
for i in range(N):
    s = input()
    if s not in dic:
        dic[s] = 1
    else:
        dic[s] += 1

dictlist = []
for key, value in dic.items():
    temp = [key,value]
    dictlist.append(temp)
dictlist.sort(key=lambda x:(-x[1], x[0]))

top = dictlist[0][1]
for i in range(len(dictlist)):
    if dictlist[i][1] == top:
        print(dictlist[i][0])