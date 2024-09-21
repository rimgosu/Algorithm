def time2minute(time):
    hour, minute = time.split(':')
    hour, minute = int(hour), int(minute)
    return hour * 60 + minute

def solution(book_time):
    answer = 0
    width, height = len(book_time[0]), len(book_time)
    for x in range(width):
        for y in range(height):
            book_time[y][x] = time2minute(book_time[y][x])
    book_time.sort(key=lambda x: x[0])
    
    stack = []
    for start, end in book_time:
        stack.append(end+10)
        stack.sort(reverse=True)
        while stack and stack[-1] <= start:
            stack.pop()
        if answer < len(stack):
            answer = len(stack)
        # print(f'stack:{stack},start:{start},end:{end}')
        
    return answer