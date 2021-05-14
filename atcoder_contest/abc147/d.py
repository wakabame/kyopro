N = int(input())
A = list(map(int, input().split()))

MOD = 10 ** 9 + 7
ans = 0
for digit in range(60):
    # 桁を固定して, その桁の貢献を計算する
    # 要素が二つ選ばれたとき, 片方が1, もう片方が0 のときに xor が 1 となる
    # したがって, (1 の個数) × (0 の個数) がその桁での貢献になる
    zero_count = 0
    one_count = 0
    for a in A:
        if a & (1 << digit):
            one_count += 1
        else:
            zero_count += 1

    ans += one_count * zero_count * pow(2, digit, MOD)
    ans %= MOD
print(ans)
