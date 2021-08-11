def make_bold(ref_func):
    def wrapper(*args):
        orig_string = ref_func(*args)
        return f"<b>{orig_string}</b>"
    return wrapper

def make_italic(ref_func):
    def wrapper(*args):
        orig_string = ref_func(*args)
        return f"<i>{orig_string}</i>"
    return wrapper

def make_underline(ref_func):
    def wrapper(*args):
        orig_string = ref_func(*args)
        return f"<u>{orig_string}</u>"
    return wrapper

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
