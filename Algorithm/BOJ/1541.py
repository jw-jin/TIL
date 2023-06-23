import sys
input = sys.stdin.readline

arr = input().strip().split('-')

num = []
for i in arr:
    minus = 0
    n = i.split('+')
    for j in n:
        minus += int(j)
    num.append(minus)

n = num[0]
for i in range(1,len(num)):
    n-=num[i]

print(n)