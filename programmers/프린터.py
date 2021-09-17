from collections import deque
def solution(priorities, location):
    answer = 0 ; prt = deque([(p, i) for i, p in enumerate(priorities)])
    while len(prt) :
        check = prt.popleft()
        if prt and check[0] < max(prt)[0] :
            prt.append(check)
        else :
            answer += 1
            if check[1] == location :
                break
    return answer


# Example
priorities = [2, 1, 3, 2] ; location = 2
# priorities = [1, 1, 9, 1, 1, 1] ; location = 0

print(solution(priorities, location))