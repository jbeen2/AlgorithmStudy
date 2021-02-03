def solution(n):
    # 재귀함수
    def convert(m, base):
        T = "0123456789ABCDEF"
        q, r = divmod(m, base)
        if q == 0:
            return T[r]
        else:
            return convert(q, base) + T[r]

    answer1 = str(convert(n, 3))[::-1]
    answer2 = int(answer1, 3)

    return answer2


# 다른 풀이
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer