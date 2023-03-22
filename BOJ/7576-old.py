#BOJ 7576 토마토
# M 가로 칸수 N 세로 칸수
# 1 익음 0 안익음 -1 없음 2 다음날 익음
import copy

M,N = map(int,input().split())

arr = []
movex = [0,0,-1,1] # 상 하 좌 우
movey = [1,-1,0,0]
for _ in range(N):
    arr.append(list(map(int,input().split())))

chkm1 = 0
chk0 = 0
days = 0
flag = 0
flag_limit = 4


for i in range(N):
    for j in range(M):
        if arr[i][j] == -1:
            chkm1 +=1 
        elif arr[i][j] == 0:
            chk0 += 1
 
while True:
    chk1 = 0
    if chk0 == 0:
        break
    if(flag == flag_limit):
        break
    chk_arr = copy.deepcopy(arr)
    for i in range(N):
        if(flag == flag_limit):
            break
        for j in range(M):
            if(flag == flag_limit):
                break
            if arr[i][j] == 0:
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
            elif arr[i][j] == 1:
                for k in range(4):
                    my = i+movey[k];  mx = j+movex[k]
                    if(my<0 or mx<0 or my>=N or mx>= M):
                        continue
                    if arr[my][mx] == -1 or arr[my][mx] == 1:
                        continue
                    arr[my][mx] = 2

    if(flag != flag_limit):
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    arr[i][j] = 1
                    chk1 +=1
                elif arr[i][j] == 1:
                    chk1 +=1
    
    days += 1
    if (N*M)-chkm1 <= chk1:
        break
    if chk_arr == arr:
        days = -1
        break

print(days)