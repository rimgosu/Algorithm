"""
next, prev, op_start, op_end
만약
"""
def time_to_second(time):
    miniute, second = time.split(':')
    return int(miniute) * 60 + int(second)
def second_to_time(sec):
    second = sec % 60
    miniute = sec // 60
    second = str(second) if len(str(second)) == 2 else '0' + str(second)
    miniute = str(miniute) if len(str(miniute)) == 2 else '0' + str(miniute)
    return miniute + ':' + second

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len, pos, op_start, op_end = time_to_second(video_len), time_to_second(pos), time_to_second(op_start), time_to_second(op_end)
    
    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        
        if command == 'next':
            pos += 10
        else:
            pos -= 10
        
        if pos < 0:
            pos = 0
        elif pos > video_len:
            pos = video_len
    
    if op_start <= pos <= op_end:
        pos = op_end
        
    return second_to_time(pos)