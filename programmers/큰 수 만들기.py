# ㅠㅠ 어떻게 하면 될 것 같은데 어떻게 못 하겠다 ..

def solution(number, k):
    length = len(number) - int(k)

    answer = []

    if len(number) == k :
        answer.append(number)
    else :
        n = length - 1
        answer = []
        while n > 0 :
            check = number[:-n]
            break
    return length


number, k = map(str, input().split())
print(solution(number, k))