def min_number(nums):
    minimum_number = min(nums)
    return f"The minimum number is {minimum_number}"

def max_number(nums):
    maximum_number = max(nums)
    return f"The maximum number is {maximum_number}"

def sum_numbers(nums):
    return f"The sum number is: {sum(nums)}"

number_sequence = [int(el) for el in input().split()]

print(min_number(number_sequence))
print(max_number(number_sequence))
print(sum_numbers(number_sequence))
