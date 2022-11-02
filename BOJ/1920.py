#1920 수 찾기

n = int(input())
tmp = input()
l = tmp.split(' ',n)
n_num = list(map(int,l))
n_num.sort()
n_len = len(n_num)

m = int(input())
tmp = input()
l = tmp.split(' ',m)
m_num = list(map(int,l))

for num in m_num:
    low = 0
    high = n_len-1
    flag = 1
    while(low<=high):
        mid = (low + high) // 2
        if (num == n_num[mid]):
            print(1)
            flag = 0
            break
        elif (num > n_num[mid]):
            low = mid + 1
        elif (num < n_num[mid]):
            high = mid - 1
    if(flag == 1):
        print(0)
