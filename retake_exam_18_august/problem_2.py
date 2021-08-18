n = int(input())
matrix = []
numbers = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10")
tea_bags = 0
alice_makes_it = False

def is_valid(row, collumn):
    if 0 <= row < n and 0 <= collumn < n:
        return True
    return False

for row in range(n):
    matrix.append(input().split())

for row in range(len(matrix)):
    for collumn in range(len(matrix[row])):
        if matrix[row][collumn] == "A":
            alice_pos = [row, collumn]
            matrix[row][collumn] = "*"
            

while True:
    command = input()
    if command == "down":
        next_row = alice_pos[0] + 1
        next_collumn = alice_pos[1]
        if is_valid(next_row, next_collumn):
            alice_pos = [next_row, next_collumn]

            if matrix[next_row][next_collumn] == ".":
                matrix[next_row][next_collumn] = "*"
            elif matrix[next_row][next_collumn] == "R":
                matrix[next_row][next_collumn] = "*"
                print("Alice didn't make it to the tea party.")
                break

            elif matrix[next_row][next_collumn] in numbers:
                tea_bags += int(matrix[next_row][next_collumn])
                matrix[next_row][next_collumn] = "*"
                if tea_bags >= 10:
                    alice_makes_it = True
                    break
        else:
            print("Alice didn't make it to the tea party.")
            break

    elif command == "up":
        next_row = alice_pos[0] - 1
        next_collumn = alice_pos[1]
        if is_valid(next_row, next_collumn):
            alice_pos = [next_row, next_collumn]

            if matrix[next_row][next_collumn] == ".":
                matrix[next_row][next_collumn] = "*"
            elif matrix[next_row][next_collumn] == "R":
                matrix[next_row][next_collumn] = "*"
                print("Alice didn't make it to the tea party.")
                break
            elif matrix[next_row][next_collumn] in numbers:
                tea_bags += int(matrix[next_row][next_collumn])
                matrix[next_row][next_collumn] = "*"
                if tea_bags >= 10:
                    alice_makes_it = True
                    break
        else:
            print("Alice didn't make it to the tea party.")
            break
    elif command == "right":
        next_row = alice_pos[0]
        next_collumn = alice_pos[1] + 1
        if is_valid(next_row, next_collumn):
            alice_pos = [next_row, next_collumn]

            if matrix[next_row][next_collumn] == ".":
                matrix[next_row][next_collumn] = "*"
            elif matrix[next_row][next_collumn] == "R":
                matrix[next_row][next_collumn] = "*"
                print("Alice didn't make it to the tea party.")
                break

            elif matrix[next_row][next_collumn] in numbers:
                tea_bags += int(matrix[next_row][next_collumn])
                matrix[next_row][next_collumn] = "*"
                if tea_bags >= 10:
                    alice_makes_it = True
                    break
        else:
            print("Alice didn't make it to the tea party.")
            break
    
    elif command == "left":
        next_row = alice_pos[0]
        next_collumn = alice_pos[1] - 1
        if is_valid(next_row, next_collumn):
            alice_pos = [next_row, next_collumn]

            if matrix[next_row][next_collumn] == ".":
                matrix[next_row][next_collumn] = "*"
            elif matrix[next_row][next_collumn] == "R":
                matrix[next_row][next_collumn] = "*"
                print("Alice didn't make it to the tea party.")
                break
            elif matrix[next_row][next_collumn] in numbers:
                tea_bags += int(matrix[next_row][next_collumn])
                matrix[next_row][next_collumn] = "*"
                if tea_bags >= 10:
                    alice_makes_it = True
                    break
        else:
            print("Alice didn't make it to the tea party.")
            break

if alice_makes_it:
    print("She did it! She went to the party.")


for row in range(len(matrix)):
    print(" ".join(matrix[row]))
