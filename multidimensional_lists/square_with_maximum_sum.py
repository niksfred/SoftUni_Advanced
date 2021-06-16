rows, columns = map(int, input().split(", "))
matrix = []
result = 0

for row in range(rows):
    matrix.append(list(map(int, input().split(", "))))


for i in range(rows -1 , 0, -1):
    for j in range(columns - 1 , 0, -1):
        current_sum = matrix[i-1][j-1] + matrix[i-1][j] + \
                      matrix[i][j-1] + matrix[i][j]
        if current_sum >= result:
            result = current_sum
            position = [i, j]

print(matrix[position[0]-1][position[1]-1], matrix[position[0]-1][position[1]])
print(matrix[position[0]][position[1]-1], matrix[position[0]][position[1]])
print(result)
