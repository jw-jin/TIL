N = int(input())


arr = []

for _ in range(N):
    arr.append(list(map(int,input().split())))   


for i in range(N):
    for j in range(N):
        for k in range(N):
            if(arr[j][i] and arr[i][k]):
                arr[j][k] = 1
            
for i in arr:
    for j in i:
        print(j, end=' ')
    print()
"""
ij jk ik
ji kj ki
정점 i에서 j로 가는 경로가 있으면 
i번째 줄의 j번째 숫자를 1로, 
없으면 0으로 출력해야 한다.
i
1~4
4~5
4~6


"""