inpt = [int(x) for x in input().split(", ")]

positive = [str(x) for x in inpt if x >= 0]
negative = [str(x) for x in inpt if x < 0]
even = [str(x) for x in inpt if x % 2 == 0 or x == 0]
odd = [str(x) for x in inpt if not x % 2 == 0]

print("Positive:", ", ".join(positive))
print("Negative:", ", ".join(negative))
print("Even:", ", ".join(even))
print("Odd:", ", ".join(odd))

