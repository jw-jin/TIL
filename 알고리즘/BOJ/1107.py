"""
0 ~9 + -
"""
# N 타겟 채널 m 고장난 버튼 개수 시작 채널은 100
def check(num):
    global btn_list
    if(num<0):
        return False
    str_num = str(num)
    for i in str_num:
        if(int(i) not in btn_list):
            return False
    return True

N = input()
M = int(input())


btn_list = [0,1,2,3,4,5,6,7,8,9]
if M:
    broken = list(map(int,input().split()))
    for i in broken:
        for j in btn_list:
            if(i==j):
                btn_list.remove(i)

cur_ch = 100
target_ch = int(N)
push_cnt = 0
plusch = target_ch
minusch = target_ch
res_ch = 100

while True:
    if(cur_ch == target_ch):
        break
    else:
        for i in range(500000):
            if(check(minusch)):
                res_ch = minusch
                break
            if(check(plusch)):
                res_ch = plusch
                break
            plusch+=1
            if(minusch-1 >= 0):
                minusch-=1
        push_cnt += len(str(res_ch)) # 숫자버튼
        cur_ch = res_ch
        ch_diff = abs(target_ch - cur_ch)
        if(target_ch> cur_ch):
            cur_ch += ch_diff
        else:
            cur_ch -= ch_diff
        push_cnt += ch_diff # +- 버튼

ch_diff = abs(target_ch - 100)
if(push_cnt> ch_diff):
    print(ch_diff)
else:
    print(push_cnt)
        
        




 # 가장 가까운 숫자 버튼으로 가기
 # 1111111
 # 98
 # 