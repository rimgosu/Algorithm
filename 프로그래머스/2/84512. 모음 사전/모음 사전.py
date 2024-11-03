def solution(words):
    answer = 0
            
    # a -> aa -> aaa -> aaaa -> aaaaa -> aaaae -> aaaai -> aaaao -> aaaau -> aaae
    # a,e,i,o,u 넣고, 길이가 5랑 같아지면 종료하는 형태
    result = []
    def dfs(word):
        if word:
            result.append(word)
        if len(word) == 5:
            return
        
        for vowel in 'AEIOU':
            dfs(word+vowel)
    
    dfs('')
    
    return result.index(words) + 1