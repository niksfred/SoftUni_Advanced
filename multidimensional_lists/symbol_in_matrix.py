n = int(input())
matrix = []
found = False

for row in range(n):
    matrix.append([])
    row_input = input()
    for column in range(n):
        matrix[row].append(row_input[column])

search = input()
for i in range(n):
    for j in range(n):
        if matrix[i][j] == search:
            found = True
            break
    if found:
        break
if found:
    print(f"({i}, {j})")
else:
    print(f"{search} does not occur in the matrix")
