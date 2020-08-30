# 런타임 에러가 날 때는 아주 작은 숫자나, 아주 큰 숫자인 경우를 생각해 보자 ...
n = int(input())
stair = [int(input()) for _ in range(n)]


d = [0]*301
d[0] = stair[0]

if n == 2 :
    d[1] = d[0] + stair[1]

if n >= 3 :
    d[1] = d[0] + stair[1]
    d[2] = max(stair[1]+stair[2] , d[0]+stair[2])

    for i in range(3,n) :
        d[i] = max(stair[i-1]+d[i-3], d[i-2])+stair[i]

# def solve(n) :
#     if d[n] > 0 :
#         return d[n]
#
#     d[n] = max(stair[n-1]+solve(n-3), solve(n-2))+stair[n]
#     return d[n]
#
# for i in range(3,n) :
#     d[i] = solve(i)

print(d[n-1])
print(d)