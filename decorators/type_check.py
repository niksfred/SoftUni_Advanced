def type_check(type):
    def decorator(ref_func):
        def wrapper(argument):
            if isinstance(argument, type):
                return ref_func(argument)
            else:
                return "Bad Type"
        return wrapper
    return decorator

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

