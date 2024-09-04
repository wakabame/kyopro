N = int(input())


# 木の直径を出すには最短距離計算を2回行う
# 一度目は, 適当な頂点を根と見なして, そこから最も遠い頂点 = 直径の端点をみつける
# BFS でも DFS でもよい（以下はDFSで実装）
# 二度目は, その頂点から最短距離を計算し, 最も遠い頂点 = 直径ももう一端 との距離を算出
distance_from_one = [-1] * (N + 1)
distance_from_one[1] = 0

for i in range(1, N + 1):
    if i == 1:
        continue
    else:
        print("?", 1, i)
        ret = int(input())
        distance_from_one[i] = ret

root_index = distance_from_one.index(max(distance_from_one))
distance_from_root = [-1] * (N + 1)
distance_from_root[root_index] = 0

for i in range(1, N + 1):
    if i == root_index:
        continue
    else:
        print("?", root_index, i)
        ret = int(input())
        distance_from_root[i] = ret

print("!", max(distance_from_root))
