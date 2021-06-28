from collections import deque

chocolate = [int(x) for x in input().split(", ") if -100 < int(x) < 100]
milk = deque([int(x) for x in input().split(", ") if -100 < int(x) < 100])

milkshakes = 0

while len(chocolate) > 0 and len(milk) > 0:

    if chocolate[-1] <= 0 and milk[0] <= 0:
        chocolate.pop()
        milk.popleft()
        continue

    if chocolate[-1] <= 0:
        chocolate.pop()
        continue
   
    if milk[0] <= 0:
        milk.popleft()
        continue

    if milk[0] == chocolate[-1]:
        milkshakes += 1 
        chocolate.pop()
        milk.popleft()
    else:
        milk.rotate(-1)
        chocolate[-1] -= 5
        continue

    if milkshakes >= 5:
        break

if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocolate) > 0:
    print(f"Chocolate:", ", ".join([str(x) for x in chocolate]))
else:
    print("Chocolate: empty")

if len(milk) > 0:
    print(f"Milk:", ", ".join([str(x) for x in milk]))
else:
    print("Milk: empty")
    
