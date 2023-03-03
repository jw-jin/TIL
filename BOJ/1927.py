import sys
import heapq
input = sys.stdin.readline
N = int(input())
min_h = []
for _ in range(N):
    x = int(input())

    if(x == 0):
        if(len(min_h) != 0):
            tmp = heapq.heappop(min_h)
            print(tmp)
        else:
            print(0)
    else:
        heapq.heappush(min_h,x)        
