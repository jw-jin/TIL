def solution(bandage, health, attacks):
    # bandage [시전시간, 초당 회복량, 추가회복량]
    # t초동안 성공하면 y만큼 추가회복
    cast_time = bandage[0]
    heal_per_sec = bandage[1]
    extra_heal = bandage[2]
    cur_health = health
    succ_time = 0 
    last_time = attacks[-1][0] + 1
    for i in range(last_time):
        att_flag = 0
        for t, dmg in attacks:
            if i == t:
                cur_health -= dmg
                succ_time=0
                att_flag=1
                if cur_health <= 0 :
                    return -1
            elif i<t:
                break
                
        if att_flag == 0:
            succ_time +=1
            cur_health += heal_per_sec
            if succ_time == cast_time:
                cur_health += extra_heal
                succ_time = 0 
                
        if cur_health >= health:
            cur_health = health

    return cur_health