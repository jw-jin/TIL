x,y,w,h = map(int, input().split())
res = min(x,y,w-x,h-y)
print(res)
