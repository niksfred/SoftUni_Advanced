from collections import deque

children = deque(input().split())
n_toss = int(input())
n = 0

while len(children) > 1:
    n += 1
    if n == n_toss:
        n = 0
        print(f"Removed {children.popleft()}")
    else:
        children.append(children.popleft())

print(f"Last is {children.popleft()}")
