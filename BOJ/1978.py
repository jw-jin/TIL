def isprime(n):
    if(n==1):
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

N = int(input())
num_list = list(map(int,input().split()))
cnt = 0
for i in num_list:
    if(isprime(i)):
        cnt+=1

print(cnt)
