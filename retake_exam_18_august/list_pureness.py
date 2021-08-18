from collections import deque
def best_list_pureness(value_list , k):
    deque_of_values = deque(value_list)
    result_sum = 0
    result_rotation = 0
    for rotation in range(k+1):
        sum = 0
        for index in range(len(deque_of_values)):
            sum += deque_of_values[index] * index 
        if sum > result_sum:
            result_sum = sum
            result_rotation = rotation
        deque_of_values.rotate()
    return f"Best pureness {result_sum} after {result_rotation} rotations"

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
