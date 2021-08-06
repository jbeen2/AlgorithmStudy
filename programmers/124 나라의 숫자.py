def solution(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return solution(q) + '124'[r]


# 효율성 ㅠ_ㅠ 시간 초과 ~~~!!

def solution2(n):
    num = ['1', '2', '4']
    k = 3
    while n >= k :
        tmp1 = ['1'+i for i in num[-k:]]
        tmp2 = ['2'+i for i in num[-k:]]
        tmp4 = ['4'+i for i in num[-k:]]

        num.extend(tmp1)
        num.extend(tmp2)
        num.extend(tmp4)

        k *= 3
    return num[n-1]


def solution3(n) :
    # answer = [''] * (n+1)
    # if n <= 3 :
    #     answer[n] = '124'[n-1]
    # else :
    #     q, r = divmod(n-1, 3)
    #     answer[n] = answer[q] + '124'[r]

    answer = ['', '1', '2', '4'] + ['']*(n)
    for i in range(4, n+1) :
        q, r = divmod(i-1, 3)
        answer[i] = answer[q] + '124'[r]
    return answer[n]


print(solution(2))
