def first(matrix):
    first_diagonal = [matrix[j][j] for j in range(len(matrix))]
    print("First diagonal:", end=" ")
    for i in range(len(first_diagonal)):
        print(f"{first_diagonal[i]}", end='')
        if not i == (len(first_diagonal)-1):
            print(end=", ")
        else:
            print(end=". ")
    print(f"Sum: {sum([int(x) for x in first_diagonal])}")

def second_diagonal(matrix):
    second_diagonal = [matrix[j][(len(matrix)-1-j)] for j in range(len(matrix))]
    print("Second diagonal:", end=" ")
    for j in range(len(second_diagonal)):
        print(f"{second_diagonal[j]}", end='')
        if not j == (len(second_diagonal)-1):
            print(end=", ")
        else:
            print(end=". ")
    print(f"Sum: {sum([int(x) for x in second_diagonal])}")


matrix = [[j for j in input().split(", ")] for i in range(int(input()))]


first(matrix)
second_diagonal(matrix)
