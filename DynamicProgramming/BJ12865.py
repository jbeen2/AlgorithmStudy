N, K = map(int, input().split())
bag = [[0,0]] + sorted([list(map(int, input().split())) for _ in range(N)]) # key=lambda x : (-x[1], x[0]))

'''
knapsack[i][j] = max(현재 물건 가치 + knapsack[이전 물건][현재 가방 무게 - 현재 물건 무게], knapsack[이전 물건][현재 가방 무게])
knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
'''

knapsack = [[0]*(K+1) for _ in range(N+1)]
for i in range(1,N+1) :
    for j in range(1,K+1) :
        w = bag[i][0] ; v = bag[i][1]
        if j < w :
            knapsack[i][j] = knapsack[i-1][j]
        else :
            knapsack[i][j] = max(v+knapsack[i-1][j-w], knapsack[i-1][j])
print(knapsack[N][K])



# 느낌은 비슷한데 ㅠㅠ 조금만 더 생각하면 좋았을 듯
# d1, d2 = [0]*100001, [0]*100001 # w, v
# for i in range(len(bag)) :
#     if K >= bag[i][0] : # K보다 큰 W가 입력으로 들어올 때
#         d1[i] += bag[i][0] ; d2[i] += bag[i][1]
#         for j in range(i+1, N) :
#             if K-d1[i] >= bag[j][0] :
#                 d1[i] += bag[j][0] ; d2[i] += bag[j][1]
# print(max(d2))


'''
test case 1 
3 5
4 2
3 4
1 5

ans : 9 


test case 2 
2 1 
2 2 
2 2 

ans : 0 


test case 3 
4 8
6 13
4 8
4 6
5 12

ans : 14 


test case 4 
4 2
1 1
5 1
5 1
1 1

ans 2

test cases [정답] != [오답]
wrong! 264 != 263 * 
7 19
9 89
8 80
1 32
6 68
2 74
3 42
7 2
wrong! 23 != 22 
6 9
3 6
2 7
4 6
4 2
4 10
1 5
wrong! 31 != 29 * 
9 10
1 8
5 10
4 10
2 6
4 5
4 7
3 7
4 7
1 4
wrong! 26 != 25
6 7
3 7
3 10
1 6
2 7
3 5
2 9
wrong! 19 != 18 
7 9
3 6
2 4
2 5
3 4
1 3
4 1
2 4
wrong! 20 != 18
7 7
1 4
3 1
3 6
2 6
3 8
3 4
2 6
wrong! 17 != 16 * 
5 9
2 4
1 3
3 5
4 8
2 1
wrong! 31 != 28
8 9
1 4
2 7
3 10
2 7
2 7
4 8
3 5
4 1
wrong! 38 != 37 * 
9 10
4 2
4 9
1 5
1 7
2 8
3 9
2 8
2 6
3 5
wrong! 21 != 20 * 
5 7
3 8
1 5
2 7
2 2
2 6
wrong! 30 != 29 * 
10 10
1 2
4 9
1 5
4 8
4 1
1 7
3 2
3 7
2 5
5 2
wrong! 24 != 23
9 7
1 1
1 4
3 10
2 1
2 7
3 8
3 9
3 3
2 7
wrong! 37 != 36
9 9
2 9
1 7
3 10
2 2
3 3
4 9
2 10
2 8
3 2
'''