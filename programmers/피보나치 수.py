# bottom-up
def solution(n):
    arr = [0]*(n+1)
    arr[0] = 0
    arr[1] = 1
    for i in range(2,n+1):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[n]%1234567


# 다른 사람 풀이
def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a