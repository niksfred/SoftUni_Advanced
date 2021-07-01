def even_numbers(initial_list):
    even_nums = list(filter(lambda x: x % 2 == 0, initial_list))
    print(even_nums)
number_sequence = [int(el) for el in input().split()]
even_numbers(number_sequence)
