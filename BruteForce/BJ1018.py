# -*- coding: utf-8 -*-

N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
answer = []

for n in range(N-7) :
    for m in range(M-7) :
        num1, num2 = 0, 0  # set1, set2

        for i in range(n, n+8) :
            for j in range(m, m+8) :
                if (i+j) % 2 == 0 :  # i+j 짝수인 경우, 홀수인 경우 색이 똑같이 칠해진다
                    if chess[i][j] != "W" : num1 += 1
                    if chess[i][j] != "B" : num2 += 1

                else :
                    if chess[i][j] != "B" : num1 += 1
                    if chess[i][j] != "W" : num2 += 1

        answer.append(min(num1, num2))

print(min(answer))


# ================ 내가 푼 답안 ================

num1 , num2 = max(N+1, 8) - 8, max(M+1, 8) - 8  # 세로, 가로
chess1 , chess2 = ['B','W','B','W','B','W','B','W'], ['W','B','W','B','W','B','W','B']
set1 , set2 = [chess1, chess2] * 4 , [chess2, chess1] * 4

check = []
for i in range(num1):
    for j in range(num2) :
        tmp = [chess[i][j:j+8], chess[i+1][j:j+8], chess[i+2][j:j+8], chess[i+3][j:j+8],
               chess[i+4][j:j+8], chess[i+5][j:j+8], chess[i+6][j:j+8], chess[i+7][j:j+8]]
        check.append(tmp)

answer = []
for ch in check :
    if (ch != set1) and (ch != set2) :

        # set1
        a = 0
        for c, s in zip(ch, set1) :
            if c != s :
                for k, l in zip(c,s) :
                    if k != l :
                        a += 1

        # set2
        b = 0
        for c, s in zip(ch, set2):
            if c != s:
                for k, l in zip(c, s):
                    if k != l:
                        b += 1

        answer.append(min(a,b))

    else :
        answer.append(0)


print(min(answer))