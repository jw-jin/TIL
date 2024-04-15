from itertools import combinations
def solution(friends, gifts):
    scores = {}
    gift_log = {}
    result = {}
    for f in friends:
        scores[f] = 0
        gift_log[f] = {}
        result[f] = 0
        
    for g in gifts:
        a, b = g.split(' ')
        scores[a] +=1
        scores[b] -=1
        if b in gift_log[a]:
            gift_log[a][b] +=1
                
        else:
            gift_log[a][b] = 1
            
    # print(gift_log)
    for i in combinations(friends, 2):
        a = i[0]
        b = i[1]
        # a가 b한테 안준경우
        # b가 a한테 안준경우
        # a-x b b -x a
        if b not in gift_log[a]:
            if a in gift_log[b]:
                result[b] +=1
            else:
                if scores[a] > scores[b]:
                    result[a] +=1
                elif scores[a] < scores[b]:
                    result[b] +=1
        elif a not in gift_log[b]:
            if b in gift_log[a]:
                result[a]+=1
            else:    
                if scores[a] > scores[b]:
                    result[a] +=1
                elif scores[a] < scores[b]:
                    result[b] +=1
        else:
            if gift_log[a][b] > gift_log[b][a]:
                result[a] +=1
            elif gift_log[a][b] < gift_log[b][a]:
                result[b] +=1
            else:    
                if scores[a] > scores[b]:
                    result[a] +=1
                elif scores[a] < scores[b]:
                    result[b] +=1
    
    return max(result.values())

