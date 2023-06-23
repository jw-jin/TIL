import sys
input = sys.stdin.readline

N, M, B = map(int,input().split())

# 제거 2초 쌓기 1초
land = []
land_height = {}
times = []
for i in range(N):
    m_input = list(map(int,input().split()))
    land.append(m_input)

min_height = min(map(min, land))
max_height = max(map(max, land))
res_height = 0
res_time = 9e9
for h in range(min_height,max_height+1): #i[0] 땅높이 i[1] 그 높이를 가진 땅
    time = 0
    block = 0
    for i in range(N):
        for j in range(M):
            land_h = land[i][j]
            if(land_h > h):
                blockcnt = land[i][j] - h
                time += blockcnt * 2
                block -= blockcnt
            elif(land_h < h):
                blockcnt = h - land[i][j]
                time += blockcnt
                block += blockcnt

    if(block<=B):
        if(res_time>=time and res_height<=h):
            res_time = time
            res_height = h


print(res_time, res_height)
            