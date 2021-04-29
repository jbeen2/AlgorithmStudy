N, C = map(int, input().split())
house = sorted([int(input()) for _ in range(N)])

def binary_search(C) :
    start, end = 1, house[-1] - house[0]
    distance = 0
    while start <= end :
        count, prev = 1, house[0]
        mid = (start + end) // 2
        for h in house :
            if (h-prev) >= mid :
                count += 1
                prev = h
        if count < C :
            end = mid - 1
        else :
            start = mid + 1
            distance = mid
    return distance

print(binary_search(C))
