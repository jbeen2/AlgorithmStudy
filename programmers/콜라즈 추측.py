def solution(num):
    answer = 0
    while True:
        if num % 2 == 0:
            num = num//2
            answer += 1

        else:
            if num != 1 :
                num= (num*3) + 1
                answer += 1
            else :
                return answer

        if answer>=500:
            return -1
            break


num = int(input())
print(solution(num))