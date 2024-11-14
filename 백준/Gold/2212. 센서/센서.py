sensor_count, station_count = int(input()), int(input())
sensor = list(map(int, input().split()))
sensor= list(set(sensor))
sensor.sort()
# [3, 6, 7, 8, 10, 12, 14, 15, 18, 20]
#   3   1  1  2  2   2    1   3   2
# 3인거 먼저 짝대기
# 2인거 그다음 짝대기
# 3 / 6,7,8 / 10 / 12, 14, 15 / 18,20
#     2                3       2

if len(sensor) <= station_count:
    print(0)
    exit()

index = 0
diff_list = []
while index < len(sensor) -1:
    distance_diff = sensor[index+1] - sensor[index]
    diff_list.append(distance_diff)  
    index += 1

install_location_list = []
while station_count != 1:
    max_length = max(diff_list)
    install_location = diff_list.index(max_length)
    diff_list[install_location] = -1
    station_count -= 1
    install_location_list.append(install_location)

install_location_list.sort()
install_location_list = install_location_list[::-1]

answer_list = []
for install_location in install_location_list:
    bundle = []
    while True:
        bundle.append(sensor.pop())
        if len(sensor) == install_location + 1:
            break
    answer_list.append(bundle)

score = 0
for answer in answer_list:
    score += max(answer) - min(answer)

if sensor:
    score += max(sensor) - min(sensor)

print(score)