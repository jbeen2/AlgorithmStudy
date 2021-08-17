# Priority Queue
import sys
from queue import PriorityQueue
N = int(sys.stdin.readline())
que = PriorityQueue()
for _ in range(N) :
    item = int(sys.stdin.readline())
    if item > 0 : que.put(item)
    else :
        if que.qsize() != 0 : print(que.get())
        else : print(0)