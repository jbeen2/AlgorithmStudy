# https://eda-ai-lab.tistory.com/465?category=766271
def solution(number, k):
    stack = [number[0]]

    for num in number[1:] :
        while len(stack) > 0 and stack[-1] < num and k > 0 :
            k -= 1
            stack.pop()
        stack.append(num)

    if k != 0 :
        stack = stack[:-k]
    return ''.join(stack)


# 이런식으로 풀지 말고.. stack 으로 풀어야 함.. 왜냐면 max 로 풀면 시간초과 나기 때문에......
# def solution(number, k):
#     length = len(number) - int(k)
#     answer = []
#
#     def maxnum(number, length) :
#         if length == 0 :
#             answer.append(number)
#         else :
#             n = length
#             print("n : ", n )
#
#             while n > 0:
#                 check = number[:-n]
#                 print("check : ", check)
#
#                 answer.append(max(check))
#                 new = number[number.index(max(check)) + 1 : ]
#                 print("new : ", new)
#                 length -= 1
#                 print("new length : ", length)
#                 print("========")
#
#                 if n == 1:
#                     answer.append(max(new))
#                     break
#
#                 return maxnum(new, length)
#
#
#
#     print(maxnum(number, length))
#     print(answer)
#     print(length)

number, k = map(str, input().split())
print(solution(number, k))