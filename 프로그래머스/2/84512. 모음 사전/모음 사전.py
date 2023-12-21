def solution(word):
    answer = 0
    word_list = []
    words = 'AEIOU'
    
    def dfs(cnt, w):
        if cnt == 5:
            return 
        for i in range(len(words)):
            word_list.append(w + words[i])
            dfs(cnt+1, w + words[i])
            
    dfs(0,"")
    
    return word_list.index(word)+1