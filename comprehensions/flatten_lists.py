start_matrix = [[j for j in x.split()] for x in input().split("|")]
flat_matrix = [x for j in range(len(start_matrix)-1, -1, -1) for x in start_matrix[j]]
print(" ".join(flat_matrix))
