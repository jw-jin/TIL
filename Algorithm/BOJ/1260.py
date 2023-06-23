import sys
from collections import deque
input = sys.stdin.readline
N, M, V = map(int, input().split())


def dfs(v):
    global visited,lines
    visited[v] = 1
    print(v,end=" ")
    for i in lines[v]:
        if(visited[i] == 0):
            dfs(i)

            
        

def bfs(v):
    global visited,lines
    q = deque()
    q.append(v)
    visited[v] = 1
    while(q):
        n = q.popleft()
        print(n, end=" ")
        for i in lines[n]:
            if(visited[i] == 0):
                q.append(i)
                visited[i] = 1

lines = [[] for _ in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    lines[x].append(y)
    lines[y].append(x)

for i in range(N+1):
    lines[i].sort()

visited = [0] * (N+1)
dfs(V)
print()
visited = [0] * (N+1)
bfs(V)


"""
정점 n 간선 m 시작번호 v
1 2 3 4
2 4
3 4
"""