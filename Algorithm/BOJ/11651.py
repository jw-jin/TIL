N = int(input())

coord = []

for i in range(N):
    x, y = input().split()
    coord.append([int(x),int(y)])

coord.sort()
coord.sort(key=lambda x:x[1])
for i in coord:
    print(i[0],i[1])
