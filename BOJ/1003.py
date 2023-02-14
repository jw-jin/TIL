#boj 1003 피보나치 함수
import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    graph = [[1,0],[0,1],[1,1]]
    for i in range(N+1):
        if i> 2:
            cnt_0 = graph[i-1][0] + graph[i-2][0]
            cnt_1 = graph[i-1][1] + graph[i-2][1]
            graph.append([cnt_0,cnt_1])

    if(N>2):
        print(graph[-1][0],graph[-1][1])
    else:
        print(graph[N][0],graph[N][1])
        
                
    