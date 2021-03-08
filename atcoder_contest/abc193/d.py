K = int(input())
S = input()[:-1]
S = [int(k) for k in S]
T = input()[:-1]
T = [int(k) for k in T]

rem = [K] * 10
for i in S:
    rem[i] -= 1
for i in T:
    rem[i] -= 1

def calc_score(cards):
    card_count = [0] * 10
    for number in cards:
        card_count[number] += 1
    score = 0
    for i in range(1,10):
        score += i * (10 ** card_count[i])
    return score

ans_denominator = 0
ans_numerator = 0

for j in range(1,10):
    for k in range(1,10):
        if j != k:
            case_count = rem[j] * rem[k]
        else:
            case_count = rem[j] * (rem[j]-1)
        takahashi_score = calc_score(S + [j])
        aoki_score = calc_score(T +[k])
        if takahashi_score > aoki_score:
            ans_numerator += case_count
        ans_denominator += case_count

print(ans_numerator/ans_denominator)