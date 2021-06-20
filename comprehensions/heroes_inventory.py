names = {x:{} for x in input().split(", ")}

command_start = input()
while not command_start == "End":
    command = command_start.split("-")
    if command[1] not in names[command[0]]:
        names[command[0]][command[1]] = int(command[2])

    command_start = input()

for key,value in names.items():
    print(f"{key} -> Items: {len(value)}, Cost: {sum(value.values())}")
