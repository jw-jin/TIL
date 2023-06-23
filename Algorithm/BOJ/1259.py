def check(n):
    n_len = len(n)
    if(n_len == 1):
        return 'yes'
    elif(n_len == 2):
        if(n[0] == n[1]):
            return 'yes'
        else:
            return 'no'
    else:
        for i in range(int(n_len/2)):
            if(n[i] != n[n_len-i-1]):
                return 'no'
        return 'yes'       

        
        
while(1):
    num = input()
    if (num == '0'):
        break
    res = check(num)
    print(res)
    