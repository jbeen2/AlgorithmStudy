# -*- coding: utf-8 -*-
N = int(input())
d = [0] * (N+2)
d[2] = 3

# [i] = 이전의 경우의 수 * 3 + 이전의 경우의 수들 * 2 + i만 만드는 경우 (2)
for i in range(4, N+1, 2) :
    d[i] = 2 + d[i-2] * 3 + sum(d[:i-3]) * 2

print(d[N])