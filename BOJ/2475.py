num = list(map(int,input().split()))
p_sum = 0
for i in num:
    p_sum += i*i
print(p_sum%10)