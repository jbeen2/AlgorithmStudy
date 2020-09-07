T = int(input())
for _ in range(T) :
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    prev= [[0]*n for _ in range(2)]

    prev[0][0] = sticker[0][0]
    prev[1][0] = sticker[1][0]

    prev[0][1] = prev[1][0] + sticker[0][1]
    prev[1][1] = prev[0][0] + sticker[1][1]


    for i in range(2, n) :
        prev[0][i] = max(prev[1][i-1], prev[1][i-2])+sticker[0][i]
        prev[1][i] = max(prev[0][i-1], prev[0][i-2])+sticker[1][i]


    print(max(prev[0][n-1], prev[1][n-1]))