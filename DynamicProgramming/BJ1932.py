n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
answer = [tri[0]]

for i in range(1, n) :
    tmp = []
    for j in range(len(tri[i])) :
        if j == 0 :
            tmp.append(answer[i-1][j] + tri[i][j])
        elif j == len(tri[i])-1 :
            tmp.append(answer[i-1][-1] + tri[i][-1])
        else :
            tmp.append(max(answer[i-1][j-1], answer[i-1][j]) + tri[i][j])
    answer.append(tmp)

print(max(answer[-1]))