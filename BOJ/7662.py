import sys
from heapq import heappush, heappop
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    chk = {}
    for _ in range(k):
        cmd = list(input().split())
        if(cmd[0] == 'I'):
            x = int(cmd[1])
            heappush(min_heap, x)
            heappush(max_heap, -x)  
            chk[x] = True
            chk[-x] = True
        elif(cmd[0] == 'D'):
            if(cmd[1] == '1'):
                if(max_heap):
                    val = heappop(max_heap)
                    chk[val] = False
                    while True:
                        if(chk[-val] == False):
                            if(max_heap):
                                val = heappop(max_heap)
                                chk[val] = False
                            else:
                                break
                        else:
                            break
            else:
                if(min_heap):
                    val = heappop(min_heap)
                    chk[val] = False
                    while True:
                        if(chk[-val] == False):
                            if(min_heap):
                                val = heappop(min_heap)
                                chk[val] = False
                            else:
                                break
                        else:
                            break
    
    res = []
    for i in range(len(max_heap)):
        max_heap[i] = -max_heap[i]
    set_res = list(set(min_heap) & set(max_heap))
    for v in set_res:
        if(chk[v] and chk[-v]):
            res.append(v)
    if(min_heap):
        print(max(res), min(res))
        
    else:
        print("EMPTY")


