from math import factorial
N = int(input())

nfact = factorial(N)
nfli = list(str(nfact))
cnt = 0
for _ in range(len(nfli)):
    if nfli[-1] == '0': 
        cnt+=1
        nfli.pop()
    else:
        break

print(cnt)
