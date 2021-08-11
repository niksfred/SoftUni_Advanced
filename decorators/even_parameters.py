def even_parameters(ref_func):
    def wrapper(*args):
        for el in args:
            if isinstance(el, str):
                return "Please use only even numbers!"
            if el % 2 == 0:
                continue
            else:
                return "Please use only even numbers!"
        return ref_func(*args)
    return wrapper

@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))


