n = int(input())
saved_result = []
result = []

for _ in range(n):
    first_range, second_range = input().split("-")
    
    first_range_as_list = list(map(int, first_range.split(",")))
    set_1 = set()
    for i in range(first_range_as_list[0], first_range_as_list[1] + 1):
        set_1.add(i)
    
    second_range_as_list = list(map(int, second_range.split(",")))
    set_2 = set()
    for i in range(second_range_as_list[0], second_range_as_list[1] + 1):
        set_2.add(i)

    intersection = set_1 & set_2

    if len(intersection) > len(result):
        result = list(intersection)

print(f"Longest intersection is {result} with length {len(result)}")
