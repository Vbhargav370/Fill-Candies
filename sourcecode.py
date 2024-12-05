import math
t = int(input())
for _ in range(t):
    N,K,M = map(int, input().split())
    each_bag = K*M
    need_bag = N/each_bag
    print(math.ceil(need_bag))
