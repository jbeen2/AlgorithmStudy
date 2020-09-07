T = int(input())
# solve : s부터 e까지의 파일을 합친 최소 비용


for _ in range(T) :
    N = int(input())
    arr = list(map(int, input().split()))
    sum_arr = [0] * N

    for i in range(1, N) :
        sum_arr[i] = sum_arr[i-1] + arr[i]

    memo = [[-1] * 501 for _ in range(501)]
    print(solve(s, e))
