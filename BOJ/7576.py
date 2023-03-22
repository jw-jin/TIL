#BOJ 7576 토마토
# M 가로 칸수 N 세로 칸수
# 1 익음 0 안익음 -1 없음 2 다음날 익음
from collections import deque
import sys
input = sys.stdin.readline
movex = [0,0,-1,1] # 상 하 좌 우
movey = [1,-1,0,0]

def bfs(arr,arr1,m,n,visited):
    q = deque(arr1)
    xsum = len(arr1)
    days = 0
    qcnt = 0
    xcnt = 0
    qlen = len(q)
    
    while q:
        
        y,x = q.popleft()
        
        
        if arr[y][x] == 1:
            for i in range(4):
                mx = x+movex[i]; my = y+movey[i]
                if mx < 0 or my < 0 or mx>= m or my>=n : 
                    continue
                if arr[my][mx] == -1 or arr[my][mx] == 1:
                    continue
                arr[my][mx] = 1
                xcnt +=1
                q.append([my,mx])
        visited[y][x] = 1
        
        qcnt += 1
        
        

        if qcnt >= qlen:
            days +=1
            xsum += xcnt
            xcnt = 0
            qcnt = 0
            qlen = len(q)
            
        if (n*m)-chkm1 <= xsum:
            return days

    return days       

M,N = map(int,input().split())

visited = [[0] * M for i in range(N)]
arr = []

for _ in range(N):
    arr.append(list(map(int,input().split())))

chk0 = 0
global chkm1
chkm1 = 0
flag = 0
flag_limit = 4
arr1 = []
for i in range(N):
    if(flag == flag_limit):
        break
    for j in range(M):
        if(flag == flag_limit):
            break
        if arr[i][j] == 1:
            arr1.append([i,j])
        elif arr[i][j] == 0:
            chk0 += 1
            flag = 0
            flag_limit = 4
            for k in range(4):
                if flag == flag_limit:
                    break
                my = i+movey[k];  mx = j+movex[k]
                if(my<0 or mx<0 or my>=N or mx>= M):
                    flag_limit -=1
                    continue
                if arr[my][mx] == -1:
                    flag +=1
                    continue
        elif arr[i][j] == -1:
            chkm1 += 1


if flag == flag_limit:
    print(-1)
elif chk0 == 0:
    print(0)
else:
    res = bfs(arr,arr1,M,N,visited)
    print(res)