# 1929 소수구하기
# 에라토스테네스의 체
import math

m,n= map(int, input().split())

arr = [1 for i in range(n+1)]

for i in range(2,int(math.sqrt(n))+1):
    if (arr[i] == 1):
        x = 2
        while(i*x <= n):
            arr[i*x] = 0
            x += 1
            

for i in range(m, n+1):
    if(arr[i] == 1 and i !=1):
        print(i)

