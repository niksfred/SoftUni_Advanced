from collections import deque

working_bees = deque([int(el) for el in input().split(" ") if 0 <= int(el) <= 150])
nectars = [int(el) for el in input().split(" ") if 0 <= int(el) <= 150]
honey_making_symbols = deque(input().split(" "))
honey_made = 0

while len(working_bees) > 0 and len(nectars) > 0:
    if working_bees[0] <= nectars[-1]:
        bee = working_bees[0]
        nectar = nectars[-1]
        operator = honey_making_symbols[0]

        if operator == "+":
            honey_made += abs(bee + nectar)

        elif operator == "-":
            honey_made += abs(bee - nectar)

        elif operator == "*":
            honey_made += abs(bee * nectar)

        elif operator == "/":
            if nectar != 0:
                honey_made += abs(bee/nectar)
            
        working_bees.popleft()
        nectars.pop()
        honey_making_symbols.popleft()  

    else:
        nectars.pop()

print(f"Total honey made: {honey_made}")

if len(working_bees) > 0:
    print("Bees left: " + ", ".join(list(map(str, working_bees))))

if len(nectars) > 0:
    print("Nectar left: " + ", ".join(list(map(str, nectars))))
