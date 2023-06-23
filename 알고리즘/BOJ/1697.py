from collections import deque
N, K = input().split()
N = int(N) ; K = int(K)

def find(N):
    global K
    visited = [0] * 100001
    visited[N] = 1
    q = deque()
    q.append([N,0])
    time = 0
    while q:
        n = q.popleft()
        if n[0] == K :
            return n[1]
        arr = [n[0]+1, n[0]-1, n[0]*2]
        for i in arr:
            if i < 0 or i > 100000:
                continue
            if visited[i] == 0:
                q.append([i, n[1]+1])
                visited[i] = 1

# 순간이동 1초 2*X 로 이동
# 걸으면 1초 X+1 X-1 이동
# N = 5 dest = 17
# 
cnt = 0
graph = {}

res = find(N)

print(res)

