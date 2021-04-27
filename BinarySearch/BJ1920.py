N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
X = list(map(int, input().split()))

def binary_search(target) :
    start, end = 0, N-1
    while start <= end :
        mid = (start + end) // 2
        if A[mid] == target :
            return mid
        elif A[mid] < target :
            start = mid + 1
        else :
            end = mid - 1
    return None

for i in X :
    answer = binary_search(i)
    print(1 if answer != None else 0)