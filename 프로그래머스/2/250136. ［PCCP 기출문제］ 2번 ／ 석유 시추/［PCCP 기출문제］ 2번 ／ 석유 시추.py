from collections import deque, defaultdict

scores = defaultdict()
visited_dict = defaultdict()

def bfs(x,y,land,visited):
    move = [[-1,0],[1,0],[0,-1],[0,1]]
    visited[y][x] = True
    q = deque([(x,y)])
    minx = x
    maxx = x
    cnt = 1
    while q:
        qx, qy = q.popleft()
        for i in range(4):
            nx = qx + move[i][1]
            ny = qy + move[i][0]
            if nx < 0 or ny < 0 or nx >= len(land[0]) or ny >= len(land):
                continue
            if land[ny][nx] == 0:
                continue
            if visited[ny][nx] == False:
                visited[ny][nx] = True
                minx = min(minx, nx)
                maxx = max(maxx, nx)
                q.append((nx,ny))
                cnt+=1
    return minx, maxx, cnt

def solution(land):
    x_len = len(land[0])
    y_len = len(land)
    res = [0] * x_len
    visited = [[False] * x_len for _ in range(y_len)]
    for i in range(x_len):
        cnt=0
        for j in range(y_len):
            if land[j][i] == 1 and visited[j][i] == False:
                minx,maxx, cnt = bfs(i,j,land,visited)
                #print(i,j,cnt,minx,maxx)
                for x in range(minx,maxx+1):
                    res[x] += cnt 


    return max(res)