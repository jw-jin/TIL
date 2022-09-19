n = int(input())
cnt = 0
num = 0
while(cnt<n):
    num+=1
    str_num = str(num)
    res = str_num.find("666")
    if(res != -1):
        cnt+=1

print(num)
        
