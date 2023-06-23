#10814 나이순 정렬
N = int(input())

member = []

# i가 낮을수록 먼저가입함
for i in range(N):
    age, name = input().split()
    member.append([age,name])

res = sorted(member, key=lambda x: int(x[0]))

for age, name in res:
    print(age, name)