# 약수는 제곱근까지 ~ range(1, int(n**0.5+1))!

def solution(brown, yellow):
    # brown = (a+b+2) * 2 , yellow = a*b
    # answer = [a+2, b+2]

    # yellow 세로 길이 후보 
    b2 = [i for i in range(1, int(yellow ** 0.5) + 1) if yellow % i == 0]

    # yellow 가로 길이 후보 
    a2 = [yellow // b for b in b2]

    answer = []
    for a, b in zip(a2, b2):
        if (a + b + 2) * 2 == brown:
            answer.extend([a + 2, b + 2])

    return answer