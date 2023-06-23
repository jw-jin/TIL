#2751 수정렬하기 2 pypy3으로 제출해서 해결
N = int(input())
res = []
for i in range(N):
    num = int(input())
    res.append(num)

for i in sorted(res):
    print(i)