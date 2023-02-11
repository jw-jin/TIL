N = int(input())

res = []
for i in range(N):
    x,y = map(int,input().split())
    res.append([x,y])

res.sort()
for i in res:
    print(i[0],i[1])

