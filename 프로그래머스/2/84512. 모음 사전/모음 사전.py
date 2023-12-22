def solution(words):
    answer = 0
    word_list = []
    word = 'AEIOU'
    
    def dfs(c, w):
        if c == 5:
            return
        for i in range(len(word)):
            word_list.append(w+word[i])
            dfs(c+1, w+word[i])
            
            
    dfs(0,'')
            
    
    return word_list.index(words)+1