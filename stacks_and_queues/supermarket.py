from collections import deque
line = deque()

customer = input()

while not customer == "End":
    if customer == "Paid":
        while line:
            print(line.popleft())
    else:
        line.append(customer)
    
    customer = input()

print(f"{len(line)} people remaining.")
