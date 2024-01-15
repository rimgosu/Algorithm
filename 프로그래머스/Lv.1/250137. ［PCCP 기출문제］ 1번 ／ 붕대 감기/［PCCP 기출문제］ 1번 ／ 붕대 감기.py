def solution(bandage, health, attacks):
    answer = 0
    
    # 붕대감기
    # 1. 1초마다 x만큼 체력 회복
    # 2. t초 연속 붕대 감는데 성곡하면 y만큼 추가 체력회복
    
    # 체력이 0이 되면 죽음
    # 죽으면 -1 return
    
    # bandage : 기술의 시전시간, 1초당 회복량, 추가회복량
    # health : 최대체력
    # attacks : 공격시간, 피해량
    # 남은 체력 return
    
    last_time = attacks[-1][0]
    current_health = health
    bonus_stack = 0
    attack_time = []
    for attack in attacks:
        attack_time.append(attack[0])
    
    for t in range(last_time+1):
        
        # print("t=", t, "current_health=", current_health, "attacks=", attacks)
        
        # 1. 공격 당할 때
        if t in attack_time:
            damaged = attacks[0][1]
            current_health -= damaged
            attacks.pop(0)
            bonus_stack=0
            
            if current_health <= 0:
                return -1
       
        # 2. 별일 없어서 체력 회복
        else:
            if current_health == health:
                pass
            else:
                current_health += bandage[1]
                bonus_stack +=1
                if current_health > health:
                    current_health = health

                # 3. 연속 체력회복
                if bonus_stack == bandage[0]:
                    current_health += bandage[2]
                    bonus_stack=0
                    if current_health > health:
                        current_health = health
        
         
        
    
    
    
    
    return current_health