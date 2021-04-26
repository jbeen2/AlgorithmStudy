# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**6)        # 이거 안 하면 런타임 에러

N = int(input())
road, cost = list(map(int, input().split())), list(map(int, input().split()))
answer = road[0] * cost[0]
price = cost[0]    # 가장 처음의 값 넣어 놓기

def oil(road, cost, answer, price) :
    if len(cost) == 1 :
        return answer
    a, b = cost.pop(0), road.pop(0)  # cost, road 리스트에서 가장 처음의 값 꺼내기
    if a <= price :                  # 꺼낸 값이 지금까지의 최솟값보다 작으면
        answer += a * b              # 꺼낸 값으로 곱하기
        price = a                    # price update
    else :                           # 꺼낸 값이 더 크다면
        answer += price * b          # 그냥 냅둬라 ..
    return oil(road, cost, answer, price)

print(oil(road[1:], cost[1:], answer, price))



# ===== 간단한 코드 ... =====
minVal = cities[0]
sum = 0
for i in range(N-1):
    if minVal > cities[i]:
        minVal = cities[i]
    sum += (minVal * roads[i])