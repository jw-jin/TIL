from collections import deque

def bfs(graph, st):
    kv_num = 0
    depth = 0
    visited = []
    q = deque()
    q.append(st)
    visited.append(st)
    while q:
        for _ in range(len(q)):
            nd = q.popleft()
            kv_num += depth
            for i in graph[nd]:
                if i not in visited:
                    q.append(i)
                    visited.append(i)
        depth +=1
    return kv_num

N,M = input().split()
N = int(N); M = int(M)


graph = {}
for _ in range(M):
    x = list(map(int,input().split()))
    if x[0] in graph:
        graph[x[0]].append(x[1])
    else:
        graph[x[0]] = [x[1]]
    if x[1] in graph:
        graph[x[1]].append(x[0])
    else:
        graph[x[1]] = [x[0]]

for i in range(1,N+1):
    tmp = set(graph[i])
    graph[i] = tmp 


res = [0] * (N+1)
res[0] = 9e9
#1=6 2=8 3=5 4=5 5=8
# 12 = 2 13 = 1 14= 1 15= 2

for i in range(1,len(res)):
    res[i] = bfs(graph,i)
print(res.index(min(res)))


