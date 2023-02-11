import sys
input = sys.stdin.readline

N = int(input())
costs = []
for i in range(N):
    costs.append(list(map(int,input().split())))
dp = [[0]*3 for _ in range(N)]
print(dp)
for i in costs:
    min_cost = 0
    min_idx = i.index(min(i))
    for j in range(i-1):
        