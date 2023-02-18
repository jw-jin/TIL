N,r,c = map(int,input().split())

def zcnt(num):
    global board,move,cnt,move_range

    if num == 1:
        for m in move_range:
            xst = m[0][0]
            xed = m[0][1]
            yst = m[1][0]
            yed = m[1][1]
            for i in range(yst,yed):
                    for j in range(xst,xed):
                        if(board[i][j] == -1):
                            for m in move:
                                board[i+m[0]][j+m[1]] = cnt
                                cnt+=1
    else: 
        zcnt(num-1)            



board = [[-1] * (2 ** N) for _ in range(2 ** N)]
move = [[0,0],[0,1],[1,0],[1,1]]
x= int(2**(N-1))
x2 = int((2**(N-1)*2)-1)
move_range = [[[0,x-1],[0,x-1]],[[x,x2],[0,x-1]],[[0,x-1],[x,x2]],[[x,x2],[x,x2]]]

#move_range = [[0,2**(N-1)-1],[2**(N-1),(2**(N-1)*2)-1]]

print((2**15)**2)
cnt = 0 
st= 0
ed= st+ 2**(N-1) 
zcnt(N)
for i in board:
    print(i)

# st= ((2**(N))//2) 4사분면
# ed= st+ 2**(N-1) 
# print(st,ed)
# for i in range(st,ed):
#     for j in range(st,ed):
#         if(board[i][j] == 0):
#             for m in move:
#                 board[i+m[0]][j+m[1]] = cnt
#                 cnt+=1

# for i in board:
#     print(i)


"""
00 01
10 11
# st= 0 1사분면
# ed= st+ 2**(N-1) 
# st= ((2**(N))//2) 4사분면
# ed= st+ 2**(N-1) 
# st= ((2**(N))//2) 4사분면
# ed= st+ 2**(N-1) 
# st= ((2**(N))//2) 4사분면
# ed= st+ 2**(N-1) 


"""