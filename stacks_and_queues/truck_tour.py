from collections import deque
queue = deque()
n_pumps = int(input())

for _ in range(n_pumps):
    gas_pump = input().split()
    queue.append([int(gas_pump[0]), int(gas_pump[1])])

for idx in range(n_pumps):
    fuel_tank = 0
    current_gas_pump = 0

    for gas_pump in queue:
        fuel, distance = gas_pump[0], gas_pump[1] 
        fuel_tank += fuel
        if fuel_tank < distance:
            break
        fuel_tank -= distance
        current_gas_pump += 1 
    
    if current_gas_pump == n_pumps:
        print(idx)
        break

    queue.rotate(-1)
