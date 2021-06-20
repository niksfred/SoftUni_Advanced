matrix = [[int(j) for j in input().split()] for i in range(int(input()))]

command = input()

while not command == "END":
    action, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)

    if action == "Add" and 0 <= row <= (len(matrix)-1) and 0 <= col <= (len(matrix[row])-1):
        matrix[row][col] += value
    elif action == "Subtract" and 0 <= row <= (len(matrix)-1) and 0 <= col <= (len(matrix[0])-1):
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    command = input()

str_matrix = [[str(j) for j in matrix[i]] for i in range(len(matrix))]

for i in range(len(str_matrix)):
    print(" ".join(str_matrix[i]))
