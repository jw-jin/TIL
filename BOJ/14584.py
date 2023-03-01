crypt = list(input())
N = int(input())

kdict = []
for _ in range(N):
    kdict.append(input())
# 97 ~ 122 - 26
flag= 0 
for i in range(1,27):
    if(flag==1):
        break
    for j in range(len(crypt)):
        x = ord(crypt[j]) + 1
        if(x > 122):
            x=x-26
        crypt[j] = chr(x)
    crypt_str = ''
    for d in crypt:
        crypt_str += d
    for dan in kdict:
        val = crypt_str.find(dan)
        if(val != -1):
            flag = 1
            break

print(crypt_str)
