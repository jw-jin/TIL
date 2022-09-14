words = input()
cnt = 0
wd_len = len(words)
if(words[0] != ' '):
    cnt+=1
for i,word in enumerate(words):
    if(word == ' '):
        if(i+1<wd_len):
            if(words[i+1] != ' '):
                cnt+=1
        

print(cnt)
