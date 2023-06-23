#BOJ 2164 큐사용문제
from collections import deque

N = int(input())

deck = deque(range(1,N+1))

while(len(deck) > 1):
    deck.popleft()
    x = deck.popleft()
    deck.append(x)

print(deck[0])