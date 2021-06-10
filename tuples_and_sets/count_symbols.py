string = input()
char_list = []
result_dict = {}

for char in string:
    char_list.append(char)

for char in string:
    result_dict[char] = char_list.count(char)

for key, value in sorted(result_dict.items()):
    print(f"{key}: {value} time/s")
