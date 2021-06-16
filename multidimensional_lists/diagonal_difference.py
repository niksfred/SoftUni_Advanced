size = int(input())
matrix = []

for i in range(size):
    matrix.append(list(map(int, input().split())))

result_primary = 0
for i in range(size):
    result_primary += matrix[i][i]

result_secondary = 0
row = size - 1 

for column in range(size):
    result_secondary += matrix[row][column]
    row -= 1

print(abs(result_primary - result_secondary))
