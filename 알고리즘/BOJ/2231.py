def cons(N):
    N_len = len(str(N))
    N_input=N
    N_list = []
    i = N_len
    while(N>1):
        tmp = N//(10**(i-1))
        N_list.append(tmp)
        N = N % (10**(i-1))
        i-=1
    res = N_input+sum(N_list)
    return res


N = int(input())
c_list = []
for i in range(N):
    con = cons(i)
    if(con == N):
        c_list.append(i)
if(c_list):
    print(min(c_list))
else:
    print(0)


