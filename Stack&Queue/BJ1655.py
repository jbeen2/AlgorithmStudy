# 푸는 중!!!

# Priority Queue : 들어간 순서에 상관없이 우선순위가 높은 데이터가 먼저 나오는 것
# PriorityQueue().queue : 작은 순서대로 정렬되어 있지 않음 ..

import sys
import heapq
N, que = int(sys.stdin.readline()), []

def medium(nums, k):
    que = nums.copy()
    kth_medium = None
    for _ in range(k):
        kth_medium = heapq.heappop(que)
        print(que)
    return kth_medium

for i in range(1,N+1) :
    n = int(sys.stdin.readline())
    heapq.heappush(que, n)

    if i%2 == 0 : print(medium(que, i//2-1)) ; print("idx", i//2-1)
    else : print(medium(que, i//2)) ; print("idx", i//2)


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