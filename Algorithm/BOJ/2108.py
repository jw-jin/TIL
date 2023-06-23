import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline



N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

sum = 0
for i in nums:
    sum += i
print(round(sum/N))

nums.sort()
print(nums[len(nums)//2])

lst = {}
max_cnt = 0
for i in nums:
    idx = bisect_left(nums,i)
    cnt = bisect_right(nums,i) - bisect_left(nums,i)
    if(max_cnt<cnt):
        max_cnt = cnt
    lst[nums[idx]] = [idx,cnt]

max_list = []
for i in lst.items():
    if(i[1][1] == max_cnt):
        max_list.append(i[0])
res_list = sorted(set(max_list))

if(len(res_list) == 1):
    print(res_list[0])
else:
    print(res_list[1])



print(max(nums)-min(nums))
