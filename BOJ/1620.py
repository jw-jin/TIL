import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poke_dict = {}
for i in range(N):
    poke_dict[i+1] = input().strip()
reverse_dict = dict(map(reversed,poke_dict.items()))
for i in range(M):
    question = input().strip()
    if(question.isdigit()):
        print(poke_dict[int(question)])
    else:
        print(reverse_dict[question])