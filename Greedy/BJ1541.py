# -*- coding: utf-8 -*-
eq = input().split('-')

answer = sum([int(t) if t != "+" else 0 for t in eq[0].split("+")])
for e in range(1, len(eq)) :
    tmp = eq[e].split('+')
    answer -= sum([int(t) if t != "+" else 0 for t in tmp])

print(answer)



# ==========================================
# eval 사용하면 '0' 으로 시작하는 경우에 문제가 생김..
# ==========================================
#
# answer = eval(eq[0])
# if len(eq) > 1 :
#     for i in range(1, len(eq)) :
#         answer -= eval(eq[i])