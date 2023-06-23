from itertools import permutations

N, M = map(int, input().split())
deck = list(map(int, input().split()))
res = 0
for deck_list in permutations(deck,3):
    tmp = sum(deck_list)
    if(res<tmp and tmp<=M):
        res = tmp
print(res)