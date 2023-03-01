from bisect import bisect_left, bisect_right

arr = [9, 13 ,30 ,40, 50]

res = bisect_left(arr, 1)
print(res)
print(arr[res])