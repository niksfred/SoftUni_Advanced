matrix = [[x for x in map(int, input().split(", "))] for j in range(int(input()))]

print([x for sublist in matrix for x in sublist])
