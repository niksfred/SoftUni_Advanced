no_vowels = [x for x in input() if not (x=='A' or x=='a' or x=='E' or x =='e' or x=='I'
 or x=='i' or x=='O' or x=='o' or x=='U' or x=='u')]

print("".join(no_vowels))
