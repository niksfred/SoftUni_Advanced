rows, columns = map(int, input().split())

matrix = [[f"{chr(97+x)}{chr(97+j+x)}{chr(97+x)}" for j in range(columns)] for x in range(rows)]

for i in range(len(matrix)):
    print(" ".join(matrix[i]))
