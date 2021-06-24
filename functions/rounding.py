sequence = list(map(float, input().split()))

round_value = lambda x: round(x)
rounded_values = []

for value in sequence:
    rounded_values.append(round_value(value))

print(rounded_values)
