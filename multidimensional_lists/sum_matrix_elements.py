matrix = []
result = 0

rows, columns = list(map(int, input().split(", ")))

for i in range(rows):
    matrix.append([])
    row_input = list(map(int, input().split(", ")))
    for el in row_input:
        matrix[i].append(el)

for i in range(rows):
    result += sum(matrix[i])
print(result)
print(matrix)
