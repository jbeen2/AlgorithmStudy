def solution(arr):
    arr.remove(min(arr))
    return arr if len(arr) > 1 else [-1]

# return 에서 바로 arr.remove(min(arr)) 하면 Null 나온다.. 왜일까... 알 수가 없다...