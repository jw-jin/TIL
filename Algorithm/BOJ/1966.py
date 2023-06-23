#BOJ 1966 프린터 큐
#FIFO 중요도 숫자 1234

case_num = int(input())
num=0
while(num<case_num):
    N,M = map(int, input().split())
    imp = list(map(int,input().split()))
    imp_idx = list(range(0,N))
    cnt = 0
    while(len(imp)):
        max_imp = imp[0]
        sorted_imp = sorted(imp)
        if(max_imp<sorted_imp[-1]):
            tmp = imp.pop(0)
            tmp_idx = imp_idx.pop(0)
            imp.append(tmp)
            imp_idx.append(tmp_idx)
        else:
            imp.pop(0)
            cnt+=1
            if(imp_idx[0] == M):
                print(cnt)
                break
            imp_idx.pop(0)
    num+=1





