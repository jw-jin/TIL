#BOJ 1018 체스판 다시 칠하기 20220519
W =  [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
      ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

B = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
     ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
     ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
     ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
     ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

def check(board):
    cnt = 0
    cnt2 = 0
    for i in range(8):
        for j in range(8):
            if(board[i][j] != W[i][j]):
                cnt+=1
            if(board[i][j] != B[i][j]):
                cnt2+=1
    
    
    return min(cnt,cnt2)

def bd_split(board,x,y):
    new_bd = [[0 for i in range(8)] for i in range(8)]
    for i in range(8):
        new_bd[i] = board[y+i][x:x+8]
    return new_bd

N, M = map(int,input().split())
board = []
for i in range(N):
    board.append(input())
    board[i] = list(board[i])

res = 64
for i in range(N):
    for j in range(M):
        if(N-i > 7 and M-j > 7):
            new_bd = bd_split(board,j,i)
            tmp = check(new_bd)
            if(tmp<res):
                res = tmp
    
print(res)



