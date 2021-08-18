tasks = list(map(int, input().split(", ")))
task_needed = int(input())

time_for_tasks_faster_than_interested = [x for x in tasks if x < tasks[task_needed]]
for i in range(0, task_needed+1):
    if tasks[i] == tasks[task_needed]:
        time_for_tasks_faster_than_interested.append(tasks[i])

print(sum(time_for_tasks_faster_than_interested))
