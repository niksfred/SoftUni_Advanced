values = tuple(map(float, input().split()))
numbers = []

for el in values:
    if el not in numbers:
        numbers.append(el)

for num in numbers:
    print(f"{num} - {values.count(num)} times")
    
