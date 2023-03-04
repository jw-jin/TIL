# boj 5430 AC
# R 배열 뒤집기 , D 첫번째수 버리기
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    cmd = list(input())
    n = int(input())
    
    q = deque(input().strip()[1:-1].split(","))
    if n==0:
        q = []
    err_flag = 0
    idx = 0
    reverse_flag = 0
    while idx<len(cmd):
        if(cmd[idx] == 'R'):
            r_cnt = 1
            tmp_idx = 0
            for j in range(idx+1,len(cmd)):
                if(cmd[j] == 'R'):
                    r_cnt +=1
                else:
                    tmp_idx = j - (idx)
                    break
            if(r_cnt%2 == 1):
                reverse_flag += 1
            idx += tmp_idx
            continue
        elif(cmd[idx] == 'D'):
            if(len(q) > 0):
                if(reverse_flag%2 == 0):
                    val = q.popleft()
                else:
                    val = q.pop()
                if(val == ''):
                    err_flag = 1
                    break
            else:
                err_flag = 1
                break
        idx+=1

    if(err_flag == 1):
        print("error")
    else:
        if(reverse_flag %2 ==  1):
            q = deque(reversed(q))
        res = '[' + ','.join(q) + ']'
        print(res)