n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
print(tri)


answer = [tri[0]]
def dp(tri, n) :
    for i in range(len(tri[n])-1) :
        print(answer[n-1][i] + tri[n][i])
        print(answer[n-1][i] + tri[n][i+1])
    return [[answer[n-1][i] + tri[n][i], answer[n-1][i] + tri[n][i+1]] for i in range(len(tri[n])-1)]

for i in range(1, n) :
    answer.append(dp(tri, i))
    print(dp(tri, i))

print()
dp(tri, 1)
print(dp(tri, 2))
print(answer)
