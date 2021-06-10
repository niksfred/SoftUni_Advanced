n = int(input())
set_even = set()
set_odd = set()
result = 0
for row in range(1, n+1):
    name = input()
    result = 0
    for char in name:
        result += ord(char)
    result = result // row
    if result % 2 == 0:
        set_even.add(result)
    else:
        set_odd.add(result)
        
if sum(set_even) == sum(set_odd):
    print(", ".join(map(str, (set_odd | set_even))))
elif sum(set_odd) > sum(set_even):
    print(", ".join(map(str, set_odd.difference(set_even))))
else:
    print(", ".join(map(str, set_even.symmetric_difference(set_odd))))
