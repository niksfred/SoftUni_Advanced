def sort_ascending(initial_list):
    return list(sorted(initial_list))

number_sequence = [int(el) for el in input().split()]
print(sort_ascending(number_sequence))

