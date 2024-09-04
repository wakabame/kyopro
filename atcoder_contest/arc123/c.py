from collections import defaultdict

T = int(input())
for t in range(T):
    c = int(input())
    ans_dict1 = defaultdict(int)
    ans_dict2 = defaultdict(int)
    curr1, curr2 = 0, 0  # curr1 はover, curr2 は過小
    for i in range(1, 19)[::-1]:
        elem = int("1" * i)
        if curr1 + elem <= c:  # 足りない場合は足す
            shortage = c - curr1
            ct = (shortage) // elem
            ans_dict1[i] += ct
            curr1 += ct * elem
        if curr2 - elem > c:  # 過剰な場合は引く
            over = curr2 - c
            ct = (over + elem - 1) // elem
            ans_dict2[i] -= ct
            curr2 -= ct * elem
        if curr2 + elem < c:
            shortage = c - curr2
            ct = (shortage + elem - 1) // elem
            ans_dict2[i] += ct
            curr2 += ct * elem

    break
print(ans_dict1, ans_dict2)
