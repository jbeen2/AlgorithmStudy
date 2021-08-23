import heapq
def solution(scoville, K):
    heapq.heapify(scoville) ; answer = 0
    while True :
        if len(scoville) > 1 :
            a = heapq.heappop(scoville) ; b = heapq.heappop(scoville)
            s = a + b*2
            heapq.heappush(scoville, s)
            answer += 1
            c = heapq.heappop(scoville)
            if c >= K : break
            else : heapq.heappush(scoville, c)
        else :
            return -1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
print(solution(scoville, 7))