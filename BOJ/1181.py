icnt = int(input())
words = []
for i in range(cnt):
    word = input()
    words.append(word)

words = list(set(words))
words.sort()
sort_words = sorted(words, key=len)

for i in sort_words:
    print(i)
