import sys
input = sys.stdin.readline
N = int(input())

info = []
for i in range(N):
    info.append(list(map(int,input().split())))

info.sort(key=lambda x:(x[1], x[0]))

res = 0
end_time = -1
for i in range(N):    
    if info[i][0] >= end_time:
        res+=1
        end_time = info[i][1]
print(res)


"""
12 ~ 14
0 ~ 6
"""

# 실패 빈도순
# import sys
# input = sys.stdin.readline
# N = int(input())

# info = []
# st_time = []
# ed_time = []
# for i in range(N):
#     info.append(list(map(int,input().split())))

# max_val = max(map(max,info))

# use_time = [0] * (max_val+1)
# for st,ed in info:
#     for i in range(st,ed+1):
#         use_time[i]+=1


# score = []
# for i in range(N):    
#     res = 0
#     for j in range(info[i][0],(info[i][1]+1)):
#         res += use_time[i]
#     score.append([res,i])

# score.sort(key=lambda x:x[0])

# times = [0] * (max_val+1)
# cnt = 0
# for i in range(N):
#     st = info[score[i][1]][0]
#     ed = info[score[i][1]][1]
#     flag = 0
#     for j in range(st,ed+1):
#         if(times[j] == 0):
#             times[j] = 1
#         else:
#             flag = 1
#             break
#     if(flag==1):
#         continue
#     cnt+=1

# print(cnt)
# """
# 12 ~ 14
# 0 ~ 6
# """