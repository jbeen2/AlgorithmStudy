def solution(price, money, count):
    answer = sum([i*price for i in range(count+1)]) - money
    if answer >= 0 : return answer
    else : return 0

print(solution(3, 20, 4))