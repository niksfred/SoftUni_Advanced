n = int(input())
names = set()

for _ in range(n):
    name = input()
    names.add(name)

while names:
    print(names.pop())
