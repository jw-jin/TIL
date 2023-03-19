# boj 2630 색종이 만들기

# 2 =< N <= 128
# 흰 0 파 1
def chk(x,y,n):
    global arr
    color = arr[y][x]
    for i in range(y,y+n):
        for j in range(x,x+n):
            if arr[i][j] != color:
                return -1
    
    return color

def solution(x,y,n):
    global arr,cnt
    res = chk(x,y,n)
    if res == -1:
        n2 = n//2
        solution(x,y,n2)
        solution(x+n2,y,n2)
        solution(x,y+n2,n2)
        solution(x+n2,y+n2,n2)
    else:
        cnt[res] +=1
        return


N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

cnt = [0,0]
solution(0,0,N)
for r in cnt:
    print(r)


