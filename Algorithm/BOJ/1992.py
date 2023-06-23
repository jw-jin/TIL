"""
0(0011)(0(0111)01)1)
"""

def chk(x,y,n):
    global res,arr
    zflag = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if(arr[j][i] == 1):
                zflag = 1
                break
    if(zflag == 0):
        res.append(0)
        return 0
    
    
    oflag = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if(arr[j][i] == 0):
                oflag = 1
                break
    if(oflag == 0):
        res.append(1)
        return 0
    #if ()
    res.append('(')
    n = n//2
    chk(x, y, n) # 1사분면
    chk(x+n, y, n) # 2사분면
    chk(x, y+n, n) # 3사분면
    chk(x+n, y+n, n) # 4사분면 
    # chk(x1, x2//2, y1, y2//2) # 1사분면
    # chk(x2//2,x2, y1, y2//2) # 2사분면
    # chk(x1, x2//2, y2//2,y2) # 3사분면
    # chk(x2//2, x2, y2//2,y2) # 4사분면 
    res.append(')')

N = int(input())

res = []
arr = []
for _ in range(N):
    arr.append(list(map(int,input())))

chk(0,0,N)
str_res = ''
for i in res:
    str_res += str(i)
print(str_res)
