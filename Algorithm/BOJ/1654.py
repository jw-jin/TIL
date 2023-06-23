k,n = map(int,input().split())
line_len = []
sum = 0
for i in range(0,k):
    tmp = int(input())
    line_len.append(tmp)

max = max(line_len)
min = 1
while(min<=max):
    lan_sum = 0
    mid = (max + min) // 2
    for i in line_len:
        lan_sum += i // mid
    if(lan_sum>=n):
        min = mid + 1
    elif(lan_sum<n):
        max = mid - 1

print(max)
    

    