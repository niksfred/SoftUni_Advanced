def odd_even(type, nums):
    if type == "Odd":
        odd = list(filter(lambda x: x % 2 == 1, nums))
        return sum(odd)*len(nums)
    elif type == "Even":
        even = list(filter(lambda x: x % 2 == 0, nums))
        return sum(even)*len(nums)
command = input()
numbers = [int(el) for el in input().split()]

print(odd_even(command, numbers))
