n = int(input())
element_set = set()

for _ in range(n):
    elements = input().split()
    for el in elements:
        element_set.add(el)

for el in element_set:
    print(el)
