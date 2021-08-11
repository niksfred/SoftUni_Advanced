def vowel_filter(function):

    def wrapper():
        vowels = "AaEeUuYyIiOo"
        string = function()
        new_result = [char for char in string if char in vowels]
        return new_result

    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
