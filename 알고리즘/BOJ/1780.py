import sys
input = sys.stdin.readline


def chk(x,y,lth):
    global arr, res
    chk_num = [-1, 0, 1]
    chk_flag = [0, 0, 0]
    for n in range(3):
        for i in range(y,y+lth):
            if(chk_flag[n] == 1):
                break
            for j in range(x,x+lth):
                if arr[i][j] != chk_num[n]:
                    chk_flag[n] = 1
                    break
    
    if(sum(chk_flag) == 2): # 수하나로 채워졌을때
        res[chk_flag.index(0)] += 1
        return
    
    if(lth == 1):
        return
    lth = lth // 3
    chk(x,y,lth) # 1
    chk(x+lth,y,lth) # 2
    chk(x+(lth*2),y,lth) # 3
    chk(x,y+lth,lth) # 4
    chk(x+lth,y+lth,lth) # 5
    chk(x+(lth*2),y+lth,lth) # 6
    chk(x,y+(lth*2),lth) # 7
    chk(x+lth,y+(lth*2),lth) # 8
    chk(x+(lth*2),y+(lth*2),lth) # 9

     

            
            



N = int(input())

arr = []
res = [0,0,0]
for _ in range(N):
    arr.append(list(map(int,input().split())))

chk(0,0,N)
for i in res:
    print(i)
#print cnt -1 0 1