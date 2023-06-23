from bisect import bisect_left, bisect_right

def count(n,list):
    minidx = bisect_left(list,n)
    maxidx = bisect_right(list,n)

    return maxidx - minidx

    
N = int(input())
card_list = list(map(int,input().split()))
M = int(input())
num_list = list(map(int,input().split()))

card_list.sort()

for i in num_list:
    cnt = count(i,card_list)
    if(i == num_list[-1]):
        print(cnt, end='')
    else:
        print(cnt, end=' ')



