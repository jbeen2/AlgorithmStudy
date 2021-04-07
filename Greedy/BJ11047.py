# -*- coding: utf-8 -*-

N, K = map(int, input().split())
coins = sorted([int(input()) for _ in range(N)], reverse=True)

count = 0
for coin in coins :
    if K == 0 : break   # 시간 단축! 
    count += K // coin
    K %= coin

print(count)