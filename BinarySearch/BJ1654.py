K, N = map(int, input().split())
line = [int(input()) for _ in range(K)]

def binary_search(target):
    start, end = 1, max(line)
    answer = 0
    while start <= end:
        m = 0
        mid = (start + end) // 2
        for x in line:
            if x >= mid:
                m += x // mid
        if m < target:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer

print(binary_search(N))