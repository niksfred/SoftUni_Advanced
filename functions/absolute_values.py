sequence = list(map(float, input().split()))

absolute = lambda x: abs(x)
absolute_values = []

for value in sequence:
    absolute_values.append(absolute(value))

print(absolute_values)
