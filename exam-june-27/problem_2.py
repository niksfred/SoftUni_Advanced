matrix = [[el for el in input().split()] for row in range(5)]
n = int(input())

current_pos = [0, 0]
targets = []    

for row in range(5):
    for col in range(5):
        if matrix[row][col] == "A":
            current_pos = row, col
            matrix[row][col] = "."
        elif matrix[row][col] == "x":
            targets.append([row, col])

count_targets = 0
targets_hit = []
row, col = current_pos

for com in range(n):
    command = input().split()
    action = command[0]
    direction = command[1]
    if action == "move":
        steps = int(command[2])
        if direction == "up":
            row -= steps
        elif direction == "down":
            row += steps
        elif direction == "right":
            col += steps
        elif direction == "left":
            col -= steps
        if row < 0 or col < 0 or row >= 5 or col >= 5 or matrix[row][col] != ".":
            row, col = current_pos
            continue
        else:
            current_pos = [row, col]
    if action == "shoot":
        if direction == "up":
            for r in range(row-1, -1, -1):
                if [r, col] in targets:
                    targets.remove([r, col])
                    matrix[r][col] = "."
                    count_targets += 1
                    targets_hit.append([r, col])
                    break
        elif direction == "down":
            for r in range(row, 5):
                if [r, col] in targets:
                    targets.remove([r, col])
                    matrix[r][col] = "."
                    count_targets += 1
                    targets_hit.append([r, col])
                    break
        elif direction == "right":
            for c in range(col, 5):
                if [row, c] in targets:
                    targets.remove([row, c])
                    matrix[row][c] = "."
                    count_targets += 1
                    targets_hit.append([row, c])
                    break
        elif direction == "left":
            for c in range(col-1, -1, -1):
                if [row, c] in targets:
                    targets.remove([row, c])
                    matrix[row][c] = "."
                    count_targets += 1
                    targets_hit.append([row, c])
                    break
    if not targets:
        break

row, col = current_pos
matrix[row][col] = "A"

if not targets:
    print(f"Training completed! All {count_targets} targets hit.")
else:
    print(f"Training not completed! {len(targets)} targets left.")
[print(target) for target in targets_hit]