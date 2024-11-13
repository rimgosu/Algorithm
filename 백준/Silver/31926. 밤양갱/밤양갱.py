inp = int(input())

"""
daldidalgo 10

daldidalgo
daldidalgo 11

daldidalgo
daldidalgo
daldidalgo
daldidalgo 12

daldidalgo 8
daldidalgo 9
daldidalgo
daldidalgo 10
daldidalgo
daldidalgo
daldidalgo
daldidalgo 11 + daldidan + 2 13

daldidalgo
daldidalgo
daldidalgo
daldidalgo
daldidalgo
daldidalgo
daldidalgo
daldidalgo
"""

now_number, dal_count = 10, 1
dal_dict = {dal_count: now_number}
while inp > dal_count:
    dal_count *= 2
    now_number +=1
    dal_dict[dal_count] = now_number

for key, value in dal_dict.items():
    if key > inp:
        print(value-1)
    elif key == inp:
        print(value)
        