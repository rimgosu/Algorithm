
def solution(friends, gifts):
    answer = 0
    """
    {'muzi' : {'ryan' : -3, 'frodo' : 1, 'neo' : -1}, 
    'ryan' : {'muzi' : 3, 'frodo' : -1, 'neo' : 0},}
    선물을 주면 +1
    선물을 받으면 -1
    """
    
    gift_jisu = {}
    gift_status = {}
    gift_next = {}
    
    for friend in friends:
        gift_jisu[friend] = 0
        gift_next[friend] = 0
        gift_status[friend] = {}
        
        for friend2 in friends:
            if friend2 != friend : 
                gift_status[friend][friend2] = 0
        
    
    
    for gift in gifts:
        fr, to = gift.split()
        gift_jisu[fr] += 1
        gift_jisu[to] -= 1
        
        gift_status[fr][to] += 1
        gift_status[to][fr] -= 1
        
    for key, value in gift_status.items():
        for key2, value2 in value.items():
            if value2 > 0 :
                gift_next[key] += 1
            elif value2 == 0:
                if gift_jisu[key] > gift_jisu[key2]:
                    gift_next[key] +=1
    
    return max(gift_next.values())