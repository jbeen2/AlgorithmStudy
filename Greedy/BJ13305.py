N = int(input())
road, cost = list(map(int, input().split())), list(map(int, input().split()))
answer = 0

print("road : ", road)
print("cost : ", cost)

def oil(road, cost, answer) :

    a, b = cost.pop(0), road.pop(0)
    print(cost)

    if a <= cost[0] :
        answer += a * b
    else :
        answer += cost[0] * b

    print(answer)

    return oil(road, cost, answer)

while cost :
    oil(road, cost, answer)
print(answer)