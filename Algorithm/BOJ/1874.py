# 시간초과 실패
import sys 
input = sys.stdin.readline
import bisect
def binarySearch(list,n):
    if(len(list) == 0):
        return -1
    low = 0
    high = len(list)-1
    while(low<=high):
        mid = (low + high) // 2
        if(list[mid] == n):
            return mid
        elif(list[mid] > n):
            high = mid -1
        else:
            low = mid + 1
    
    return -1

n = int(input())


want_num = []
for i in range(n):
    tmp = int(input())
    want_num.append(tmp)

st = []
res = []
output = []
num_list = list(range(1,n+1))
idx = 0
fail = 0
while(len(res) < n and n != 1):
    if (fail == 1):
        break
    for i in num_list:
        if(idx==n):
            idx=0
        chk = binarySearch(st,want_num[idx])
        if(chk == -1):
            st.append(i)
            output.append("+")
            num_list.remove(i)
            if(len(num_list) == 0):
                fail = 1
            break
            
        elif(chk >=0):
            num = st.pop()
            num_list.append(num)
            res.append(num)
            output.append("-")
            idx+=1
            if(len(num_list) == 0):
                fail = 1
            break


if(n == 1):
    print("+")
    print("-")
elif(fail == 0):
    for i in output:
        print(i)
else:
    print("NO")
