# Priority Queue
import sys
from queue import PriorityQueue
N = int(sys.stdin.readline())
que, answer = PriorityQueue(), 0
for i in range(N) :
    que.put(int(sys.stdin.readline()))

while True :
    if que.qsize() == 1 :
        break
    a = que.get() ; b = que.get()
    answer += (a+b)
    que.put(a+b)

print(answer)