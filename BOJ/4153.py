#4153 직각삼각형

def calc(li):
    a = pow(li[0],2)
    b = pow(li[1],2)
    c = pow(li[2],2)
    if(a+b == c):
        return "right"
    else:
        return "wrong"

while(True):
    input_list = input()
    if(input_list == '0 0 0'):
        break
    li = input_list.split(' ')
    li = list(map(int, li))
    li.sort()

    print(calc(li))
