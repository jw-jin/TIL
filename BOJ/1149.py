import sys
input = sys.stdin.readline

N = int(input())
costs = []
for i in range(N):
    costs.append(list(map(int,input().split())))

res = 0

costs_sum = [[0] * 3 for _ in range(N)] 
for i in range(3):
    costs_sum[0][i] = costs[0][i]
for i in range(1, len(costs)):
    cost = [0] * 3
    cost[0] = min(costs_sum[i-1][1],costs_sum[i-1][2])
    cost[1] = min(costs_sum[i-1][0],costs_sum[i-1][2])
    cost[2] = min(costs_sum[i-1][0],costs_sum[i-1][1])
    
    for j in range(3): # 012
        costs_sum[i][j] += cost[j] + costs[i][j]

print(min(costs_sum[N-1]))






# res = 0
# painted[0][costs[0].index(min(costs[0]))] = 1
# res += min(costs[0])
# min_cost = 1001
# for i in range(1, len(costs)):
#     costs_sum = {}
#     for a in range(3):
#         for b in range(3):
#             if(a!=b):
#                 costs_sum[a,b] = (costs[i-1][a] + costs[i][b])
    
#     costs_sum = sorted(costs_sum.items(), key=lambda x:x[1])

#     fail = 1
#     for j in costs_sum:
#         # j[0] = 인덱스 두개
#         # j[1] = 비용
#         if(min_cost >= j[1]): # 
#             min_cost = j[1]
#             if(sum(painted[i-1]) == 1):
#                 for k in range(3):
#                     if(painted[i-1][k] == 1):
#                         res-=costs[i-1][k]
#                         painted[i-1][k] = 0
#                         break
#             painted[i-1][j[0][0]] = 1
#             painted[i][j[0][1]] = 1
#             res += min_cost
#             break
    
#     if(fail == 1):
#         min_cost = costs_sum[0][1]
#         painted[i][costs_sum[0][0][1]] = 1
#         res += min_cost - costs[i-1][costs_sum[0][0][0]]
#     print(costs_sum)
#     print(min_cost)
        


# print(painted)
# print(res)



"""
89 86 83

96

"""