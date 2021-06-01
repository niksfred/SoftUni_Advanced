from collections import deque

water_quantity = int(input())
queue = deque()

name = input()
while not name == "Start":
    queue.append(name)
    name = input()

water_wanted = input()

while not water_wanted == "End":
    if "refill" in water_wanted:
        water = water_wanted.split()
        water_quantity += int(water[1])

    else:
        if int(water_wanted) <= water_quantity:
            water_quantity -= int(water_wanted)
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    
    water_wanted = input()

print(f"{water_quantity} liters left")