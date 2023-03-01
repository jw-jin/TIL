import sys
import re
input = sys.stdin.readline

n = input()
num_list = re.findall('\d+', n)
sign = []
for i in n:
    if(i == '+' or i == '-'):
        sign.append(i)

res = int(num_list[0])

i = 0
while i<len(sign):
    if(sign[i] == '-'):
        if(i<len(sign)-1):
            pl_idx = i+1
            minus_val = 0
            while(sign[pl_idx] == '+'):
                if(pl_idx>=len(sign)-1):
                    break
                minus_val += int(num_list[pl_idx])
                pl_idx+=1
            res -= minus_val
            i+=pl_idx
            continue
        res -= int(num_list[i+1])
        i+=1
    else:
        res += int(num_list[i+1])
        i+=1
print(res)
