# Priority Queue : 들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나오는 것
import sys
import heapq
N = int(sys.stdin.readline())
small, big = [], []
for i in range(N) :
    n = int(sys.stdin.readline())
    if len(small) == len(big) : heapq.heappush(small, (-n,n))
    else : heapq.heappush(big, (n,n))

    if big and small[0][1] > big[0][1] :
        a = heapq.heappop(small)[1] ; b = heapq.heappop(big)[1]
        heapq.heappush(small, (-b, b)) ; heapq.heappush(big, (a, a))

    print(small[0][1])



# 시간초과 ...
# import sys
# import heapq
# import copy
# N, que = int(sys.stdin.readline()), []
#
# def medium(nums, k):
#     que = copy.deepcopy(nums) # 이거 때문에 시간초과 나는듯 ..
#     kth_medium = None
#     for _ in range(k):
#         kth_medium = heapq.heappop(que)
#     return kth_medium
#
# for i in range(1,N+1) :
#     n = int(sys.stdin.readline())
#     heapq.heappush(que, n)
#     if i%2 == 0 : print(medium(que, i//2))
#     else : print(medium(que, i//2+1))


# PriorityQueue().queue : (list) 작은 순서대로 정렬되어 있지 않음 ..
# import sys
# from queue import PriorityQueue
# N = int(sys.stdin.readline())
# que = PriorityQueue()
#
# def medium(nums, k):
#     kth_medium = None
#     for _ in range(k):
#         kth_medium = que.get()
#     return kth_medium
#
# for i in range(1,N+1) :
#     n = int(sys.stdin.readline())
#     que.put(n)
#     if i%2 == 0 : print(medium(que, i//2-1)) ; print("idx", i//2-1)
#     else : print(medium(que, i//2)) ; print("idx", i//2)