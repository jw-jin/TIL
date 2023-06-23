# boj 9251 LCS
import sys
input = sys.stdin.readline
N = input().strip(); M = input().strip(); nlen = len(N); mlen = len(M)

res = 0
dp = [[0] * (mlen+1) for _ in range(nlen+1)]
for i in range(1,nlen+1):
    for j in range(1,mlen+1):
        if N[i-1] == M[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[nlen][mlen])


    