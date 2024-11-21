num = int(input())
dices = []
for _ in range(num):
    dices.append(list(map(int, input().split())))
dices = dices[::-1]

dice_dict = {
    0: ([1,2,3,4],5),
    1: ([0,2,4,5],3),
    2: ([0,1,3,5],4), 
    3: ([0,2,4,5],1), 
    4: ([0,1,3,5],2), 
    5: ([1,2,3,4],0)
}

first_dice = dices.pop()
answers = []
idx = 0
for bottom_idx, (side_idxs, top_idx) in dice_dict.items():
    answer = 0
    bottom, sides, top = first_dice[bottom_idx], [first_dice[side_idx] for side_idx in side_idxs], first_dice[top_idx]
    answer += max(sides)
    dices_copy = dices.copy()
    while dices_copy:
        dice = dices_copy.pop()
        _bottom_idx = dice.index(top)
        _side_idxs, _top_idx = dice_dict[_bottom_idx]

        bottom, sides, top = dice[_bottom_idx], [dice[_side_idx] for _side_idx in _side_idxs], dice[_top_idx]

        answer += max(sides)
    answers.append(answer)

print(max(answers))