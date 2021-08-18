from collections import deque

def fill_the_box(height, lenght, width, *args):
    starting_volume = height * lenght * width
    volume = starting_volume
    cubes_to_put = deque()
    print(starting_volume)

    for cube in args:
        if not cube == "Finish":
            cubes_to_put.append(int(cube))
        elif cube == "Finish":
            break
    print(cubes_to_put)

    while cubes_to_put:
        if (volume - cubes_to_put[0]) >= 0:
            volume -= cubes_to_put.popleft()
            print(volume)
            
        else:
            cubes_to_put.append(starting_volume-volume)
            return f"No more free space! You have {sum(cubes_to_put) - starting_volume} more cubes."

    return f"There is free space in the box. You could put {volume} more cubes."

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))