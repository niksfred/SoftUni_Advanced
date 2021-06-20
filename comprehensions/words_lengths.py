names = [x for x in input().split(", ")]
lenghts = [len(x) for x in names]

for i in range(len(names)):
    print(f"{names[i]} -> {lenghts[i]}", end='')
    if not i == (len(names) - 1):
        print(", ", end='')
