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

command = input()

while command != "END":
    command = command.split()
