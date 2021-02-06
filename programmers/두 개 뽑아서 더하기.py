def solution(numbers):
    from itertools import combinations
    idx = list(combinations([i for i in range(len(numbers))], 2))

    answer = []
    for i in idx:
        answer.append(numbers[i[0]] + numbers[i[1]])

    return sorted(list(set(answer)))


# 다른 사람 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))