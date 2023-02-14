from itertools import combinations
N,M = input().split()
N = int(N)
M = int(M)

info = []
ch_info = []
def get_chic_len(info):
    global N
    chic_len = 0
    for i in range(N):
        for j in range(N):
            if(info[i][j] == 1):
                min_len = (N*N)+1
                for x in range(N):
                    for y in range(N):
                        if(info[x][y] == 2):
                            tmp_len = abs((i-x)) + abs((j-y))
                            if(tmp_len < min_len):
                                min_len = tmp_len
                chic_len+= min_len 
    return chic_len

#dp = [[-1] * N for i in range(N)]
ch_cnt = 0
for i in range(N):
    info.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        if(info[i][j] == 2):
            ch_info.append([i,j])
res = get_chic_len(info)
test_info = info
chic_len_info = []
bomb_list = list(combinations(ch_info, len(ch_info) - M))
if(len(bomb_list) != 0):
    for i in bomb_list:
        for j in i:
            test_info[j[0]][j[1]] = 0
        chic_len_info.append(get_chic_len(test_info))
        for j in i:
            test_info[j[0]][j[1]] = 2


if(len(chic_len_info) == 0):
    print(res)
else:
    print(min(chic_len_info))
            
    
