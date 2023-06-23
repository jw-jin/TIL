import sys
input = sys.stdin.readline
N = int(input())

st = []
for i in range(N):
    command = input().split()
    if(command[0][0] == 'p'):
        if(command[0][1] == 'u'):
            st.append(command[1])
        elif(command[0][1] == 'o'):
            if(len(st)):
                print(st.pop())
            else:
                print(-1)
    elif(command[0][0] == 's'):
        print(len(st))
    elif(command[0][0] == 'e'):
        if(len(st)):
            print(0)
        else:
            print(1)
    elif(command[0][0] == 't'):
        if(len(st)):
            print(st[len(st)-1])
        else:
            print(-1)

    