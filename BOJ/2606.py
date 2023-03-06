from collections import deque
n = int(input())
m = int(input())

def bfs(arr):
    global n
    visited = [0] * (n+1)
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        nd = q.popleft()
        for i in arr[nd]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    
    return visited



arr = {}
for _ in range(m):
    x, y = map(int,input().split())
    if x not in arr:
        arr[x] = [y]
    else:
        arr[x].append(y)
    if y not in arr:
        arr[y] = [x]
    else:
        arr[y].append(x)

res = bfs(arr)
print(sum(res)-1)