contact = input()
phone_dic = {}
while not contact[0].isdigit():
    name, number = contact.split("-")
    phone_dic[name] = number
    
    contact = input()
n = int(contact)

for _ in range(n):
    name = input()
    if name in phone_dic:
        print(f"{name} -> {phone_dic[name]}")
    else:
        print(f"Contact {name} does not exist.")
