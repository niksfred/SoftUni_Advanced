def logged(ref_func):
    def wrapper(*args):
        lenght = ref_func(*args)

        return f"you called {ref_func.__name__}{args}\nit returned {lenght}"
    return wrapper

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))

