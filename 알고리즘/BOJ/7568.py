import sys
input = sys.stdin.readline

N = int(input())
arr = []
rank = [1] * N
for i in range(N):
    w, h = input().split()
    arr.append([int(w),int(h)])
    
for i in range(len(arr)):
    for j in range(len(arr)):
        if(i != j):
            if(arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]):
                rank[i] += 1

for i in rank:
    print(i, end=' ') 