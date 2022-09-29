# 시간초과 실패
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
while(len(res) < n):
    if (fail == 1):
        break
    for i in num_list:
        if(idx==n):
            idx=0
        if(want_num[idx] not in st):
            st.append(i)
            output.append("+")
            num_list.remove(i)
            if(len(num_list) == 0):
                fail = 1
            break
            
        elif(want_num[idx] in st):
            num = st.pop()
            num_list.append(num)
            res.append(num)
            output.append("-")
            idx+=1
            if(len(num_list) == 0):
                fail = 1
            break


if(fail == 0):
    print(output)
else:
    print("NO")
