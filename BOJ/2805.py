import sys
input = sys.stdin.readline

N,M = map(int,input().split())
height = list(map(int,input().split()))

low = 0
high = max(height)
res = 0
while True:
    if(low>=high):
        break
    
    mid = (low+high) // 2

    cut_lst = []
    for i in height:
        cut_height = i-mid
        if(cut_height<0):
            cut_height = 0
        cut_lst.append(cut_height)

    if(sum(cut_lst) < M):
        high = mid
    elif(sum(cut_lst)> M):
        low = mid+1
        res = mid
    elif(sum(cut_lst) == M):
        res = mid
        break
        
print(res)






    


