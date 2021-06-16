def read_matrix(num_rows):
    matrix = []
    for _ in range(num_rows):
        nums= input().split()
        nums = [int(el) for el in nums]
        matrix.append(nums)
    
    return matrix

num_rows, num_cols = input().split()
num_rows, num_cols = int(num_rows), int(num_cols)

matrix = read_matrix(num_rows)
pos = []
max_result = None

for i in range(num_rows-2):
    for j in range(num_cols-2):
        current_result =sum([ matrix[i][j], matrix[i][j+1], matrix[i][j+2],
                            matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2],
                            matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2],
                            ])

        if max_result is None or max_result < current_result:
            max_result = current_result
            pos.clear()
            pos.append(i)
            pos.append(j)

pos_i = pos[0]
pos_j = pos[1]

print(f"Sum = {max_result}")
for i in range(3):
    for j in range(3):
        print(matrix[pos_i+i][pos_j+j], end=" ")
    print()
