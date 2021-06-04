lines = int(input())
stack = []


for i in range(lines):
    command = input().split()

    if command[0] == "1":
        stack.append(command[1])
    elif command[0] == "2":
        if len(stack) > 0:
            stack.pop()        
    elif command[0] == "3":
        if len(stack) > 0:
            print(max(stack))
    elif command[0] == "4":
        if len(stack) > 0:
            print(min(stack))


print(", ".join(reversed(stack)))
