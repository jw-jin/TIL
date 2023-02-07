#BOJ 9012 괄호

T = int(input())

for i in range(T):
    data = input()
    li = list(data)
    if(li[0] == ')'):
        print("NO")
        continue
    elif(len(li)%2 == 1):
        print("NO")
        continue
    flag = 0
    idx = 0
    while(len(li)>idx):
        if(len(li)<=idx+1):
            break;
        if(li[idx] == '(' and li[idx+1] == ')'):
            del li[idx:idx+2]
            idx=0
        else:
            idx+=1
    
    while(len(li) > 0):
        if(li[0] == '(' and li[1] == ')'):
            del li[0:2]
        elif(li[0] == '(' and li[-1] == ')'):
            del li[0]
            del li[-1]
        else:
            flag = 1
            break
    if(flag==1):
        print("NO")
    elif(flag==0):
        print("YES")
    
    
    