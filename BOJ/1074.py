N,r,c = map(int,input().split())

def recur(n,N,x1,x2,y1,y2):
    global res, r, c
    xmid = (x1+x2) // 2
    ymid = (y1+y2) // 2
    
    if n == 1:
        return 

    
    if (r<ymid and c<xmid):
        nx1 = x1; nx2 = xmid; ny1 = y1; ny2 = ymid;
    elif (r<ymid and c>=xmid):
        res += (4**(N-1))* 1
        nx1 = xmid; nx2 = x2; ny1 = y1; ny2 = ymid;
    elif (r>=ymid and c<xmid):
        res += (4**(N-1))* 2
        nx1 = x1; nx2 = xmid; ny1 = ymid; ny2 = y2;
    elif (r>=ymid and c>=xmid):
        nx1 = xmid; nx2 = x2; ny1 = ymid; ny2 = y2;
        res += (4**(N-1))* 3
    
    N-=1
    recur(n//2,N,nx1,nx2,ny1,ny2)

# 4** (n-2)
# 2 ** N
n = 2**N
res = 0
recur(n,N,0,n,0,n)

print(res)