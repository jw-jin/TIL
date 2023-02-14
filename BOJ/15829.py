import math
L = int(input())
input_str = input()
M = 1234567891
res = 0
for i in range(len(input_str)):
    #시그마 0 ~l-1 문자 mod M
    r = 1
    a = ord(input_str[i]) - 96
    for j in range(i):
        r=r*31

    res += (a*r)

print(res%M)

