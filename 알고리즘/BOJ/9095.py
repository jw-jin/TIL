T = int(input())
import copy
for _ in range(T):
    n = int(input())
    for tn in range(2,n+1):
        if(tn<=2):
            num = [[1,1]]
        else:
            num_len = len(num)
            for i in range(len(num)):
                tmp = copy.deepcopy(num[i])
                tmp.append(1)
                num.append(tmp)
                for j in range(len(num[i])):
                    tmp = copy.deepcopy(num[i])
                    tmp[j] +=1
                    if(sum(tmp) == tn and tmp[j] <= 3):
                        num.append(tmp)
            num = num[num_len:] 
            num = list(set(map(tuple, num)))
            for k in range(len(num)):
                num[k] = list(num[k])

        
    if(n>3):
        print(len(num))
    else:
        if(n==1):
            print(1)
        elif(n==2):
            print(2)
        elif(n==3):
            print(4)
        

            
    

    """
    1 = 1 0
    2 = 1+1 1
        2
    3 = 1+1+1 3
        1+2 2+1
        3
    4 = 1+1+1+1
        1+1+2
        1+2+1
        2+1+1
        2+2
        1+3
        3+1
    5 = 1+1+1+1+1
        1+1+2+1
        1+2+1+1
        2+1+1+1

        2+2+1
        1+3+1
        3+1+1
        1+2+2
        2+1+2

        2+3
        1+4
        3+2
        4+1

    
    """