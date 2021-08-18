matrix =[[i for i in input().split(" ")] for j in range(8)]
queens = []
n = 8

def is_next_move_valid(row, collumn):
    if 0 <= row < n and 0 <= collumn < n:
        return True
    return False 

directions = {
    "up":(-1, 0),
    "down":(1,0),
    "right":(0, 1),
    "left":(0, -1),
    "up_right":(-1, 1),
    "up-left":(-1, -1),
    "down_right":(1, 1),
    "down_left":(1, -1)
}

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] == "K":
            king_pos = (x, y)

for direction in directions:
    row = king_pos[0]
    collumn = king_pos[1]
    next_row = row + directions[direction][0]
    next_collumn = collumn + directions[direction][1]
    while is_next_move_valid(next_row, next_collumn):
        if matrix[next_row][next_collumn] == "Q":
            queens.append([next_row, next_collumn])
            break
        next_row += directions[direction][0]
        next_collumn += directions[direction][1]

if queens:
    for el in queens:
        print(el)
else:
    print("The king is safe!")
