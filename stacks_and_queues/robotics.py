from collections import deque


name, time = input().split("-")
robot = [name, int(time), "free", []]

#robot = input().split("-")
#robot[1] = int(robot[1])
#robot.append("free")
#robot.append([])

time = list(map(int, input().split(":")))   #time input

items = deque()
item = input()
while not item == "End":
    items.append(item)
    item = input()

while not len(items) == 0:
    time[2] += 1
    if time[2] == 60: #clock
        time[1] += 1
        time[2] = 0
        if time[1] == 60:
            time[0] += 1
            time[1] = 0
    
    if robot[2] == "free":
        robot[2] = "busy"
        item = items.popleft()
        robot[3] = time.copy()
        print(f"{robot[0]} - {item} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")
        robot[3][2] += (robot[1] - 1)
        if robot[3][2] >= 60: # end time calculation
            robot[3][2] -= 60
            robot[3][1] += 1
            if time[1] >= 60:
                robot[3][0] += 1
    
    elif robot[2] == "busy":
        if robot[3] == time:
            robot[2] = "free"

