def tags(tag):
    def decorator(ref_func):
        def wrapper(*args):
            result = f"<{tag}>" + f"{ref_func(*args)}" + f"</{tag}>"
            return result
        return wrapper
    return decorator

@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))
