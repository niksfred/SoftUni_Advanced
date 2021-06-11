matrix = []
result = 0

n = int(input())

for i in range(n):
    matrix.append([])
    row_input = list(map(int, input().split()))
    for el in row_input:
        matrix[i].append(el)

for i in range(n):
    result += matrix[i][i]

print(result)
