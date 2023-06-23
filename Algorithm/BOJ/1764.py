N, M = input().split()
N = int(N); M = int(M)

nhns_dict = {}
nhns = []
for _ in range(N+M):
    name = input()
    if name not in nhns_dict:
        nhns_dict[name] = 1
    else:
        nhns_dict[name] +=1


for k,v in nhns_dict.items():
    if(v >= 2):
        nhns.append(k)
    

print(len(nhns))
nhns.sort()
for i in nhns:
    print(i)
