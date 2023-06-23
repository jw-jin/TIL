while True:
    st = []
    input_str = input()
    if(input_str == "."):
        break
    flag = 0
    for i in input_str:
        if(i == '(' or i == '['):
            st.append(i)
        elif(i == ')'):
            if(len(st) == 0):
                flag = 1
                break
            if(st.pop() != '('):
                flag = 1
                break
        elif(i == ']'):
            if(len(st) == 0):
                flag = 1
                break
            if(st.pop() != '['):
                flag = 1
                break
    if(len(st)>0):
        flag=1
    
    if(flag == 0):
        print("yes")
    else:
        print("no")
        
