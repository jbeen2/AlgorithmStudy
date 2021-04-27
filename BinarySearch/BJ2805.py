N, M = map(int, input().split())
tree = list(map(int, input().split()))

def binary_search(target) :
    start, end = 0, max(tree)
    answer = 0
    while start <= end :
        m = 0
        mid = (start + end) // 2
        for x in tree :
            if x > mid :
                m += x - mid
        if m < target :
            end = mid - 1
        else :
            answer = mid
            start = mid + 1
    return answer

print(binary_search(M))