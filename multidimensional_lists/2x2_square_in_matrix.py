rows, columns = map(int, input().split())
matrix = []
result = 0

for row in range(rows):
    matrix.append(input().split())

for i in range(rows -1 , 0, -1):
    for j in range(columns - 1 , 0, -1):
        if matrix[i-1][j-1] == matrix[i-1][j] == matrix[i][j-1] == matrix[i][j]:
            result += 1

print(result)
