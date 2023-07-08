

def solution(priorities, location):
    answer = 0
    val_pr = list(zip(list(range(len(priorities))), priorities))
    stack = []
    # print(val_pr)
    _max = max([t[1] for t in val_pr])
    # print(_2ndMax)
    
    """
    1. max값이 val_pr에 있을 때
    2. max 값이 stack에 있을 때
    3. max 값이 val_pr과 stack에 둘 다 있을 때
    """
    breaker = True
    i=0
    while breaker:
        val_pr_1e = [t[1] for t in val_pr]
        stack_1e = [t[1] for t in stack]
        _max = max(val_pr_1e + stack_1e)
        light = True
        
        try:
            if _max == val_pr_1e[-1]:
                val_pr.pop()
                print('_max = val_pr_1e[-1]')
                light= False
            elif _max == stack_1e[-1]:
                stack.pop()
                print('_max = stack_1e[-1]')
                light= False
        except:
            pass
        
        if light:
            if _max in val_pr_1e and _max in stack_1e:
                print('both')
                print('val_pr_1e_index', val_pr_1e.index(_max), 'stack_1e_index', stack_1e.index(_max))
            elif _max in val_pr_1e:
                stack.append(val_pr.pop())

                print('_max in val_pr_1e')
            elif _max in stack_1e:
                print('_max in stack_1e')

        print("stack", stack, "val_pr", val_pr)
        i+=1
        if i == 4:
            breaker = False
    
    return answer

def solution(priorities, location):
    answer = 0
    val_pr = list(zip(list(range(len(priorities))), priorities))
    stack = []
    while True:
        _max = max([t[1] for t in val_pr])
        if _max == val_pr[0][1]:
            stack.append(val_pr.pop(0))
            # print('max = val_pr',val_pr)
        else:
            val_pr.append(val_pr.pop(0))
            # print('appended', val_pr)
        
        if val_pr == []:
            break
    print(stack)
    return [ t[0] for t in stack].index(location)+1