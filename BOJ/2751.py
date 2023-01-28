N = int(input())
res = []
for i in range(0,N):
    num = int(input())
    res.append(num)

res.sort()

for i in res:
    print(i)