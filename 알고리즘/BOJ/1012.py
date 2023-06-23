import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

T = int(input())
def dfs(y,x):
    global visited,field,M,N
    visited[y][x] = 1
    move = [[-1,0],[1,0],[0,-1],[0,1]] # 상하좌우
    for m in move:
        movex = x + m[1]
        movey = y + m[0]
        if(movex < 0 or movey < 0 or movex>=M or movey>=N):
            continue
        if(visited[movey][movex] == 1 or field[movey][movex] == 0):
            continue
        dfs(movey,movex)

for i in range(T):
    M,N,K = map(int,input().split())
    field = [[0] * M for _ in range(N)]
    visited  = [[0] * M for _ in range(N)]
    for _ in range(K):
        x,y = map(int,input().split())
        field[y][x] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if(field[i][j] == 1 and visited[i][j] != 1):
                dfs(i,j)
                cnt+=1
    print(cnt)


