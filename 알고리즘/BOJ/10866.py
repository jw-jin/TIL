import sys
from itertools import combinations
input = sys.stdin.readline
#nCr = n-1Cr + n-1Cr-1

N,K = input().split()
N = int(N)
K = int(K)
tmplist = [[0,0] for i in range(N)]

res = list(combinations(tmplist,K))
print(len(res))
