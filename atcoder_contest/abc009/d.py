import numpy as np
import numba

K, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
MOD = 1 << 64  # 使っていない


# DP の漸化式が同じ場合は, 行列の繰り返し二乗法によって求めることができる
# 非負整数に対して, 和: xor, 積: and の半環（xorの単位元は -1(unsigned int)）とみなすことができる
def power_matrix_under_mod(mat, n, p):
    res = np.identity(K, dtype=np.uint32) * -1
    bi = str(format(n, "b"))  # 2進表現に
    for i in range(len(bi)):
        res = multiple_and_matrix(res, res)
        # res = np.mod(res, p)
        if bi[i] == "1":
            res = multiple_and_matrix(res, mat)
            # res = np.mod(res, p)
    return res


# 3重ループは numba に任せる
@numba.jit
def multiple_and_matrix(mat1, mat2):
    res = np.zeros((K, K), dtype=np.uint32)
    for i in range(K):
        for j in range(K):
            for k in range(K):
                res[i][j] ^= mat1[i][k] & mat2[k][j]

    return res


def calc_and_xor(mat, arr):
    ret = 0
    for i in range(K):
        ret ^= arr[i] & mat[-1][i]
    return ret


# 行列の累乗を行う
dp_matrix = np.zeros((K, K), dtype=np.uint32)
for i in range(K - 1):
    dp_matrix[i][i + 1] = -1
dp_matrix[-1] = np.array(C[::-1])

if M <= K:
    print(A[M - 1])
else:
    print(calc_and_xor(power_matrix_under_mod(dp_matrix, M - K, MOD), A))
