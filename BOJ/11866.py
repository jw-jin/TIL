#11866 BOJ 요세푸스 문제 0
import sys
input = sys.stdin.readline

N,K = map(int,input().split())

li = list(range(1,N+1))
idx = K-1
res = []
while(len(li)>0):
    res.append(li.pop(idx))
    idx = idx - 1 + K
    
    while(idx > len(li)-1):
        idx = idx - len(li)
        if(len(li)==0):
            break

print("<", end='')
for i in res:
    if(i == res[-1]):
        print(i,end='')
    else:
        print(i,end=', ')
print(">")
