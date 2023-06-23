import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())


def dfs(y,x,color):
    global visited,grid,N
    visited[y][x] = 1
    move = [[-1,0],[1,0],[0,-1],[0,1]] # 상하좌우
    for m in move:
        movex = x + m[1]
        movey = y + m[0]
        if(movex < 0 or movey < 0 or movex>=N or movey>=N):
            continue
        if(visited[movey][movex] == 1 or grid[movey][movex] != color):
            continue
        dfs(movey,movex,color)

grid = []
for _ in range(N):
    input_str = input()
    input_arr = []
    for i in input_str:
        input_arr.append(i)
    grid.append(input_arr)


visited = [[0] * N for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(N):
        if(visited[i][j] == 0):
            dfs(i,j,grid[i][j])
            cnt+=1

visited = [[0] * N for _ in range(N)]
cnt_rg = 0
for i in range(N):
    for j in range(N):
        if(grid[i][j] == 'G'):
            grid[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if(visited[i][j] == 0):
            dfs(i,j,grid[i][j])
            cnt_rg+=1

print(cnt,cnt_rg)




