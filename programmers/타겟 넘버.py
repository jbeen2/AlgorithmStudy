# 1. BFS
from collections import deque
def solution(numbers, target) :
    answer, n = 0, len(numbers)
    queue = deque()

    queue.append([numbers[0] , 0])  # value, index
    queue.append([numbers[0] * (-1) , 0])

    while queue :
        a, idx = queue.popleft()
        idx += 1

        if idx < n :
            queue.append([a + numbers[idx], idx])
            queue.append([a - numbers[idx], idx])

        else :
            if a == target :
                answer += 1

    return answer

print(solution([1,1,1,1,1], 3))


# 2. DFS
def solution3(numbers, target) :
    answer, n = 0, len(numbers)

    def dfs(idx, result) :
        if idx == n :
            if result == target :
                nonlocal answer
                answer += 1

        else :
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])

    dfs(0, 0)
    return answer

print(solution3([1,1,1,1,1], 3))


# 3. Recursive
def solution2(numbers, target) :
    if not numbers and target == 0 :
        return 1
    elif not numbers :
        return 0
    else :
        return(solution2(numbers[1:], target-numbers[0]) + solution2(numbers[1:], target+numbers[0]))