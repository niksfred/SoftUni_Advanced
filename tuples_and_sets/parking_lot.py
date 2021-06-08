n = int(input())
cars = set()
for _ in range(n):
    action, plate = input().split(", ")
    if action == "IN":
        cars.add(plate)
    elif action == "OUT":
        cars.remove(plate)

if len(cars) > 0:
    for items in cars:
        print(items)
else:
    print("Parking Lot is Empty")
    